import requests

url = "http://127.0.0.1:8000"

# FACTORIAL
try:
    request = requests.post(url + "/api/factorial", data ={
        "number":"8"})
except Exception as e:
    print(e)

print(request.json())

# MEDIAN
try:
    request = requests.post(url + "/api/median", data ={
        "numbers":"1,2,3,4,5,6"})
except Exception as e:
    print(e)

print(request.json())