string = input("Enter a String to check Palindrome: ").replace(" ", "").lower()
is_palindrome = True
i, j = 0, len(string) - 1

while i < j:
    if string[i] != string[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("String is Palindrome.")
else:
    print("String is not Palindrome.")