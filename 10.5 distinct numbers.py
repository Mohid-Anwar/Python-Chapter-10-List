user_input = input("Input scores sepererated by space: ")
scores_lst = [eval(score) for score in user_input.split()]
print_lst=[]
for i in range(len(scores_lst)):
    if scores_lst[i] not in print_lst:
        print_lst.append(scores_lst[i])
print(print_lst)
