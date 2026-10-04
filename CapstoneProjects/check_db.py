import sqlite3
import os

# Check if database exists
db_path = 'eng_subtitles_database.db'
if os.path.exists(db_path):
    file_size = os.path.getsize(db_path)
    print(f"Database file exists. Size: {file_size / (1024*1024):.2f} MB")
else:
    print("Database file NOT found!")
    exit()

# Connect and check tables
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print(f"Found {len(tables)} tables:")
for table in tables:
    print(f"- {table[0]}")

# Check table structure
if tables:
    cursor.execute("PRAGMA table_info(zipfiles)")
    columns = cursor.fetchall()
    print(f"\nTable 'zipfiles' has {len(columns)} columns:")
    for col in columns:
        print(f"- {col[1]} ({col[2]})")

conn.close()