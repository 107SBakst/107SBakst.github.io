import requests
import os
import json

url_base = "https://api.v2.emissions-api.org/api/v2/ozone/average.json?country={}&begin=2019-02-10&end=2021-02-11&limit=100&offset=0"

country = ['FRA', 'AUS', 'USA', 'GBR']

for i in country:
    URL = url_base.format(i)
    print(URL)

data = requests.get(URL).json()

fileName = "data_airquality_ozone_"+str(i)+".json"

print(fileName)

with open(fileName, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_acsii=False, indent=4)
