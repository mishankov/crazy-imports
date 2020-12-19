import sqlite3


def init_db(extension: str):
    conn = sqlite3.connect(
        "tests/test_data/database_{}.{}".format(extension, extension)
    )
    cur = conn.cursor()

    cur.execute("CREATE TABLE text_table (id integer PRIMARY KEY, text text)")
    cur.execute("INSERT INTO text_table (id, text) VALUES (?, ?)", (1, "text_snippet"))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    init_db("sqlite")
    init_db("sqlite3")
