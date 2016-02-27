# -*- coding: utf-8 -*-

import requests
import csv
import bs4

dicts = []

url = "https://www.zumper.com/blog/2015/07/the-10-most-luxurious-apartments-for-rent-in-nyc-right-now/"
r = requests.get(url)
soup = bs4.BeautifulSoup(r.content, "html.parser")

elements = soup.findAll('h3')
for e in elements:
    if len(e.getText()) > 20: # ignore the last few h3s w/ shorter length
        number = e.getText().split('.')[0].encode('utf-8')
        tail = e.getText().split('.')[1].encode('utf-8')
        neighborhood = tail.split('–')[0].strip()
        detail = tail.split('–')[1].strip()

        d = {'number': number, 'neighborhood': neighborhood, 'detail': detail}
        dicts.append(d)

with open('apartments.csv', 'w') as csvfile:
    fieldnames = dicts[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for d in dicts:
        writer.writerow(d)
