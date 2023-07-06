#3) Write a program that prints the integers from 1 to 100 and for multiples of “3” print "study" instead of the number and for the multiples of “5” print "well"
#and for numbers that are multiples of both three and five print "study well"
#Output:
#1, 2, study, 4, well, study, 7, 8, study, well, 11, study, 13, 14,
#Study well, 16, 17, …………


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("study well")
    elif num % 3 == 0:
        print("study")
    elif num % 5 == 0:
        print("well")
    else:
        print(num)


