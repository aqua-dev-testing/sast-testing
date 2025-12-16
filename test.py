# insecure.py
import pymysql

def get_user(conn, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()
