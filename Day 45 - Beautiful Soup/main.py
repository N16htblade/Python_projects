#import requests
from bs4 import BeautifulSoup

PATH = "C:/PyLearning/projects/Day 45 - Beautiful Soup/website.html"


with open(PATH, encoding="utf-8") as file:
    content = file.read()
    data = BeautifulSoup(content, "html.parser")

ranking = []
names = data.find_all(name="h3")
for title in names:
    text = title.getText()
    ranking.append(text)
ranking.reverse()

for item in ranking:
    with open ("C:/PyLearning/projects/Day 45 - Beautiful Soup/list.txt", "a") as file:
        file.write(f"{item}\n")