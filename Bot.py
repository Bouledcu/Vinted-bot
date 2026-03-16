import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1483087079775666350/cTNQikMitumsMOR1q6hUN12eZr8DP5oD9aPjKoeCyJE8NWmPLvyvMleTEW0psZGgqqJv"

SEARCHES = [
"nike",
"nike tech fleece",
"ralph lauren",
"lacoste",
"maillot lens",
"rc lens",
"maillot football",
"ps5",
"pokemon",
"nintendo switch"
]

seen = set()

requests.post(WEBHOOK, json={"content": "🟢 BOT VINTED ACTIF"})

while True:

    for search in SEARCHES:

        url = f"https://www.vinted.fr/api/v2/catalog/items?search_text={search}&per_page=5"

        try:
            r = requests.get(url)
            data = r.json()

            for item in data["items"]:

                if item["id"] not in seen:

                    seen.add(item["id"])

                    title = item["title"]
                    price = item["price"]
                    link = item["url"]

                    message = f"🆕 {title}\n💰 {price}€\n🔗 {link}"

                    requests.post(WEBHOOK, json={"content": message})l

        except:
            pass

    time.sleep(20)
