import pickle


test_list = [1, 2, 3, 4, 5]
test_list2 = [10, 20, 30, 40, 50]

with open("pickle_file.pickle", "wb") as file:
    pickle.dump((test_list), file)
