
# take total bill from user in pkr
total_bill = float(input("Enter the total bill amount in PKR: "))
#take tip percentage from user in pkr
tip_percentage=float(input("Enter tip_percentage: "))
total_people = int(input("Enter total people in number: "))
if total_bill <= 0 or tip_percentage<0 or total_people <= 0 :
  print("invalid.Total bill and Total people must be greater than 0")
else:
  tip_amount=(tip_percentage / 100) * total_bill
  total_bill += tip_amount
#calculate each person's share
each_person_share = (total_bill/total_people)
print("Total bill with tip: PKR", round(total_bill, 2))
print("Each person should pay PKR:", round(each_person_share, 2))
