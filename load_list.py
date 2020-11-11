import pickle

with open("./data/book_list1.txt", "rb") as fp:   # Unpickling
    load_list = pickle.load(fp)
    print(load_list)
    print(type(load_list))

