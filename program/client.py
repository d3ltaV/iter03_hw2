import requests

# Use requests package to call your api address http://127.0.0.1:5000/api/joke to display a funny joke

url = "http://127.0.0.1:5000/api/joke"
url2 = "http://127.0.0.1:5000/api/jokes/2"

response = requests.get(url)
print(response.json())

response2 = requests.get(url2)
print(response2.json())