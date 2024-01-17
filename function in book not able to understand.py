def main():
    lst = [1, 2, 3, 4, 5]
    s(lst)

    print(lst)
    for value in lst:
        print(value, end=' ')


def s(lst):
    newLst = len(lst) * [0]

    for i in range(len(lst)):
        newLst[i] = lst[len(lst) - 1 - i]

    lst = newLst



main()
