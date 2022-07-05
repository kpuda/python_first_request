import requests

url='http://api.open-notify.org/astros.json'

response = requests.get(url)

json = response.json()
json['people']
for person in json['people']:
    print(person)
