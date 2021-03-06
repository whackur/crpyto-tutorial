import requests
import json


project_id = "e7a2c1da50a54b2d913f857b2988758c"
url = f"https://mainnet.infura.io/v3/{project_id}"

body = {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionByHash",
    "params": ["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"],
    "id": 1,
}

response = requests.post(url, data=json.dumps(body))
print(response.text)
