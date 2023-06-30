import json
import csv

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'cameras.json'
your_city = input('What City? birmingham, mobile, montgomery, tuscaloosa, tuscumbia: ')

str_data = open(fname).read()
json_data = json.loads(str_data)

with open('cameras.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["CITY","MAIN ROAD", "CROSS ROAD", "LAT", "LONG"])
    for entry in json_data:
        for data_item in entry["entries"]:
            if not data_item['organizationId'] == your_city:
                continue
            city = data_item["organizationId"]
            road = data_item["primaryRoad"]
            cross_street = data_item["crossStreet"]
            lat = data_item["latitude"]
            long = data_item["longitude"]
            writer.writerow([city,road,cross_street,lat,long])




