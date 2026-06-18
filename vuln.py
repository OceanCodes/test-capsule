import sqlite3
def get_user(name):
    conn = sqlite3.connect("db")
    conn.cursor().execute("SELECT * FROM users WHERE name = '" + name + '")
