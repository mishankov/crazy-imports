import sqlite3
import crazyimports.sqlite
import tests.database as database


def test_sqlite():
    assert database.code[0]["code"] == "text_snippet"
