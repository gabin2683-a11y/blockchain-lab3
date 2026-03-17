import requests

# ✅ 여기만 바꾸면 돼요!
API_KEY = "ZNHNBZTI681MG2C8F745VKS9Z1P63HV68X"
TX_HASH = "0x82b8c73a5056f92a49566fdf1df518f16b672399fc6e228bcbc1f5a91410d26e"

# Sepolia Etherscan API
url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": "11155111",
    "module": "proxy",
    "action": "eth_getTransactionByHash",
    "txhash": TX_HASH,
    "apikey": API_KEY
}

print("📡 트랜잭션 정보 조회 중...")
response = requests.get(url, params=params)
data = response.json()

tx = data.get("result")

if not tx:
    print("❌ 트랜잭션을 찾을 수 없어요. TX Hash를 확인해주세요.")
else:
    # nonce는 16진수로 오기 때문에 10진수로 변환
    nonce = int(tx["nonce"], 16)
    value_wei = int(tx["value"], 16)
    value_eth = value_wei / 10**18  # Wei → ETH 변환

    print("\n✅ 트랜잭션 조회 성공!")
    print(f"  TX Hash   : {tx['hash']}")
    print(f"  From      : {tx['from']}")
    print(f"  To (친구)  : {tx['to']}")
    print(f"  Nonce     : {nonce}")
    print(f"  전송량     : {value_eth:.6f} ETH")
    print(f"  Block     : {int(tx['blockNumber'], 16)}")
    print(f"\n🔗 Etherscan 링크: https://sepolia.etherscan.io/tx/{tx['hash']}")
