import sqlite3
from crazyimports.common import ExDataLoader


class SQLite(ExDataLoader):
    ext = ".sqlite3"

    def exec_module(self, mod):
        conn = sqlite3.connect("database.sqlite3")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()

        data = {}
        for table in tables:
            cur.execute("SELECT * FROM {}".format(table["name"]))
            data[table["name"]] = cur.fetchall()
        
        cur.close()
        conn.close()

        self.repack(mod, data)
