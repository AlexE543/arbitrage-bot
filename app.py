from scraper import Scraper
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/market/check/<marketId>')
def check_market(marketId):
    print("Checking ", marketId)
    scraper = Scraper()
    result = scraper.check_market(marketId)
    if result == 0:
        return "Buy Yes"
    if result == 1:
        return "Buy No"

@app.route('/markets/check/all')
def check_all_markets():
    print("Checking all markets")
    scraper = Scraper()
    yes, no, either = scraper.check_all_markets()
    return {"Buy Yes": yes, "Buy No": no}

if __name__ == "__main__":
    app.run()