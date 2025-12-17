import MySQLdb 
def get_user_by_name(conn, name):
    # 🚨 SQLi: user input concatenated into SQL string
    query = "SELECT id, name FROM users WHERE name = '%s'" % name
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()
