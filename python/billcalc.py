#program Description: Calculates bill

#Asking user forBill Amt

bill=float(input("Enter bill amt:"))

#Asking user for no. of people

people = int(input("Enter no. of people sharing the bill:"))

#Define tax and tip rates

tax_rate=0.0825
tip_rate=0.15

#foroula to calculate tax, tip and total
tax=bill*tax_rate

tip =bill+tax_rate

total=bill+ tax + tip

#Calculate amt each person owes
per_person=total /people

#Printing everything

print ("Restaurant Bill Calculator")
print("___________________________")
print(f"Orginal Bill: {bill}")
print(f"Tip 15% {tip}")
print(f"Tax {tax}")
print(f"here is the total bill {total}")
print(f"Each person share: {per_person}")

