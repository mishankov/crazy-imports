# SQLite

Generate database file with folowing script

```python
import sqlite3

conn = sqlite3.connect("database.sqlite3")
cur = conn.cursor()

cur.execute("CREATE TABLE table(id integer PRIMARY KEY, text text)")

text_snippet = "orange"

cur.execute("INSERT INTO table (id, text) VALUES (?, ?)", (1, text_snippet))

conn.commit()
cur.close()
conn.close()
```

Then create python file like this

```python
import crazyimports
import database

print(database.table[0]["code"])
```

All tables from SQLite file stored in attributes of a imported module

SQLite files should have `.sqlite` or `.sqlite3` extensions
