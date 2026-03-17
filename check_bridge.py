import requests

# ✅ 여기만 바꾸면 돼요!
API_KEY = "ZNHNBZTI681MG2C8F745VKS9Z1P63HV68X"
TX_HASH = "0x05448faa4fd1d3aa43ec6679820dddf31caf0c425720df7ab5b6c9fb4a9fcea5"

# Base Sepolia 용 Etherscan API
url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": "84532",
    "module": "proxy",
    "action": "eth_getTransactionByHash",
    "txhash": TX_HASH,
    "apikey": API_KEY
}

print("📡 Bridge 트랜잭션 정보 조회 중...")
response = requests.get(url, params=params)
data = response.json()

if "result" not in data:
    print("❌ 오류:", data)
    exit()

tx = data["result"]

if tx is None or isinstance(tx, str):
    print("❌ 트랜잭션을 찾을 수 없어요. TX Hash를 확인해주세요.")
    print("응답:", data)
    exit()

nonce = int(tx["nonce"], 16)
value_wei = int(tx["value"], 16)
value_eth = value_wei / 10**18

print("\n✅ Bridge 트랜잭션 조회 성공!")
print(f"  TX Hash             : {tx['hash']}")
print(f"  From                : {tx['from']}")
print(f"  To (Bridge 컨트랙트) : {tx['to']}")
print(f"  Nonce               : {nonce}")
print(f"  브릿지 금액           : {value_eth:.10f} ETH")
print(f"  Block               : {int(tx['blockNumber'], 16)}")
print(f"\n🔗 Basescan 링크: https://sepolia.basescan.org/tx/{tx['hash']}")
print(f"\n📌 방향: Base Sepolia → Sepolia (L2 → L1 출금)")
