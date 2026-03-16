import requests

WEBHOOK = "https://discord.com/api/webhooks/1483007349898870948/JUYhAjFVXvVMHXvhb27fI_CmtfLfu_2oqispy5NQFBbRo-uDeinbnNgnnL1z8IMfHDoi"

requests.post(WEBHOOK, json={"content":"TEST DISCORD BOT"})
