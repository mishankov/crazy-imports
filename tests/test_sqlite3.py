import sqlite3
import crazyimports
import tests.test_data.database_sqlite3 as database


def test_sqlite_file_type():
    assert database.__file__.split(".")[-1] == "sqlite3"


def test_sqlite_text_type():
    assert type(database.text_table[0]["text"]) == str


def test_sqlite_text_value():
    assert database.text_table[0]["text"] == "text_snippet"


def test_sqlite_integer_type():
    assert type(database.text_table[0]["id"]) == int


def test_sqlite_integer_value():
    assert database.text_table[0]["id"] == 1
