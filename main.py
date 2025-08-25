import json
import time
from urllib.request import urlopen, Request

API = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

def fetch_prices():
    req = Request(API, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return {
        "bitcoin": data["bitcoin"]["usd"],
        "ethereum": data["ethereum"]["usd"],
    }

if __name__ == "__main__":
    try:
        prices = fetch_prices()
        print(f"BTC: ${prices['bitcoin']}")
        print(f"ETH: ${prices['ethereum']}")
    except Exception as e:
        print("Failed to fetch prices:", e)
        time.sleep(2)
        try:
            prices = fetch_prices()
            print(f"BTC: ${prices['bitcoin']}")
            print(f"ETH: ${prices['ethereum']}")
        except Exception as e2:
            print("Second attempt failed:", e2)
