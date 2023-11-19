string = input("Enter a String: ").replace(" ", "")
string = string.lower()
is_palindrome = True
i = 0
j = len(string) - 1
while i < j:
    if string[i] != string[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print(f'"{string}" is a String a Palindrome.')
else:
    print(f'"{string}" is not a String a Palindrome.')