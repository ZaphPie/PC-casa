import requests

url = 'http://www.randomnumberapi.com/api/v1.0/random'
input = {
    "min": 100,
    "max": 1000,
    "count": 10
}
result = requests.get(url, data=input)
print(result.json())
