import matplotlib.pyplot as plt
import numpy as np
import requests
import json

ford = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=F&apikey=APIKEY&datatype=json")
ford_json = json.loads(ford.text)

toyota = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TM&apikey=APIKEY&datatype=json")
toyota_json = json.loads(toyota.text)

honda = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=HMC&apikey=APIKEY&datatype=json")
honda_json = json.loads(honda.text)

dodge = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=DODGX&apikey=APIKEY&datatype=json")
dodge_json= json.loads(dodge.text)

mazda = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MZDAY&apikey=APIKEY&datatype=json")
mazda_json = json.loads(mazda.text)

print(ford_json)
print("----------------")
print(toyota_json)
print("----------------")
print(honda_json)
print("----------------")
print(dodge_json)
print("----------------")
print(mazda_json)
