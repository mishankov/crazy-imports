# Pickle

Create file with the name `init_pickle.py` and the folowing script

```python
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

```

Then create python file like this

```python
import crazyimports
from init_pickle import TestClass
import pickle_file


list1, list2, class1 = pickle_file.data

print(list1, list2)
print(class1(1, 2).sum())
```

All objects from Pickle file stored in a `<file_name>.data`. If there are multiple objects stored in Pickle file then `<file_name>.data` would be a `tuple`

Pickle files should have `.pickle` extension
