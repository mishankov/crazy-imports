import sqlite3
from crazyimports.common import ExDataLoader


class SQLite(ExDataLoader):
    ext = ".sqlite3"

    def exec_module(self, mod):
        conn = sqlite3.connect("code_database.sqlite3")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM code")
        data = cur.fetchall()
        cur.close()
        conn.close()

        self.repack(mod, data)
