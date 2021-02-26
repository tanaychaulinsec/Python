import requests
req = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data=req.json()
t=data["list"]