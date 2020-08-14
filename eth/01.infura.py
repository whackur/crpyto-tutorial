from web3 import Web3
from conf import infura

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura["project_id"]}'))
print(w3.eth.blockNumber)
