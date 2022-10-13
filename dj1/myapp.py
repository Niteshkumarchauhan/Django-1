import requests
import json
URL = " http://127.0.0.1:8000/preinfo/"
data = {
    'name' :'cyrus',
    'roll' : 5
}
json_data = json.dumps(data)
r = requests.post(url = URL, data =json_data)
data= r.json()
print(data)
