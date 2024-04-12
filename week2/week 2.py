print("-----Task 1-----")
def find_and_print(messages, current_station):
    distances = []


    for message, station in messages.items():
        if station == "Xiaobitan" and current_station == "Qizhang":
            distance = 0.5
        elif station == "Xiaobitan" and current_station == "Xindian City Hall":
            distance = 1.5
        elif station == "Xiaobitan" and current_station == "Dapinglin":
            distance = 1.5

        else:
            distance = abs((stations.index(current_station)) - (stations.index(station)))
        distances.append(distance)

    min_distance = min(distances)
    min_distance_index = distances.index(min_distance)
    closest_friend = list(messages.keys())[min_distance_index]

    print(closest_friend)






messages={
        "Leslie": "Xiaobitan",
        "Bob": "Ximen",
        "Mary": "Jingmei",
        "Copper": "Taipei Arena",
        "Vivian": "Xindian"

}
stations = ["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing",
                "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall",
                "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin",
                "Qizhang", "Xiaobitan","Xindian City Hall", "Xindian",]



find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall")

print("-----Task 2-----")
consultants=[
{"name":"John", "rate":4.5, "price":1000,"booking":[]},
{"name":"Bob", "rate":3, "price":1200,"booking":[]},
{"name":"Jenny", "rate":3.8, "price":800,"booking":[]}
]

def book(consultants, hour, duration, criteria):
    available_consultant=[]
    for consultant in consultants:
        for booked_hour,booked_duration in consultant["booking"]:
            for time in range(duration):
                if time + hour in range(booked_hour,booked_hour+booked_duration):
                    break
            else:
                continue
            break
        else:
            available_consultant.append(consultant)


    if not available_consultant:
        print("No service")
        return

    if criteria == "price":
        best_consultant = min(available_consultant, key=lambda x: x["price"])

    elif criteria == "rate":
        best_consultant = max(available_consultant, key=lambda x: x["rate"])


    best_consultant["booking"].append((hour, duration))
    print(best_consultant["name"])




book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John
print("-----Task 3-----")



def func(*datas):
    names = []
    for data in datas:
        if len(data) <= 3:
          name= data[1]
          names.append(name)
        else:
           name = data[2]
           names.append(name)

    unique_names = []
    for name in names:
        if names.count(name) == 1:
            unique_names.append(name)

    if unique_names:
        for unique_name in unique_names:
            for data in datas:
                if len(data) <=3 and data[1] == unique_name:
                    print(data)
                elif len(data)>3 and data[2] == unique_name:
                    print(data)
    else:
        print("沒有")



func("彭大牆", "陳王明雅", "吳明")
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")
func("郭宣雅", "夏曼藍波安", "郭宣恆")

print("-----Task 4-----")




def get_number(index):
   if index==0:
       return 0

   elif index % 3==0:
       return get_number(index-1)-1




   else:

       return get_number(index-1)+4




print(get_number(1))
print(get_number(5))
print(get_number(10))
print(get_number(30))

