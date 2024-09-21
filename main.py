import json
import csv
import argparse
from web3 import Web3

def main(contract_address, abi_file):
    RPC = "https://public-en-cypress.klaytn.net"
    w3 = Web3(Web3.HTTPProvider(RPC))

    contract_address = Web3.to_checksum_address(contract_address)

    with open(abi_file, "r") as read_file:
        contract_abi = json.load(read_file)

    nft_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    total_supply = nft_contract.functions.totalSupply().call()

    def get_all_holders(total_supply):
        holders = {}
        for token_id in range(1, total_supply + 1):
            try:
                owner = nft_contract.functions.ownerOf(token_id).call()
                if owner not in holders:
                    holders[owner] = {
                        "nft_count": 0,
                        "balance": 0
                    }
                holders[owner]["nft_count"] += 1  
            except Exception as e:
                print(f"Error for token ID {token_id}: {e}")
        return holders

    holders = get_all_holders(total_supply)

    for holder in holders:
        try:
            balance = nft_contract.functions.balanceOf(holder).call()
            holders[holder]["balance"] = balance
        except Exception as e:
            print(f"Error getting balance for holder {holder}: {e}")

    with open('holders_with_balance.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Holder Address', 'NFT Count', 'Balance'])  
        for holder, data in holders.items():
            writer.writerow([holder, data['nft_count'], data['balance']])

    print("Export to file holders_with_balance.csv.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan NFT holders, get balances, and export to CSV.')
    parser.add_argument('contract_address', type=str, help='The address of the NFT contract')
    parser.add_argument
