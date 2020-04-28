import requests
import sys

activities_url = "https://www.strava.com/api/v3/athlete/activities?access_token="
header = {"Authorization": "Bearer " + "97e07e316cbc1ebea1a351daf96999af1ad86059"}
param = {"per page": 200, "page": 1}
my_dataset = requests.get(activities_url, headers=header, params=param).json

print(sys.executable)
print(my_dataset)

name = input("your name?")
print("Hello", name)
