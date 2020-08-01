import requests


class Scraper:

    def __init__(self):
        self.base_url = "https://www.predictit.org/api/marketdata"
        self.epsilon = .1
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.105 Safari/537.36"
        }

    """ 
        Checks all markets for arbitrage opportunities
        Returns: yes_ids: list of ids to buy all yes on
                 no_ids: list of ids to buy all no on
                 either_ids: list of ids to buy either all yes or all no on
    """
    def check_all_markets(self):
        url = self.base_url + "/all/"
        res = requests.get(url, headers=self.headers).json()
        yes_ids, no_ids, either_ids = [], [], []
        for market in res['markets']:
            market_id = market['id']
            p_yes_list = [contract['bestBuyYesCost'] for contract in market['contracts'] if contract['bestBuyYesCost']]
            p_no_list = [contract['bestBuyNoCost'] for contract in market['contracts'] if contract['bestBuyNoCost']]
            yes = len(p_yes_list) >= 2 and sum(p_yes_list) >= .8 and sum(p_yes_list) < (1 - self.epsilon)
            no = len(p_no_list) >= 2 and sum(p_no_list) >= (len(p_no_list) - 1.2) and sum(p_no_list) < (len(p_no_list) - 1 - self.epsilon)
            if yes and no:
                either_ids.append(market_id)
            elif yes and not no:
                yes_ids.append(market_id)
            elif not yes and no:
                no_ids.append(market_id)
        print(yes_ids)
        print(no_ids)
        print(either_ids)
        return yes_ids, no_ids, either_ids

    """ 
        Checks market <marketId> for arbitrage opportunities
        Returns: 0: Buy Yes, 1: Buy No, 2: Buy Either, None: Buy None
    """

    def check_market(self, marketId):
        url = self.base_url + '/markets/' + str(marketId)
        res = requests.get(url, headers=self.headers).json()
        sum_yes, num_yes = 0, 0
        sum_no, num_no = 0, 0
        for contract in res['contracts']:
            p_yes, p_no = contract['bestBuyYesCost'], contract['bestBuyNoCost']
            sum_yes += p_yes if p_yes else 0
            sum_no += p_no if p_no else 0
            num_yes += 1 if p_yes else 0
            num_no += 1 if p_no else 0
        yes, no = sum_yes >= .8 and sum_yes < (1 - self.epsilon), sum_no >= .8 and sum_no < (
                num_no - 1 - self.epsilon)
        print(marketId, sum_yes, sum_no, num_no)
        if yes and no:
            print("Buy Yes or No")
            return 2
        elif yes and not no:
            print("Buy Yes")
            return 0
        elif not yes and no:
            print("Buy No")
            return 1
        else:
            print("Buy None")
            return None


if __name__ == "__main__":
    s = Scraper()
    s.check_all_markets()
