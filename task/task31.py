#1.wap to check the greater number taken from user 

num = int(input("Enter the number: "))
max_digit = 0

while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num = num // 10

print("The greatest digit is:", max_digit)



