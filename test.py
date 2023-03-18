import requests

url = "http://127.0.0.1:8000"

# FACTORIAL
try:
    request = requests.post(url + "/api/factorial", data ={
        "number":"-1"})
except Exception as e:
    print(e)

print(request.json())