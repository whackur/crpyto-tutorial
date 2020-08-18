import requests
import json


project_id = "e7a2c1da50a54b2d913f857b2988758c"
url = f"https://mainnet.infura.io/v3/{project_id}"

body = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f", "latest"],
    "id": 1,
}

response = requests.post(url, data=json.dumps(body))
print(response.text)
