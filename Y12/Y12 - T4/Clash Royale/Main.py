from flask import Flask, render_template, g, send_from_directory, abort, jsonify, request
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join('database', 'cards.db')
CARDS_FOLDER = os.path.join('database', 'Cards')  # Capital C
IMAGES_FOLDER = os.path.join('static', 'images')  # Add this line for background images

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Get the first table in the database automatically
def get_table_name():
    con = get_db()
    tables = con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    if not tables:
        raise Exception("No tables found in the database.")
    return tables[0][0]  # first table name

# Home page – list all cards
@app.route('/')
def index():
    table = get_table_name()
    con = get_db()
    try:
        cards = con.execute(f"SELECT * FROM {table}").fetchall()
    except sqlite3.OperationalError as e:
        return f"Database error: {e}"
    return render_template('index.html', cards=cards)

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

# Serve background images from /static/images/
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

# Search/Autocomplete API
@app.route('/api/search', methods=['GET'])
def search_cards():
    query = request.args.get('q', '').strip().lower()
    field = request.args.get('field', 'name').lower()
    limit = request.args.get('limit', 500, type=int)  # Increased from 10 to 500 to show all matching cards
    
    table = get_table_name()
    con = get_db()
    
    # Map search fields to table columns
    valid_fields = ['name', 'description', 'type', 'rarity', 'arena']
    if field not in valid_fields:
        field = 'name'
    
    try:
        # Get column names to ensure field exists
        cursor = con.execute(f"PRAGMA table_info({table})")
        columns = [row[1].lower() for row in cursor.fetchall()]
        
        if field not in columns:
            field = 'name'
        
        # Search query
        if query:
            results = con.execute(
                f"SELECT id, name, image, {field} FROM {table} WHERE LOWER({field}) LIKE ? LIMIT ?",
                (f'%{query}%', limit)
            ).fetchall()
        else:
            results = con.execute(
                f"SELECT id, name, image, {field} FROM {table} LIMIT ?",
                (limit,)
            ).fetchall()
        
        return jsonify([dict(r) for r in results])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)