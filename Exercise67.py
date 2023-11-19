#67
total=0
while (True):
        age=input("The age of the guest:")
        if age==" ": break
        elif int(age) <=2:
            total += 0
        elif int(age) <=12:
            total += 14
        elif int(age) >= 65:
            total += 18
        elif int(age)> 12 and int(age)<65:
            total += 23
        else: print ("Invalid age entered!!!")
print("The total admission cost is: $",total,".00",sep="")

    