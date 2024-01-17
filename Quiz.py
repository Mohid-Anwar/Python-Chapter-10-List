def reverse(number):
    number = number[::-1]
    return int(number)
a = input(str("Enter number to be reversed"))
b = reverse(a)
print(b)