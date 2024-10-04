## input we need from user
# total rent
# total food ordered for snacking
# electricity units spend
# charge per units
# persons living in room

## outputrent
# total amount you have to pay is

class ToalRent:
    def total_bill(self, rent, food, electricity_spend, charge_per_unit, persons):
        electric_bill = electricity_spend * charge_per_unit
        total_amount = (rent + food + electric_bill)/persons
        return total_amount

rent = int(input("Enter you room rent= "))
food = int(input("Enter the amount of food ordered= "))
electricity_spend = int(input("Enter the total of electricity spend in unit= "))
charge_per_unit = int(input("Enter the charge per unit= "))
persons = int(input("Enter the number of persons living in room= "))

total_rent_is = ToalRent()
bill = total_rent_is.total_bill(rent, food, electricity_spend, charge_per_unit, persons)
print("Each person will pay = ", bill)

"""
--- input from user ---
Enter you room rent= 5000
Enter the amount of food ordered= 2000
Enter the total of electricity spend in unit= 300
Enter the charge per unit= 12
Enter the number of persons living in room= 5

--- output ---
Each person will pay =  2120.0

"""