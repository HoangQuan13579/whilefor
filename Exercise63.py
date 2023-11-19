c=0
print(str("Celsius").ljust(10),end="")
print("Fahrenheit")
while c<=100:
    print(str(c).ljust(10),end="")
    f=1.8*c+32
    print(f)
    c=c+10