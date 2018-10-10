import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import requests
import json

ford = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=F&apikey=KEY&datatype=json")
ford_json = json.loads(ford.text)

toyota = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TM&apikey=KEY&datatype=json")
toyota_json = json.loads(toyota.text)

honda = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=HMC&apikey=KEY&datatype=json")
honda_json = json.loads(honda.text)

dodge = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=DODGX&apikey=KEY&datatype=json")
dodge_json= json.loads(dodge.text)

gm = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=GM&apikey=KEY&datatype=json")
gm_json = json.loads(gm.text)

forddate = []
fordhighPrice = []
ford = ford_json['Monthly Time Series']
for key, value in ford.items():
    forddate.append(key)
    fordhighPrice.append(float(value['2. high']))
    if key == "2013-10-31":
        break
forddate.reverse()
fordhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(forddate, fordhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("Ford Stock Prices: Oct '13 - Oct '18")
axs.grid(True)
plt.xticks([])
fig.savefig("ford.png")


toyotadate = []
toyotahighPrice = []
toyota = toyota_json['Monthly Time Series']
for key, value in toyota.items():
    toyotadate.append(key)
    toyotahighPrice.append(float(value['2. high']))
    if key == "2013-10-31":
        break
toyotadate.reverse()
toyotahighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(toyotadate, toyotahighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("Toyota Stock Prices: Oct '13 - Oct '18")
axs.grid(True)
plt.xticks([])
fig.savefig("toyota.png")


hondadate = []
hondahighPrice = []
honda = honda_json['Monthly Time Series']
for key, value in honda.items():
    hondadate.append(key)
    hondahighPrice.append(float(value['2. high']))
    if key == "2013-10-31":
        break
hondadate.reverse()
hondahighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(hondadate, hondahighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("Honda Stock Prices: Oct '13 - Oct '18")
axs.grid(True)
plt.xticks([])
fig.savefig("honda.png")


dodgedate = []
dodgehighPrice = []
dodge = dodge_json['Monthly Time Series']
for key, value in dodge.items():
    dodgedate.append(key)
    dodgehighPrice.append(float(value['2. high']))
    if key == "2013-10-31":
        break
dodgedate.reverse()
dodgehighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(dodgedate, dodgehighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("Dodge Stock Prices: Oct '13 - Oct '18")
axs.grid(True)
plt.xticks([])
fig.savefig("dodge.png")


gmdate = []
gmhighPrice = []
gm = gm_json['Monthly Time Series']
for key, value in gm.items():
    gmdate.append(key)
    gmhighPrice.append(float(value['2. high']))
    if key == "2013-10-31":
        break
gmdate.reverse()
gmhighPrice.reverse()

fig, axs = plt.subplots()
axs.plot(gmdate, gmhighPrice)
axs.set_ylabel("Stock Price ($)")
axs.set_title("GM Stock Prices: Oct '13 - Oct '18")
axs.grid(True)
plt.xticks([])
fig.savefig("gm.png")
