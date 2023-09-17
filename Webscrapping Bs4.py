# Scrapping using Request Module

import requests
from bs4 import BeautifulSoup

# r=requests.get("https://www.timesjobs.com/get")
# r=requests.get(" https://httpbin.org/get")
r=requests.get("https://latif-real-estate.000webhostapp.com/get")

soup=BeautifulSoup(r.text,"html.parser")

if r.status_code == 200:
    print("Working....")
else:
    print("Error occur")   

# print(soup.prettify)   

# print(soup.title.string)

# print(soup.get_text())

# print(soup.find_all("a"))
# print(soup.find_all("container"))

# for i in soup.find_all("a"):
#     print(i.get("href"))


# for child in soup.find(class_="container").childrens:
#     print(child)

cnt=soup.find(class_="container")
print(cnt.has_attr("class"))



# Note: 
#1. Websites usually do not give access/permission to scrap their Data. 
#2.These types of modules requires proxy to scrap Data, So i Initially test on different website that has no restriction. 
