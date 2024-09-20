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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan NFT holders and export to CSV.')
    parser.add_argument('contract_address', type=str, help='The address of the NFT contract')
    parser.add_argument('abi_file', type=str, help='The path to the ABI JSON file')

    args = parser.parse_args()

    main(args.contract_address, args.abi_file)
