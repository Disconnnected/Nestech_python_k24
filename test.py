"""
import requests
from bs4 import BeautifulSoup

request = requests.get('https://vnexpress.net/tin-tuc-24h')

html_doc = request.text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find(id='down-app-popup_vne')) # result: None
print(soup.find(id='sis_slider')) # resutl: có kết quả"""


import requests
from bs4 import BeautifulSoup

request = requests.get('https://vnexpress.net/tin-tuc-24h')

html_doc = request.text
# f = open("web_vnexpress_2.txt", "w", encoding="utf-8")
# f.write(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find(id='sis_slider'))
