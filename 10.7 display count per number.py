from random import randint

counts = [0] * 10
input_lst = [randint(0, 9) for i in range(10)]

for num in input_lst:

    counts[num] += 1

for i in range(10):
    print(f"{i}'s: {counts[i]} ")
print(f"The {len(input_lst)} numbers given were",input_lst)
