print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


real_tip= bill * tip /100

total_bill = real_tip + bill

how_pay = round(total_bill/ people ,2)

print (f" you will pay {how_pay}")
