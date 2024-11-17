#rent calculator
#rent expense divide equally
rent = int(input("enter the total rent = "))
food = int(input("enter the total amount of  food rent = "))
electricity_bill = int(input("entre the electricity bill = "))
charge_per_unit = int(input("enter the chagre per unit in your area = "))
number_of_persons = int(input("enter the number of persons = "))
#logical calculations
total_bill = electricity_bill*charge_per_unit
calculator = (rent+food+total_bill)//number_of_persons
#output
print("each person will pay  ", calculator)