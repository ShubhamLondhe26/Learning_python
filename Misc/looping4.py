#for loop using break and continue
x = "python is high-level programming language"
for letter in x :
    if (letter == "e" or letter == "i"):
        break
    print(letter,end ="")
print()
print("-"*50)
x = "python is high-level programming language"
for letter in x :
    if (letter == "e" or letter == "i"):
        continue
    print(letter,end = '  ')
    
