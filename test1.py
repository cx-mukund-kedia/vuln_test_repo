import sqlite3

def setup_db():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur.execute("INSERT INTO users(username, password) VALUES ('alice', 'alicepass')")
    cur.execute("INSERT INTO users(username, password) VALUES ('bob', 'bobpass')")
    conn.commit()
    return conn

def get_user_vulnerable(conn, username_input):
    # <-- Vulnerable: building SQL by concatenating user input directly
    sql = f"SELECT id, username FROM users WHERE username = '{username_input}'"
    print("DEBUG vulnerable SQL:", sql)
    cur = conn.cursor()
    cur.execute(sql)   # executing concatenated SQL
    return cur.fetchall()

if __name__ == "__main__":
    conn = setup_db()

    # Normal lookup
    print("Normal lookup:")
    print(get_user_vulnerable(conn, "alice"))  # works as expected

    # Malicious input that performs SQL injection
    malicious = "' OR '1'='1"
    print("\nAttack input:", malicious)
    print(get_user_vulnerable(conn, malicious))  # returns all rows!
