import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/users", auth = ("user","pass"))
data = json.loads(r.text)
with open('API_ex.json', 'w', encoding = "utf-8") as f:
    json.dump(data, f)
name = input("Enter a username: ").lower()
found_name = False
for d in data:
    if d["username"].lower() == name:
        found_name = True
        for i,j in d.items():
            print(i,":",j)
if not found_name:
    print("Can't find your username.")