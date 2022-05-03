print("Welcome to the tip calculator!\n")
total = float(input("What was the total bill? "))
tip = (int(input("How much tip would you like to give? 10, 12 or 15? "))/100) +1
number_of_people = int(input("How many people to split the bill? "))
share = float(total*tip/number_of_people)
print(f"Each person should pay: {round(share,2)}")
