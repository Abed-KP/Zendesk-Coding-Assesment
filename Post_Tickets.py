import json
import requests


import requests

headers = {
    'content-Type': 'application/json',
}

with open('tickets.json.txt','r') as file:
    info = file.read()
    data = json.loads(info)
    print(type(data))

payload = json.dumps(data)
url = 'https://zccstudents5231.zendesk.com/api/v2/imports/tickets/create_many.json'

response = requests.post(url, headers=headers, data=payload, auth=('abed98kp@gmail.com', 'codingproject123'))
print(response)
