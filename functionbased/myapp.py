from wsgiref import headers
from certifi import contents
import requests
import json
URL = " http://127.0.0.1:8000/preinfo/"
def get_data(id = None):
  data={}
  if id is not None:
   data={'id':id}
  json_data = json.dumps(data)
  headers = {'content-Type':'application/json'}
  r = requests.get(url = URL, headers = headers, data=json_data)
  data= r.json()
  print(data)
# get_data()

def post_data():
  data = {
    'name':'cyrus',
    'roll': 10,
  }
  headers = {'content-Type':'application/json'}
  json_data = json.dumps(data)
  r = requests.post (url = URL,headers = headers, data=json_data)
  data= r.json()
  print(data)

post_data()

def update_data():
  data = {
    'id': 6,
    'name':'mohit'
  }
  json_data = json.dumps(data)
  r = requests.put(url = URL, data=json_data)
  data= r.json()
  print(data)
# update_data()

def delete_data():
  data = {
    'id': 6,
  }
  json_data = json.dumps(data)
  r = requests.delete(url = URL, data=json_data)
  data= r.json()
  print(data)
# delete_data()