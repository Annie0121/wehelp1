import json
import urllib.request as request
scr = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
scr2='https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'
with request.urlopen(scr) as response:
    data = response.read().decode('utf-8')

with request.urlopen(scr2) as response:
    data2 =response.read().decode('utf-8')


data = json.loads(data)
title = data["data"]["results"]

data2 =json.loads(data2)
titke2 = data2["data"]

with open("spot.csv","w",encoding="utf-8") as file:
    for inf in title:
        spot_title = inf['stitle']
        longitude = inf['longitude']
        latitude = inf['latitude']
        ImageURL = inf["filelist"].split("https")[1]
        for dis in titke2:
            if inf["SERIAL_NO"] == dis["SERIAL_NO"]:
                District =dis["address"].split("區")[0]
                Dis = District.replace("臺北市  ", "")
                #print(Dis + '區')
        file.write(f"{spot_title}, {Dis}區, {longitude}, {latitude}, https{ImageURL}\n")

with open("mrt.csv","w",encoding="utf-8") as file:
    attraction_dict={}
    for dis in titke2:
        StationName = dis["MRT"]
        for inf in title:
            if inf["SERIAL_NO"] == dis["SERIAL_NO"]:
                AttractionTitle=inf["stitle"]
                if StationName in attraction_dict:
                    attraction_dict[StationName].append(AttractionTitle)
                else:
                    attraction_dict[StationName]=[AttractionTitle]

    for station,attraction in attraction_dict.items():
        attractions_str = ", ".join(attraction)
        file.write(f"{station}, {attractions_str}\n")









# 比對兩筆資料
# for inf in title:   #serial=inf["SERIAL_NO"]  serial2 = dis["SERIAL_NO"]
#     for dis in titke2:
#         if inf["SERIAL_NO"] == dis["SERIAL_NO"]:
#             District =dis["address"].split("區")[0]
#             Dis = District.replace("臺北市  ", "")
#             print(Dis + '區')




# #印出行政區
# for dis in titke2:
#     District =dis["address"].split("區")[0]
#     Dis = District.replace("臺北市  ", "")
#     print(Dis+'區')


