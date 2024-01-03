#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("The Most Advanced AI Enabled Tip Calculator\n")
bill = float(input("What's the total bill\n$"))
number_of_friends = float(input("\nHow many people are in your group?\n"))
tip = float(input("\nHow much tip do you want to give in Percent, 12, 30, 2? \n"))

bill_for_each = (bill/number_of_friends) * (tip/100 +1)
rounded_bill = round(bill_for_each,2)
formatted_bill = "{:.2f}".format(rounded_bill)
print(f"\nEach person should pay ${formatted_bill}")