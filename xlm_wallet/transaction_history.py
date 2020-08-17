import requests

public_key = "GDCMV6ZJIOU73HV3UZSPY7Y5SOHFSETL4QFEJWCOIJDO7JAACJIE4MHI"
url = f"https://localhost/v1/wallets/XLM/transactionHistory/{public_key}"

response = requests.request("GET", url, verify=False)

print(response.text)
