from flask import request, jsonify
from db import get_db, get_table_name

#   SEARCHING
# https://www.youtube.com/watch?v=SrTn_tq2yNU&t=661s THis was used
# Search with auto coplete
# PERSONAL note "request.args.get" Sends a GET request


def search_cards(): 
    table = get_table_name()
    con = get_db() # connection


    query = request.args.get('q', '').strip().lower() # gets keyword of hte search
    field = request.args.get('field', 'name').lower() # column like name or description
    limit = request.args.get('limit', 125, type=int) # how many can show up, like 125 cards at most

    # Advanced filter
    rarity = request.args.get('rarity', '').strip() # this just means the user can search through
    unit = request.args.get('unit', '').strip()
    arena_val = request.args.get('arena', '').strip()
    elixir_min = request.args.get('elixir_min', type=int)
    elixir_max = request.args.get('elixir_max', type=int)
    evo = request.args.get('evo', '').strip()
    splash = request.args.get('splash', '').strip()
    spawn = request.args.get('spawn', '').strip()
    sort = request.args.get('sort', '').strip()


    try: # Get column names to ensure field exists and to validate sort column
        cursor = con.execute(f"PRAGMA table_info({table})") # PRAGMA table_info() returns info about every column in a table
        columns = [row[1].lower() for row in cursor.fetchall()] # extract just the column names


        if field not in columns:
            field = 'name' # if user gives a field not in there 

        # lists that will store WHERE conditions and parameter values
        where_clauses = [] # pieces of SQL like rarity = 'common'
        params = []

        if query: # Basic searching
            where_clauses.append(f"LOWER({field}) LIKE ?") # case senstitive match 
            params.append(f"%{query}%") # partial match

        # Advanced filters (user can filter by rarity, unit, arena, etc.)
        if unit:
            where_clauses.append("LOWER(unit) = ?")
            params.append(unit.lower())
        
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

        # boolean filters, like has evo
        truthy_clause = "{col} IS NOT NULL AND TRIM({col}) != '' AND LOWER({col}) NOT IN ('false','0','no','none')" 
        
        if evo: # truthy_clause is a reusable bit of SQL that checks if a column has a meaningful value.
            where_clauses.append(truthy_clause.format(col='evo'))

        if splash:
            where_clauses.append(truthy_clause.format(col='splash'))

        if spawn:
            if 'spawn_unit' in columns:
                where_clauses.append(truthy_clause.format(col='spawn_unit'))
           

        # the order by stuff 
        order_clause = ''
        if sort: # obviously asc is ascending, desc is descending
            if sort == 'name_asc':
                order_clause = 'ORDER BY name COLLATE NOCASE ASC'
            elif sort == 'name_desc':
                order_clause = 'ORDER BY name COLLATE NOCASE DESC'
            elif sort == 'rarity_asc':
                # Custom rarity order Common then Rare then Epic then Legendary then Champion
                order_clause = '''ORDER BY CASE 
                    WHEN rarity = 'Common' THEN 1
                    WHEN rarity = 'Rare' THEN 2
                    WHEN rarity = 'Epic' THEN 3
                    WHEN rarity = 'Legendary' THEN 4
                    WHEN rarity = 'Champion' THEN 5
                    ELSE 6
                END ASC'''
            elif sort == 'unit_asc':
                order_clause = '''ORDER BY CASE 
                    WHEN unit = 'Troop' THEN 10
                    WHEN unit = 'Air' THEN 11
                    WHEN rarity = 'Building' THEN 12
                END ASC'''
            elif sort == 'unit_desc':
                # Reverse unit order
                order_clause = '''ORDER BY CASE 
                    WHEN rarity = 'Troop' THEN 10
                    WHEN rarity = 'Air' THEN 11
                    WHEN rarity = 'Building' THEN 12
                END DESC'''
            elif sort == 'type_asc':
                order_clause = 'ORDER BY type ASC'
            elif sort == 'type_desc':
                order_clause = 'ORDER BY type DESC'
            elif sort == 'arena_asc':
                # Extract numeric part from arena
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
