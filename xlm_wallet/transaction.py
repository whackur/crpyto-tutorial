import requests

url = "https://localhost/v1/wallets/XLM/transaction"

payload = {
    "toAddress": "GBHJJSWIVPPK27UARRWUR2QG3GIWUVNM4FHX74XXF3Y46J3Q5L3NNMIG",
    "amount": 3,
    "pinNumber": "111111",
    "memo": "안녕하세요",
}
headers = {
    "mnemonic": "ball goat team focus minor inmate push fashion grain fitness small address",
    "Content-Type": "application/json",
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text.encode("utf8"))
