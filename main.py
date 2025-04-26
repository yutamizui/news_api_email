import requests
from send_email import send_email

topic = "tesla"
apu_key = "52c36fd48e9f4a14834b653bd59ae425"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}" \
    "&from=2025-03-26" \
    "&sortBy=publishedAt" \
    "&apiKey=52c36fd48e9f4a14834b653bd59ae425" \
    "&language=en"
r = requests.get(url)
content = r.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += (
            (article["title"] or "") + "\n" +
            (article["description"] or "") + "\n" +
            (article["url"] or "") + "\n\n"
        )


send_email(message=body)