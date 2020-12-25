import pickle


test_list = [1, 2, 3, 4, 5]
test_list2 = [10, 20, 30, 40, 50]


class TestClass:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self) -> int:
        return self.a + self.b


with open("pickle_file.pickle", "wb") as file:
    pickle.dump((test_list, test_list2, TestClass), file)
