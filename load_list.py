import pickle

with open("./data/naver_url.txt", "rb") as fp:   # Unpickling
    nvaer_url_list = pickle.load(fp)
    print(nvaer_url_list)
    print(len(nvaer_url_list))

with open("./data/book_list_author.txt", "rb") as fp:   # Unpickling
    author_list = pickle.load(fp)
    print(author_list)
    print(len(author_list))


with open("./data/book_list_img.txt", "rb") as fp:   # Unpickling
    img_list = pickle.load(fp)
    print(img_list)
    print(len(img_list))


with open("./data/book_list_title.txt", "rb") as fp:   # Unpickling
    title_list = pickle.load(fp)
    print(title_list)
    print(type(title_list))


with open("./data/book_list_url.txt", "rb") as fp:   # Unpickling
    url_list = pickle.load(fp)
    print(url_list)
    print(type(url_list))

