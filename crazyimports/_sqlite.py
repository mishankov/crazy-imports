import sqlite3
from ._common import ExDataLoader


class SQLite3(ExDataLoader):
    extensions = [".sqlite3", ".sqlite"]

    def exec_module(self, mod):
        data = self.load_data(mod.__spec__.origin)
        self.repack(mod, data)

    def load_data(self, db_path):
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()

        data = {}
        for table in tables:
            cur.execute("SELECT * FROM {}".format(table["name"]))  # nosec
            data[table["name"]] = cur.fetchall()

        return data
