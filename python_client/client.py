import requests

endpoints="http://127.0.0.1:8000/car/list"

getresponse=requests.get(endpoints)
# print(getresponse.json())
print(getresponse.status_code)