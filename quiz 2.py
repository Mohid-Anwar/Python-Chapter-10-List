lower_case_word = "harry potter"
lower_case_word = lower_case_word.split()

output = ""
for i in range(len(lower_case_word)):
    lower_case_word[i] = lower_case_word[i].title()

output = " ".join(lower_case_word)
print(output)
