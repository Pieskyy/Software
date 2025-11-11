import sqlite3

conn = sqlite3.connect('database/cards.db')
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f'Tables found: {tables}')

if tables:
    table_name = tables[0][0]
    print(f'\nChecking table: {table_name}')
    
    count = conn.execute(f'SELECT COUNT(*) FROM {table_name}').fetchone()
    print(f'Total cards in DB: {count[0]}')
    
    # Check by rarity
    rarities = conn.execute(f'SELECT rarity, COUNT(*) FROM {table_name} GROUP BY rarity').fetchall()
    print('\nBy rarity:')
    for r, c in sorted(rarities):
        print(f'  {r}: {c}')

conn.close()
