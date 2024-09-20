# NFT Airdrop Tool

## Introduction

This tool is designed for project owners who want to conduct token airdrops to users holding their NFTs. With a user-friendly interface and intuitive interaction, you can easily:

* Check the number of users: Determine how many users are currently holding your NFTs.
* Count the number of NFTs: Know the total number of NFTs in circulation.
* Manage the list: Create a list of wallet addresses for the airdrop.
* Export data to csv file
  
## Usage
### Installation:

Clone the repository:
```bash
git clone https://github.com/chauanhtuan185/nft-cli-airdrop
```
Install required libraries:
```bash
cd nft-cli-airdrop
pip install -r requirements.txt
```
Run the script:
```bash
python main.py <contract_address> <path_to_abi.json>
```
* <contract_address>: The contract address of your NFT on the Klaytn blockchain.
* <path_to_abi.json>: The path to the ABI file of your contract (downloadable from KlaytnScope).

Requirements:
* NFT contract address: You need to know the exact address of your NFT contract on the Klaytn blockchain.
* Contract ABI: The ABI file containing information about the contract's functions and variables. You can download this from KlaytnScope.
* ABI visibility on KlaytnScope: Your NFT contract must be set to publicly display its ABI on KlaytnScope.

Notes:

* Klaytn blockchain: The tool currently supports the Klaytn blockchain.
* Customization: You can customize the script to fit your specific project needs.
