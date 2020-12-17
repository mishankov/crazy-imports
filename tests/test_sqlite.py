import sqlite3
import crazyimports.sqlite
import database


def test_sqlite():
    assert database.raw_data[0]["code"] == "text_snippet"
