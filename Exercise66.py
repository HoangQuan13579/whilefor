total=0
count=0
while (True):
    n=input("Enter the arbitrary number (or blank line to finish):")
    if n=="A":
        total += 4
        count += 1
    elif n=="B+":
        total += 3.5
        count += 1
    elif n== "B":
        total += 3
        count += 1
    elif n== "C+":
        total += 2.5
        count += 1
    elif n== "C":
        total += 2
        count += 1
    elif n== "D+":
        total += 1.5
        count +=1
    elif n== "D":
        total += 1
        count +=1
    elif n== "F+":
        total += 0.5
        count += 1
    elif n=="F":
        total += 0
        count +=1
    elif n==" ":
        break
    else:
        print("Invalid!!! Please re-enter!!!")
print("The grade point average is:",round(total/count,1))