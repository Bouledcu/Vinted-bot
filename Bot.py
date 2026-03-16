import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1483007349898870948/JUYhAjFVXvVMHXvhb27fI_CmtfLfu_2oqispy5NQFBbRo-uDeinbnNgnnL1z8IMfHDoi"

SEARCHES = [
"nike",
"ralph lauren",
"lacoste",
"maillot lens",
"rc lens",
"playstation",
"ps5",
"nintendo switch",
"pokemon"
]

seen=set()

url="https://www.vinted.fr/api/v2/catalog/items"

def send(item):

 title=item["title"]
 price=item["price"]
 link=item["url"]
 photo=item["photo"]["url"]

 data={
 "embeds":[{
 "title":title,
 "url":link,
 "description":f"💰 {price}€",
 "image":{"url":photo}
 }]
 }

 requests.post(WEBHOOK,json=data)

while True:

 for search in SEARCHES:

  params={
  "search_text":search,
  "order":"newest_first"
  }

  r=requests.get(url,params=params)
  data=r.json()

  for item in data["items"]:

   if item["id"] not in seen:

    seen.add(item["id"])
    send(item)

 time.sleep(10)
