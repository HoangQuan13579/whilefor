x=float(input("Enter the number to calculate the square root:"))
guess = x/2
max_iterations = 10
iterations = 0
while iterations < max_iterations:
    guess = 0.5 * (guess + x / guess)
    iterations += 1
print(f"Square root {x} approximately={guess:.1f}")
