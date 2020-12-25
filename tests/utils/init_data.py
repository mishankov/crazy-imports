import sqlite3
import pickle


def init_db(extension: str):
    conn = sqlite3.connect(
        "tests/test_data/generated/database_{}.{}".format(extension, extension)
    )
    cur = conn.cursor()

    cur.execute("CREATE TABLE text_table (id integer PRIMARY KEY, text text)")
    cur.execute("INSERT INTO text_table (id, text) VALUES (?, ?)", (1, "text_snippet"))

    conn.commit()
    cur.close()
    conn.close()


class TestClass:
    def __init__(a: int, b: int):
        self.a = a
        self.b = b

    def sum(self) -> int:
        return self.a + self.b


def init_pickle():
    test_list = [1, 2, 3, 4, 5]

    with open("tests/test_data/generated/pickle_file.pickle", "wb") as file:
        pickle.dump((test_list), file)


if __name__ == "__main__":
    init_db("sqlite")
    init_db("sqlite3")
    init_pickle()
