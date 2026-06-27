import sqlite3

def init_db():
    conn = sqlite3.connect("osint.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        username TEXT,
        data TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT
    )
    """)
    conn.commit()
    return conn, cursor
