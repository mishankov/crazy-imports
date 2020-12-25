import crazyimports
from init_pickle import TestClass
import pickle_file


list1, list2, class1 = pickle_file.data

print(list1, list2)
print(class1(1, 2).sum())
