import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb+srv://Monica:sh0DUW41YaWVwcJS@cluster1.jczyy.mongodb.net/merng?retryWrites=true&w=majority&appName=Cluster1")
db = client["suturePadsData"]
collection = db["pressureData"]

PRESSURE_THRESHOLD = 1030

pressure_data = pd.read_excel('pressure_data.xlsx', sheet_name=0)
pressureList = list(pressure_data['pressure_values'])

count = 0
highPressure = []
for pressure in pressureList:
    print("Current Pressure:", pressure)
    count += 1

    if pressure > PRESSURE_THRESHOLD:
        print(f"Alert: {pressure} is past the pressure threshold.")
        highPressure.append(pressure)

insert_data = collection.insert_many([{"pressure": pressure} for pressure in highPressure])


