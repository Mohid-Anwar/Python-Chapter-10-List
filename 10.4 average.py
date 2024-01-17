user_input = input("Input scores sepererated by space: ")
scores_lst = [eval(score) for score in user_input.split()]

avg = sum(scores_lst) / len(scores_lst)

below_avg = [score_loop for score_loop in scores_lst if score_loop < avg]
aboveorequal_avg = [score for score in scores_lst if score >= avg]

print('The total scores are ', len(scores_lst))
print('The no of scores abv avg is ', len(aboveorequal_avg))
print('The no of scores below avg is ', len(below_avg))
