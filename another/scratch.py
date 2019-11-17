import json
import requests

response = requests.get("http://127.0.0.1:8000/api/info/")
todos = json.dumps(response.text)
print(todos)
print(type(todos))
'''for dict_item in todos:
    print(dict_item)'''
