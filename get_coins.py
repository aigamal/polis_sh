import requests
from requests.structures import CaseInsensitiveDict

#declare Headers
headers = CaseInsensitiveDict()
headers["Connection"] = "keep-alive"
headers["sec-ch-ua"] = ""Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92""
headers["Accept"] = "application/json, text/plain, */*"
headers["DNT"] = "1"
headers["sec-ch-ua-mobile"] = "?0"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
headers["Content-Type"] = "application/json;charset=UTF-8"
headers["Origin"] = "https://faucet.polis.tech"
headers["Sec-Fetch-Site"] = "same-site"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Dest"] = "empty"
headers["Referer"] = "https://faucet.polis.tech/"
headers["Accept-Language"] = "en-US,en;q=0.9"
url = "https://faucet-api.polis.tech/"

#rotate on the address
data = '{"address":"0x5a86b3c4dab2613f3bdd8eaafde17754cdf6df0d","network":"testnet"}'

#submit response 
resp = requests.post(url, headers=headers, data=data)

#Print results 
print(resp.status_code)