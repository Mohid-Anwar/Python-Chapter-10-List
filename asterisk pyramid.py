def a():
    for i in range(1, 6):
        print("*" * i)


def b():
    for j in range(6, 0, -1):
        print("*" * j)


def c():
    l = 6
    for k in range(l):
        print(" " * k, end="")
        print("*" * l)
        l -= 1


def e():
    j = 0
    for i in range(6, -1, -1):
        print(" " * i, end="")
        print("*" * j)
        j += 1


def f():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def g():
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


g()
