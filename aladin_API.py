import os
import sys
import requests
import json
import pickle

#key 불러오기
with open("./key/key.txt", "rb") as fp:   # Unpickling
    key = pickle.load(fp)

#url 정의 및 reqeust와 response
url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=ItemNewSpecial&MaxResults=100" \
      "&start=1&SearchTarget=Book&output=js&Version=20131101&CategoryId=50993"

response = requests.get(url)

#데이터 json으로 변환
response_json = json.loads(response.text)

#check
print(response_json)


item_list = response_json['item']

print(item_list)





title_list_title = []
for i in range(len(item_list)):
    temp_title = item_list[i]['title']
    title_list_title.append(temp_title)
print(len(title_list_title))

title_list_url = []
for i in range(len(item_list)):
    temp_url = item_list[i]['link']
    title_list_url.append(temp_url)
print(len(title_list_url))

title_list_img = []
for i in range(len(item_list)):
    temp_img = item_list[i]['cover']
    title_list_img.append(temp_img)
print(len(title_list_img))

title_list_author = []
for i in range(len(item_list)):
    temp_author = item_list[i]['author']
    title_list_author.append(temp_author)
print(len(title_list_author))

title_list_isbn = []
for i in range(len(item_list)):
    temp_isbn = item_list[i]['isbn13']
    title_list_isbn.append(temp_isbn)
print(len(title_list_isbn))


#url 정의 및 reqeust와 response
url_2 = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=Bestseller&MaxResults=100" \
      "&start=1&SearchTarget=Book&output=js&Version=20131101&CategoryId=50994"

response = requests.get(url_2)

#데이터 json으로 변환
response_json = json.loads(response.text)

#check
print(response_json)


item_list = response_json['item']

print(len(item_list))





for i in range(len(item_list)):
    print("a",len(title_list_title))
    temp_title = item_list[i]['title']
    title_list_title.append(temp_title)
    print(len(title_list_title))
print("b",len(title_list_title))


for i in range(len(item_list)):
    temp_url = item_list[i]['link']
    title_list_url.append(temp_url)
print(len(title_list_url))


for i in range(len(item_list)):
    temp_img = item_list[i]['cover']
    title_list_img.append(temp_img)
print(len(title_list_img))


for i in range(len(item_list)):
    temp_author = item_list[i]['author']
    title_list_author.append(temp_author)
print(len(title_list_author))

for i in range(len(item_list)):
    temp_isbn = item_list[i]['isbn13']
    title_list_isbn.append(temp_isbn)
print(len(title_list_isbn))

with open("./data/book_list_title.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list_title, fp)

with open("./data/book_list_url.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list_url, fp)

with open("./data/book_list_img.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list_img, fp)

with open("./data/book_list_author.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list_author, fp)

with open("./data/book_list_isbn.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list_isbn, fp)