isCovered = [False] * 99

endOfInput = False
while not endOfInput:

    s = input("Enter Line of Numbers separated by spaces: ")
    items = s.split(" ")

    lst = [eval(x) for x in items]

    for number in lst:
        if number == 0:
            endOfInput = True
        else:
            isCovered[number - 1] = True

if False in isCovered:
    print("The ticket doesn't cover all numbers")
else:
    print("The ticket covers all numbers")
    print(isCovered)

