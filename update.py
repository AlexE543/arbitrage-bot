import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    url = "https://www.predictit.org/api/marketdata/markets/"
    all_markets_url = "https://www.predictit.org/api/marketdata/all/"
    # markets = requests.get(all_markets_url).json()['markets']
    # market_ids = [markets[x]["id"] for x in range(len(markets))]
    # print(market_ids)
    # ids = [3698]
    # for id in ids:
    #     print(check_arbitrage(url, id))
    yes, no = find_arbitrage_markets(all_markets_url)
    print(yes)
    print(no)
    print(check_arbitrage(url, 6521))
def find_arbitrage_markets(url, epsilon=.08):
    res = requests.get(url).json()
    buyNoArbitrages = []
    buyYesArbitrages = []
    # Parse through markets to find arbitrages
    for market in res['markets']:
        id = market['id']
        # If the first price is None don't look at it
        if market['contracts'][0]['bestBuyYesCost'] != None and market['contracts'][0]['bestBuyYesCost'] > 3:
            bestBuyYes = [contract['bestBuyYesCost'] for contract in market['contracts'] if contract['bestBuyYesCost']]
        else:
            bestBuyYes = []
        if market['contracts'][0]['bestBuyNoCost'] != None and market['contracts'][0]['bestBuyNoCost'] > 3:
            bestBuyNo = [contract['bestBuyNoCost'] for contract in market['contracts'] if contract['bestBuyNoCost']]
        else:
            bestBuyNo = []
        if (bestBuyNo != [] or bestBuyYes != []):
            # If the cost is less than the number of contracts - 1 - epsilon we are good to buy
            if sum(bestBuyNo) <= len(bestBuyNo) - 1 - epsilon:
                buyNoArbitrages.append(id)
            # If the cost is less than 1 - epsilon we are good to buy
            if sum(bestBuyYes) <= 1 - epsilon and len(bestBuyYes) > 1:
                buyYesArbitrages.append(id)
    return buyYesArbitrages, buyNoArbitrages

def check_arbitrage(url, id, epsilon=0.08):
    parsed_info = {
        "id": [],
        "bestBuyYes": [],
        "bestBuyNo": []
    }
    res = requests.get(url+str(id)).json()
    for contract in res['contracts']:
        buy_no = contract['bestBuyNoCost']
        buy_yes = contract['bestBuyYesCost']
        if not buy_no or not buy_yes:
            break
        parsed_info["id"].append(contract['id'])
        parsed_info["bestBuyYes"].append(buy_yes) if buy_yes else parsed_info["bestBuyYes"].append(0)
        parsed_info["bestBuyNo"].append(buy_no) if buy_no else parsed_info["bestBuyNo"].append(0)
    buyAllCostNo = sum(parsed_info["bestBuyNo"])
    buyAllCostYes = sum(parsed_info["bestBuyYes"])

    if (parsed_info['bestBuyNo'] != [] or parsed_info['bestBuyYes'] != []):
        if (buyAllCostNo <= len(parsed_info["bestBuyNo"]) - 1 - epsilon) or (buyAllCostYes <= 1 - epsilon):
            return True
    return False

if __name__ == "__main__":
    main()
