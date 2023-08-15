from utils.mint import mint, Client, Network
import json

c = Client(Network.mainnet().string())

def load():
    with open("wallets.json", "r") as f:
        wallets = json.load(f)
    return wallets

def main():
    wallets = load()
    for index, wallet in enumerate(wallets):
        m = mint(index, wallet, c)
        if m:
            print(f"Minted {index} to {wallet}")
        else:
            print(f"ERROR: Failed to mint {index} to {wallet}")
    
    print(f"Done! minted {len(wallets)} NFTs")