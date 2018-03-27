import requests
import json
import csv

user = "aimacode" #username whose github is to be scrapped
url = "https://api.github.com/repos/" + user + "/aima-python/contributors"
response = requests.get(url)
data = response.text

parsed = json.loads(data)
dat = []
list1 = []
for data1 in parsed :
    dat.append(data1['login'])
    list1.append(data1['contributions'])
    print((data1['login'] + ":").ljust(30) +str(data1['contributions']))

zip(dat, list1)

with open('micro.csv', 'w', encoding = "ISO-8859-1", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    fieldnames = ['Name', 'Commits']
    writer.writerow(fieldnames)
    writer.writerows(zip(dat, list1))
