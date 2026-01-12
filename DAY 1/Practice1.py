name = input("Enter your name: ")

city = input("Enter your city: ")
state = input("Enter your state: ")
house = input("Enter your house: ")
road = input("Enter your road: ")

phone_number = input("Enter your phone number: ")

day, month, year = map(int, input("Enter your DOB (day month year): ").split())

university = input("Enter your university: ")
department = input("Enter your department: ")

print("\nHere are your details:")
print(f"Name: {name}")
print(f"Address: House {house}, Road {road}, {city}, {state}")
print(f"Phone Number: {phone_number}")
print(f"Date of Birth: {day}/{month}/{year}")
print(f"University: {university}")
print(f"Department: {department}")
