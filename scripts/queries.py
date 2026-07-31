import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\n===== {table_name} =====")
    cursor.execute(f'PRAGMA table_info("{table_name}")')
    columns = cursor.fetchall()

    for col in columns:
        print(col[1])

conn.close()