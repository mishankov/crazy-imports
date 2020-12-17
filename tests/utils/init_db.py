import sqlite3

conn = sqlite3.connect("tests/database.sqlite3")
cur = conn.cursor()

cur.execute("CREATE TABLE code(id integer PRIMARY KEY, code text)")

cur.execute("INSERT INTO code (id, code) VALUES (?, ?)", (1, "text_snippet"))

conn.commit()
cur.close()
conn.close()
