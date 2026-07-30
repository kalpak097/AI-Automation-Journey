import requests

url = "https://jsonplaceholder.typicode.com/posts/999999"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print(data)
    elif response.status_code == 404:
        print("Data not found.")
    else:
        print("API returned status:", response.status_code)

except requests.RequestException as error:
    print("Request failed:", error)