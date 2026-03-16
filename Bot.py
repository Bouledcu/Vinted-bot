import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1483007349898870948/JUYhAjFVXvVMHXvhb27fI_CmtfLfu_2oqispy5NQFBbRo-uDeinbnNgnnL1z8IMfHDoi"

SEARCHES = [
"nike",
"nike tech fleece",
"ralph lauren",
"lacoste",
"maillot lens",
"rc lens",
"maillot football",
"playstation",
"ps5",
"ps4",
"nintendo switch",
"pokemon",
"zelda",
"mario kart"
]

seen = set()

while True:

    for search in SEARCHES:

        url = "https://www.vinted.fr/api/v2/catalog/items"

        params = {
            "search_text": search,
            "order": "newest_first"
        }

        r = requests.get(url, params=params)

        try:
            data = r.json()
        except:
            continue

        for item in data.get("items", []):

            if item["id"] not in seen:

                seen.add(item["id"])

                title = item["title"]
                price = item["price"]
                link = item["url"]

                message = f"🆕 {title}\n💰 {price}€\n🔗 {link}"

                requests.post(WEBHOOK, json={"content": message})

    time.sleep(15)
