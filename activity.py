import requests
import csv
url='https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'
# it is used to get the records from the dataset and split it into rows
with requests.get(url, stream=True) as req:
    lines = (lines.decode('utf-8') for lines in req.iter_lines())
    data = [row for row in csv.reader(lines)]

# print(data)
total=len(data)
print(f'total no. of records: {total}')

borough=[]
brooks=0

for row in data[1:]:
    if row[1] not in borough:
        borough.append(row[1])
    if row[1]=='Brooklyn':
        brooks +=1

borough.sort()
print(f'\n\nunique boroughs:\n {borough}')

print(f'\n\nBrooklyn boroughs: {brooks}')

output_file = 'taxi_zone_output.txt' 
with open(output_file, 'w') as f:
    f.write(f"Total Records: {total}\n")
    f.write(f"Unique Boroughs: {borough}\n")
    f.write(f"Records for Brooklyn: {brooks}\n")

print(f"Data saved to {output_file}")
