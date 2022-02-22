from pprint import pprint
from os import system as cmd
import click
import requests
from bs4 import BeautifulSoup

with open('./html/trim.html', 'r') as f:
    webpage = f.read()

soup = BeautifulSoup(webpage, 'lxml')

items = soup.find_all('div', class_='catalog_item')
itemsReegion = soup.find('li', class_='over').text
print(f'{itemsReegion}')
for n, i in enumerate(items, start=1):
    itemName = i.find('div', class_='title').text.strip()
    itemPrice = i.find('span').text.strip()
    print(f'{n}: {itemName} {itemPrice} ')