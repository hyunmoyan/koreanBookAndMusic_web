import os
import sys
import requests
import json





import pickle

with open("./data/book_list_isbn.txt", "rb") as fp:   # Unpickling
    isbn_list = pickle.load(fp)
    print(isbn_list)
    print(len(isbn_list))
with open("./data/book_list_title.txt", "rb") as fp:   # Unpickling
    title_list = pickle.load(fp)
    print(title_list)
    print(type(title_list))
url_list = []

for i in range(len(isbn_list)):
    if isbn_list[i] !="":
        isbn = isbn_list[i]
        url = f"https://openapi.naver.com/v1/search/book.json?query={isbn}"  # json 결과

        header = {"X-Naver-Client-Id": "m5hV21pxqst1Jx50WMmS","X-Naver-Client-Secret": "scmdS_PNQl" }
        response = requests.get(url, headers = header)

        response_json = json.loads(response.text)
        print(response_json)
        url = response_json['items'][0]['link']
        print(url)
        url_list.append(url)
    # else:
    #     title = title_list[i]
    #     url = f"https://openapi.naver.com/v1/search/book.json?query={title}"  # json 결과
    #
    #     header = {"X-Naver-Client-Id": "m5hV21pxqst1Jx50WMmS", "X-Naver-Client-Secret": "scmdS_PNQl"}
    #     response = requests.get(url, headers=header)
    #
    #     response_json = json.loads(response.text)
    #     print(response_json)
    #     url = response_json['items'][0]['link']
    #     print(url)
    #     url_list.append(url)




with open("./data/naver_url.txt", "wb") as fp:   #Pickling
    pickle.dump(url_list, fp)