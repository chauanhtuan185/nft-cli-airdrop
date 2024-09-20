import json
import csv
from web3 import Web3

RPC = "https://public-en-cypress.klaytn.net"
w3 = Web3(Web3.HTTPProvider(RPC))

contract_address = Web3.to_checksum_address('0xce70eef5adac126c37c8bc0c1228d48b70066d03')

with open("abi.json", "r") as read_file:
    contract_abi = json.load(read_file)

nft_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

total_supply = nft_contract.functions.totalSupply().call()

def get_all_holders(total_supply):
    holders = {}
    for token_id in range(1, total_supply + 1):
        try:
            owner = nft_contract.functions.ownerOf(token_id).call()
            if owner not in holders:
                holders[owner] = 0
            holders[owner] += 1  
        except Exception as e:
            print(f"Error for token ID {token_id}: {e}")
    return holders

holders = get_all_holders(total_supply)

with open('holders.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Holder Address', 'NFT Count'])  
    for holder, count in holders.items():
        writer.writerow([holder, count])

print("Export to file holders.csv.")
