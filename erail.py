import requests
import json

print("Station code : ")
source_code = input()

print("destination code : ")
dest_code = input()

print("dd-mm : ")
date = input()

print("Enter Class ( plz enter in capital letters ) : ")
level = input()

print("Enter your quota : ")
quota = input()

api_key = "sgley8808"

url="http://api.railwayapi.com/between/source/"+source_code +"/dest/"+dest_code+"/date/"+date+"/apikey/"+api_key+"/"

r = requests.get(url=url)
res = r.json()

Name = []
Number = []
Arr_time = []
Dep_time = []
classes = []
class_level = []
seat_availability = []

j = len(res['train'])
i=0
ticket="Sorry No Info Available at this time"
for i in range (0,j):
    Name.append(res['train'][i]['name'])
    Number.append(res['train'][i]['number'])
    Arr_time.append(res['train'][i]['dest_arrival_time'])
    Dep_time.append(res['train'][i]['src_departure_time'])
    classes.append(res['train'][i]['classes'])

for i in range (0,j):
    url2="http://api.railwayapi.com/check_seat/train/"+Number[i]+"/source/" +source_code+ "/dest/" +dest_code+"/date/"+date+"-2016/class/"+level+"/quota/"+quota+"/apikey/"+api_key+"/"
    r=requests.get(url=url2)
    result=r.json()  
    try:
        seat_availability.append(result['availability'][0]['status'])
    except:
        seat_availability.append(ticket)


for i in range (0,j):
    print("Date of journey : " + date+"-2016") 
    print("train name : " + Name[i])
    print("train number : " + Number[i])
    print("arrival time : " + Arr_time[i])
    print("Departure time : " + Dep_time[i])
    print("Seat Availability : " + seat_availability[i])
    print("\n")
             