#80
import random
def simulate_coin_flips():
    consecutive_count = 0
    flip_count = 0
    last_flip = None
    while consecutive_count < 3:
        flip_result = random.choice(['H', 'T'])
        print(flip_result, end=" ")
        flip_count += 1
        if flip_result == last_flip:
            consecutive_count += 1
        else:
            consecutive_count = 1
        last_flip = flip_result
    print(f"\nNumber of flips needed: {flip_count}")
    return flip_count
total_flips = 0
for i in range(10):
    total_flips += simulate_coin_flips()
average_flips = total_flips / 10
print(f"Average number of flips needed: {average_flips}")