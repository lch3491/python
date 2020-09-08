import requests

res = requests.get('http://google.com')
print(res.status_code)