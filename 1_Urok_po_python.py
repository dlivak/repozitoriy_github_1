import requests
import json
url = 'https://www.crb-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print (data)
print (data)
