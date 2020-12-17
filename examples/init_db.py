import sqlite3

conn = sqlite3.connect("database.sqlite3")
cur = conn.cursor()

cur.execute("CREATE TABLE code(id integer PRIMARY KEY, code text)")

code_snippet = """
class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
"""

cur.execute("INSERT INTO code (id, code) VALUES (?, ?)", (1, code_snippet))

conn.commit()
cur.close()
conn.close()
