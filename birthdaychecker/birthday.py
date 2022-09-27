import datetime

#birthday = input("When is your birthday in DD/MM/YYYY? ")
current_date = datetime.date.today()
today = current_date.strftime("%d/%m/%Y")
print(today)
#age = today - int(birthday)
#print(f"You are {age} years old")