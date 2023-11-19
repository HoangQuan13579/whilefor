n=int(input())
i=0
S=0
while n!=0:
    S=S+n
    i=i+1
    n=int(input())
if i!=0:
    A=S/i
    print("Average=",A)
if n==0 and i==0:
    print("Error")