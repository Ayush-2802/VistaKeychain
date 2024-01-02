import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.instagram.com/accounts/login/")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text 
print(title)