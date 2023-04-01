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
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find(id='down-app-popup_vne'))
