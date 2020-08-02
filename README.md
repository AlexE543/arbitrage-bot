# Predictit Arbitrage Detection Bot
Web-scraping arbitrage bot to find arbitrage opportunities on online political betting site

### Setup
In order to setup simply install the following on pip
```
pip install requests flask
```

### Running
In order to run the script, navigate into the directory containing app.py and input 
```
python app.py
```
This should start a local flask server with two callable endpoints

### Reading the output
The output should print to your a local webpage 3 lists of number IDs. These number IDs are labeled Buy Yes/Buy No and correspond to markets on Predictit's website. If the list is empty there are no current arbitrage opportunities. If they are filled, go to that market on Predictit's website and make sure the market is able to be arbitraged (WIP: Writing a guide for this) then either buy or sell all the contracts.

### TODO:
- [ ] Write a guide on how the arbitrage works (Math behind it)
- [ ] Autocheck hourly
- [ ] More advanced market detection
- [ ] Auto trading (If I build the courage :D)
