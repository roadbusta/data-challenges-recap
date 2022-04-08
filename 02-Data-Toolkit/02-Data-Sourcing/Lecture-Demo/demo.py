#import libraries
import requests
from bs4 import BeautifulSoup

url= "https://www.imdb.com/list/ls055386972/"

response = requests.get(url)

soup  = BeautifulSoup(response.content , "html.parser")


section_list = soup.find_all("div", class_="lister-item-content")

for section in section_list:
    title = section.find("a").string
    print(type(title))
    print(title)
