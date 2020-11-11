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

title_list = []
for i in range(len(item_list)):
    temp = item_list[i]['title']
    title_list.append(temp)
print(len(title_list))


with open("./data/book_list1.txt", "wb") as fp:   #Pickling
    pickle.dump(title_list, fp)


