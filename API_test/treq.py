import requests

resp = requests.get('https://www.baidu.com')

print(resp.status_code)