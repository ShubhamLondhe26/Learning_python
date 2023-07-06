#for i in range(5,35,5):
    #print(i)

#break

for i in range(5,35,5):
    if(i==25):
        break
    print(i)

for i in range(5,35,5):
    if(i==25):
        continue
    print(i)

count=0
while(count<40):
    print(count)
    count=count+5

#break
count=0
while(count<40):
    count=count+5
    if(count==25):
        break
    print(count)

#continue
count=0
while(count<40):
    count=count+5
    if(count==25):
        continue
    print(count)





