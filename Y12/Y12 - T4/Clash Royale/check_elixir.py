import sqlite3

con = sqlite3.connect('database/cards.db')
cursor = con.execute("SELECT name, elixir FROM cards WHERE name LIKE '%Spirit%' OR name LIKE '%Empress%' LIMIT 10")
rows = cursor.fetchall()
print("Elixir values for Spirit/Empress cards:")
for row in rows:
    print(f"  {row[0]}: {row[1]} (type: {type(row[1]).__name__})")

# Also check some normal cards
cursor = con.execute("SELECT name, elixir FROM cards WHERE name IN ('Goblin', 'Knight', 'Wizard') LIMIT 3")
rows = cursor.fetchall()
print("\nElixir values for normal cards:")
for row in rows:
    print(f"  {row[0]}: {row[1]} (type: {type(row[1]).__name__})")
