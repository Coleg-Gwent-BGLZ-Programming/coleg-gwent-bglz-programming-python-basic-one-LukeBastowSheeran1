name = input("Please input your name!")
while True:
  age = input("Please input your age!")
  try: 
    age = int(age)
    break
  except ValueError:
    print("Please input numerical values")
hobbies = {input("Please input your first hobby"), input("Please input your second hobby"), input("Please input your third hobby")}
userData = {
  "Name": name,
  "Age": age,
  "Hobbies": hobbies}
def returnString(inputtedData):
    print(f"Name: {inputtedData["Name"]}\nAge: {inputtedData["Age"]}\nHobbies:{inputtedData["Hobbies"]}")
returnString(userData)
