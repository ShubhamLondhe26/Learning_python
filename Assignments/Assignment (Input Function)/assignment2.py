#2)Create a tip Calculator:
# User: Please Enter Total Bill (New line) Amount Rs.
# User: How Much % Tips Would You Like To Give? 10 15 or 20?
# User: How Many People To Spilt The Bill

#Expected output:
#Please Enter total Bill
#Amount Rs.4500.45
#How much tips(%) would you like to give?
#10 15 or 20?10
#How many people to split the bill?4
#Each person should pay: Rs.1237.62(Hint use round function)

total_bill=float(input("Please enter total bill Amount: \n"))
tips=float(input("How much tips(%) would you like to give?\n"))
split1=float(input("How many people to split the bill?\n"))

calc=total_bill*tips/100
amount=total_bill+calc
final_amount=amount/split1
print(f"Each person should pay {final_amount}.")