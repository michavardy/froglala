import requests
from bs4 import BeautifulSoup
import re

URL = "https://pump.fun/coin/GG9197MJXD55vqKfjXHMyq76rH57wa8dgHuMhCQEpump?coins_sort=market_cap"  # Replace with the actual page URL

def get_market_cap_text() -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return  [span.text for span in soup.find_all("span") if "market cap" in span.text][0]

def parse_market_cap(text:str) -> int:
    match = re.search(r"\$([\d,]+)", text)

    if match:
        market_cap = int(match.group(1).replace(",", ""))
        return market_cap

def get_market_cap()->int:
    market_cap_text = get_market_cap_text()
    market_cap_int = parse_market_cap(market_cap_text)
    return market_cap_int
    

if __name__ == "__main__":
    print(get_market_cap())