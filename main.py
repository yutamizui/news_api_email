import requests

apu_key = "52c36fd48e9f4a14834b653bd59ae425"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-03-26&sortBy=publishedAt&apiKey=52c36fd48e9f4a14834b653bd59ae425"
r = requests.get(url)
content = r.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])