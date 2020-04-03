# Predictit Arbitrage Detection Bot
Web-scraping arbitrage bot to find arbitrage opportunities on online political betting site

# Setup
In order to setup simply install the following on pip
'''
pip install requests
pip install selenium
'''

# Running
In order to run the script, navigate into the directory containing update.py and input 
'''
python update.py
'''

# Reading the output
The out put should print to your command line two lists of number IDs. These number IDs are labeled buy/sell and correspond to markets on Predictit's website. If the list is empty there are no current arbitrage opportunities. If they are filled, go to that market on Predictit's website and make sure the market is able to be arbitraged (WIP: Writing a guide for this) then either buy or sell all the contracts.

### TODO:
[ ] Write a guide on how the arbitrage works (Math behind it)
[ ] Autocheck hourly
[ ] More advanced market detection
[ ] Auto trading (If I build the courage :D)
