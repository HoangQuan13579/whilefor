#78
decimal=int(input("Decimal:"))
binary=""
print("Binary:",end="")
while decimal>0:
    binary=str(decimal%2)+binary
    decimal=decimal//2
print(binary)
    