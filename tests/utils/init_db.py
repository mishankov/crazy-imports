import sqlite3

conn = sqlite3.connect("tests/test_data/database.sqlite3")
cur = conn.cursor()

cur.execute("CREATE TABLE text_table (id integer PRIMARY KEY, text text)")
cur.execute("INSERT INTO text_table (id, text) VALUES (?, ?)", (1, "text_snippet"))

conn.commit()
cur.close()
conn.close()
