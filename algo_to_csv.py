import json
import csv

#https://algotraffic.com/api/v1/layers/cameras

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'cameras.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

with open('cameras.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["CITY","MAIN ROAD", "CROSS ROAD", "LAT", "LONG"])
    for entry in json_data:
        for data_item in entry["entries"]:
            if not data_item['organizationId'] == "tuscaloosa":
                continue
            city = data_item["organizationId"]
            road = data_item["primaryRoad"]
            cross_street = data_item["crossStreet"]
            lat = data_item["latitude"]
            long = data_item["longitude"]
            writer.writerow([city,road,cross_street,lat,long])




