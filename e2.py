import csv

with open("csv/weather.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row)