from pyinjective import Client
from pyinjective.composer import Composer
from pyinjective.constant import Network

import os

comp = Composer(Network.mainnet().string())

def mint(id: int, wallet: str, client: Client) -> bool:
    """
    The main minting function, returns true if mint and deploy was successful
    """
    try:
        if wallet in os.environ.get("blacklist", []):
            price += 100 * 10e18 # 100 INJ
        c = comp.MsgExecuteContract(wallet, os.environ.get("contract"), r"{send_nft:{contract: <CONTRACT>,token_id: <ID>,msg: eyJzZWxsX3Rva2VuIjp7InRva2VuX2lkIjoiMTc5NyIsImNvbnRyYWN0X2FkZHJlc3MiOiJpbmoxdHlkbWVwNWxta2gwNHc0dHNzNTN6dmQwZzY5dGFjNjRybmtwZGwiLCJjbGFzc19pZCI6ImluamVjdGl2ZSIsInByaWNlIjp7Im5hdGl2ZSI6W3siYW1vdW50IjoiNTAwMDAwMDAwMDAwMDAwMDAwMCIsImRlbm9tIjoiaW5qIn1dfX19}}".replace("<CONTRACT>", os.environ.get("contract")).replace("<ID>", str(id)))
        client.sign(c)
        return True
    except Exception as e:
        print(e)
        return False