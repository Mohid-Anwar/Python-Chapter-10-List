lst = []

print("Enter integers between 1 and 100: ")
for i in range(4):
    integer = int(input())
    lst.append(integer)

o_lst = list(set(lst))
for i in range(len(o_lst)):
    integer = 0
    for j in range(i, len(lst)):
        if lst[j] == o_lst[i]:
            integer += 1
    print(lst[i], " occurs ", integer, "times")
