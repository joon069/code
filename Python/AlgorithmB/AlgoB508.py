def palindrome(a):
    front = 0
    back = len(a)-1

    while front < back:
        if not a[front].isalpha():
            front += 1
        elif not a[back].isalpha():
            back -= 1

        elif a[front].lower() != a[back].lower():
            return False
        else:
            front += 1
            back -= 1
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))