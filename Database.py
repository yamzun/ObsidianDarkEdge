import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    subscribed INTEGER,
    expiry TEXT
)
""")
conn.commit()

def add_user(user_id):
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (user_id, 0, None))
    conn.commit()

def subscribe_user(user_id, days=30):
    expiry = (datetime.now() + timedelta(days=days)).isoformat()
    cursor.execute("UPDATE users SET subscribed=1, expiry=? WHERE user_id=?", (expiry, user_id))
    conn.commit()

def is_subscribed(user_id):
    cursor.execute("SELECT expiry FROM users WHERE subscribed=1 AND user_id=?", (user_id,))
    row = cursor.fetchone()
    if not row or not row[0]:
        return False
    return datetime.fromisoformat(row[0]) > datetime.now()
