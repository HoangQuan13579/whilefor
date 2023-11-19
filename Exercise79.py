#79
import random
max = 0
update = 0
for i in range(100):
    new_integer = random.randint(1, 100)
    print(f"New integer: {new_integer}", end=" ")
    if new_integer > max:
        max = new_integer
        update += 1
        print(f"(New max: {max})")
    else:
        print()
print(f"The maximum value encountered is: {max}")
print(f"The maximum value was updated {update} times")