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
    return scraper.check_market(marketId)

@app.route('/markets/check/all')
def check_all_markets():
    print("Checking all markets")
    scraper = Scraper()
    return scraper.check_all_markets()

if __name__ == "__main__":
    app.run()