import datetime
import math

birthday = input("When is your birthday in DD/MM/YYYY? ")
today = datetime.datetime.now()
converted_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")

ageIndays = (today - converted_birthday).days
age = math.floor(ageIndays/365)
print(f"You are {age} years old")