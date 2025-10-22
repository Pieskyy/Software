import json
import sqlite3
import os

# === Path to JSON file ===
json_path = r"C:\Users\ANGIE\OneDrive\Documents\Adam - School\Software\Y12\Y12 - T4\database\cards.json"

# === Load JSON ===
with open(json_path, "r", encoding="utf-8") as f:
    cards = json.load(f)

if not isinstance(cards, list):
    raise ValueError("JSON must be a list of card objects!")

print(f"✅ Loaded {len(cards)} cards from JSON.")

# === Determine all unique keys across all cards ===
all_keys = set()
for card in cards:
    all_keys.update(card.keys())

# === Helper function to detect SQLite column types ===
def detect_type(value):
    if isinstance(value, bool):
        return "BOOLEAN"
    elif isinstance(value, int):
        return "INTEGER"
    elif isinstance(value, float):
        return "REAL"
    else:
        return "TEXT"

# === Build SQL column definitions ===
columns_sql = []
for key in all_keys:
    sample_value = None
    for card in cards:
        if key in card:
            sample_value = card[key]
            break
    # Lists stored as JSON text
    col_type = "TEXT" if isinstance(sample_value, list) else detect_type(sample_value)
    if key == "id":
        columns_sql.append(f"{key} {col_type} PRIMARY KEY")
    else:
        columns_sql.append(f"{key} {col_type}")

columns_sql_str = ", ".join(columns_sql)

# === Create SQLite DB in same folder as JSON ===
db_path = os.path.join(os.path.dirname(json_path), "cards.db")

# === Delete existing database file if it exists ===
if os.path.exists(db_path):
    os.remove(db_path)
    print("🗑️ Old database deleted.")

# === Create new database ===
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute(f"CREATE TABLE cards ({columns_sql_str})")
print("📦 New table created successfully.")

# === Insert all card data ===
for card in cards:
    row = {}
    for key in all_keys:
        value = card.get(key, None)
        if isinstance(value, list):
            value = json.dumps(value)
        row[key] = value

    columns = ", ".join(row.keys())
    placeholders = ", ".join("?" for _ in row)
    values = tuple(row.values())

    cursor.execute(f"INSERT INTO cards ({columns}) VALUES ({placeholders})", values)

conn.commit()
conn.close()

print(f"✅ Database successfully rebuilt at: {db_path}")
