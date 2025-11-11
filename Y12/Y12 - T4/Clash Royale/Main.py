from flask import Flask, render_template, g, send_from_directory, abort, jsonify, request
import sqlite3
import os

DATABASE = os.path.join('database', 'cards.db') # My database
CARDS_FOLDER = os.path.join('database', 'Cards') # Card images folder
app = Flask(__name__)



def get_db(): # get database connection
    if not hasattr(g, "db"):
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # to access columns by name
    return g.db



def get_table_name():
    connection = get_db() # Open the database
    result = connection.execute( # Get all table names in the database
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall()

    if len(result) == 0: # If there are no tables, give an error
        raise Exception("Your database has no tables.")
    
    first_table_name = result[0][0]# Return the name of the first table
    return first_table_name


@app.route('/')
def index():
    table_name = get_table_name() # Get the table name
    db = get_db()    # Connect to the database
    try:
        rows = db.execute(f"SELECT * FROM {table_name}").fetchall()# Select everything from that table
    except sqlite3.OperationalError as error:
        return f"Database error: {error}"
    return render_template("index.html", cards=rows)# Show the index.html page and give it the rows from the database

# Card detail page
@app.route('/card/<int:card_id>')
def card_detail(card_id):
    table = get_table_name()
    con = get_db()
    try:
        card = con.execute(f"SELECT * FROM {table} WHERE id=?", (card_id,)).fetchone()
    except sqlite3.OperationalError as e:
        return f"Database error: {e}"
    if not card:
        abort(404)
    return render_template('card_detail.html', card=card)

# Serve card images from /database/Cards/
@app.route('/Cards/<path:filename>')
def card_image(filename):
    return send_from_directory(CARDS_FOLDER, filename)



# Search/Autocomplete API
@app.route('/api/search', methods=['GET'])
def search_cards():
    query = request.args.get('q', '').strip().lower()
    field = request.args.get('field', 'name').lower()
    limit = request.args.get('limit', 500, type=int)
    # Advanced filter params
    rarity = request.args.get('rarity', '').strip()
    arena_val = request.args.get('arena', '').strip()
    elixir_min = request.args.get('elixir_min', type=int)
    elixir_max = request.args.get('elixir_max', type=int)
    evo = request.args.get('evo', '').strip()
    splash = request.args.get('splash', '').strip()
    spawn = request.args.get('spawn', '').strip()
    sort = request.args.get('sort', '').strip()
    
    table = get_table_name()
    con = get_db()
    
    # We'll validate against actual table columns below; keep requested field as-is for now
    
    try:
        # Get column names to ensure field exists and to validate sort column
        cursor = con.execute(f"PRAGMA table_info({table})")
        columns = [row[1].lower() for row in cursor.fetchall()]

        if field not in columns:
            field = 'name'

        # Build dynamic WHERE clause from query + advanced filters
        where_clauses = []
        params = []

        if query:
            where_clauses.append(f"LOWER({field}) LIKE ?")
            params.append(f"%{query}%")

        # advanced filters (use parameterized values)
        if rarity:
            where_clauses.append("LOWER(rarity) = ?")
            params.append(rarity.lower())

        if arena_val:
            # allow partial match on arena
            where_clauses.append("LOWER(arena) LIKE ?")
            params.append(f"%{arena_val.lower()}%")

        if elixir_min is not None:
            where_clauses.append("CAST(elixir AS INTEGER) >= ?")
            params.append(elixir_min)

        if elixir_max is not None:
            where_clauses.append("CAST(elixir AS INTEGER) <= ?")
            params.append(elixir_max)

        # boolean-like filters: check for non-empty/truthy values
        truthy_clause = "{col} IS NOT NULL AND TRIM({col}) != '' AND LOWER({col}) NOT IN ('false','0','no','none')"
        if evo:
            where_clauses.append(truthy_clause.format(col='evo'))

        if splash:
            where_clauses.append(truthy_clause.format(col='splash'))

        if spawn:
            # some datasets use 'spawn_unit' column for spawn behavior
            if 'spawn_unit' in columns:
                where_clauses.append(truthy_clause.format(col='spawn_unit'))
            elif 'spawn' in columns:
                where_clauses.append(truthy_clause.format(col='spawn'))

        # Determine ORDER BY from sort parameter
        order_clause = ''
        if sort:
            if sort == 'name_asc':
                order_clause = 'ORDER BY name COLLATE NOCASE ASC'
            elif sort == 'name_desc':
                order_clause = 'ORDER BY name COLLATE NOCASE DESC'
            elif sort == 'rarity_asc':
                # Custom rarity order: Common < Rare < Epic < Legendary < Champion
                order_clause = '''ORDER BY CASE 
                    WHEN rarity = 'Common' THEN 1
                    WHEN rarity = 'Rare' THEN 2
                    WHEN rarity = 'Epic' THEN 3
                    WHEN rarity = 'Legendary' THEN 4
                    WHEN rarity = 'Champion' THEN 5
                    ELSE 6
                END ASC'''
            elif sort == 'rarity_desc':
                # Reverse rarity order
                order_clause = '''ORDER BY CASE 
                    WHEN rarity = 'Common' THEN 1
                    WHEN rarity = 'Rare' THEN 2
                    WHEN rarity = 'Epic' THEN 3
                    WHEN rarity = 'Legendary' THEN 4
                    WHEN rarity = 'Champion' THEN 5
                    ELSE 6
                END DESC'''
            elif sort == 'type_asc':
                order_clause = 'ORDER BY type ASC'
            elif sort == 'type_desc':
                order_clause = 'ORDER BY type DESC'
            elif sort == 'arena_asc':
                # Extract numeric part from arena (handles "Arena 5", "5", "Training Camp", etc.)
                order_clause = '''ORDER BY CASE 
                    WHEN arena = 'Training Camp' THEN 0
                    WHEN arena LIKE 'Arena %' THEN CAST(SUBSTR(arena, 7) AS INTEGER)
                    ELSE CAST(arena AS INTEGER)
                END ASC'''
            elif sort == 'arena_desc':
                # Reverse arena numeric order
                order_clause = '''ORDER BY CASE 
                    WHEN arena = 'Training Camp' THEN 0
                    WHEN arena LIKE 'Arena %' THEN CAST(SUBSTR(arena, 7) AS INTEGER)
                    ELSE CAST(arena AS INTEGER)
                END DESC'''
            elif sort == 'elixir_asc':
                # Handle both numeric and array format like "[3, 6]" - extract the max value
                order_clause = '''ORDER BY CASE 
                    WHEN elixir LIKE '[%' THEN CAST(SUBSTR(elixir, INSTR(elixir, ',') + 2, LENGTH(elixir) - INSTR(elixir, ',') - 2) AS INTEGER)
                    ELSE CAST(elixir AS INTEGER)
                END ASC'''
            elif sort == 'elixir_desc':
                # Reverse: extract max value and sort descending
                order_clause = '''ORDER BY CASE 
                    WHEN elixir LIKE '[%' THEN CAST(SUBSTR(elixir, INSTR(elixir, ',') + 2, LENGTH(elixir) - INSTR(elixir, ',') - 2) AS INTEGER)
                    ELSE CAST(elixir AS INTEGER)
                END DESC'''
            elif sort == 'damage_asc':
                order_clause = 'ORDER BY CAST(damage AS INTEGER) ASC'
            elif sort == 'damage_desc':
                order_clause = 'ORDER BY CAST(damage AS INTEGER) DESC'
            elif sort == 'health_asc':
                order_clause = 'ORDER BY CAST(health AS INTEGER) ASC'
            elif sort == 'health_desc':
                order_clause = 'ORDER BY CAST(health AS INTEGER) DESC'

        # If no where_clauses and no query, fall back to previous behavior (rows where field is not empty)
        if not where_clauses:
            if field in ['evo', 'splash', 'spawn_unit', 'spawn']:
                # return truthy boolean-like rows
                where_clauses.append(truthy_clause.format(col=field))
            else:
                where_clauses.append(f"{field} IS NOT NULL AND TRIM({field}) != ''")

        where_sql = ' AND '.join(where_clauses)

        sql = f"SELECT id, name, image, {field} FROM {table} WHERE {where_sql} "
        if order_clause:
            sql += order_clause + ' '
        sql += 'LIMIT ?'
        params.append(limit)

        results = con.execute(sql, tuple(params)).fetchall()
        
        return jsonify([dict(r) for r in results])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)