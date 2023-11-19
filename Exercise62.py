a=4.95
print(str("original price".ljust(20)),end="")
print(str("discount amount".ljust(20)),end="")
print(str("new price"))
while a<25:
    print(str(a).ljust(20),end=" ")
    print(str(round(0.6*a,2)).ljust(20),end=" ")
    print(round(0.4*a,2))
    a=a+5
    