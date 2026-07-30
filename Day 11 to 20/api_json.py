import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

data = response.json()

print("Title:", data["title"])
print("Body:", data["body"])
print("User ID:", data["userId"])