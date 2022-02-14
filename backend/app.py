#!/usr/bin/env python3
import pymongo
import requests
from pathlib import Path
from pprint import pprint
from time import sleep

# save your api.weatherapi.com key in 'api-key' file
APIKEY = Path('api-key').read_text()

# initialize db-connection
client = pymongo.MongoClient('localhost', 27017)
db = client.weather_db
weather_data = db.weather_data

def main():
	
	locations = ['London', 'Berlin', 'Paris']
	
	while True:
		for loc in locations:	
			r = requests.get(
				f'https://api.weatherapi.com/v1/current.json?key={APIKEY}&q={loc}&aqi=no'
			)
			json = r.json()
			print(json['location']['name'], json['current']['temp_c'], 'Celcius')
			oid = weather_data.insert_one(json).inserted_id
			print(oid)
		print("sleeping 1min")
		sleep(60)


if __name__ == "__main__":
	main()