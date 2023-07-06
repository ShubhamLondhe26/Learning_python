print("-"*50)
print("print hello world 3 times :".upper())
count = 0
while (count < 3):
    count = count + 1
    print("hello world")

print("-"*50)
print("Use of break statement inside the loop :".upper())
count = 5
while (count > 0):
    count = count - 1
    if count == 2:
        break
    print(count)
print("loop ended")

print("-"*50)
print("Use of continue statement inside the loop :".upper())
count = 5
while (count > 0):
    count = count - 1
    if count == 2:
        continue
    print(count)
print("loop ended")


