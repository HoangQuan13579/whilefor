pi=3
n=int(input("In ra bao nhieu gia tri xap xi pi?: "))
for i in range (2, (2*(n+1)),2):
    if i%41!=0:
        pi+=4/(i*(i+1)*(i+2))
        print(pi)
    elif i%4==0:
        pi-=4/(i*(i+1)*(i+2))
        print(pi)