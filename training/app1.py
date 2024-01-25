import csv

filename = 'EVCS.csv'
keys = ('Station Name', 'New Georeferenced Column')
records = []

with open(filename, 'r') as file:
    parser = csv.DictReader(file)

    for row in parser:
        listkey = {key: row[key] for key in keys}
        records.append(listkey)

print(records[0:2])

record = records[0]
coords = record['New Georeferenced Column'].split("(")[-1].split(")")[0].split()
print(coords)

longitude, latitude = coords

print(longitude)
print(latitude)

for record in records:
    record['longitude'] = float(longitude)
    record['latitude'] = float(latitude)

print(records[0])