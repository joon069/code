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

#---------------------------------------------------

def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else: return "?"
sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(get_name(sample_info, 105))
print(get_name(sample_info, 777))