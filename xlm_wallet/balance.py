import requests

pub_key = "GBHJJSWIVPPK27UARRWUR2QG3GIWUVNM4FHX74XXF3Y46J3Q5L3NNMIG"
url = f"http://localhost/v1/wallets/XLM/balance/{pub_key}"

response = requests.request("GET", url, verify=False)

print(response.text.encode('utf8'))
