#76
n=int(input("Enter an integer:"))
if n<2:
    print("Error")
while n>=2:
    for i in range (2,n+1):
        if n%i==0:
            print(i)
            n=n//i
            break
        