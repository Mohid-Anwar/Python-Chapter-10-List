user_input = input("Input scores sepererated by space: ")
lst = [eval(score) for score in user_input.split()]
min_index = 0
min_value= min(lst)
for i in range(len(lst)):
    if lst[i] == min_value:
        min_index=i
        break
print(f"The min value is {min_value} at index {min_index}")

