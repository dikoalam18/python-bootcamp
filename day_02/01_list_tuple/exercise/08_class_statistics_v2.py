student_scores = [98, 75, 100, 86, 100, 3]

# TODO: Print the average score
average_score = sum(student_scores) // len(student_scores)
print()
print(average_score)

# TODO: Print the rankings, highest to lowest
print()
print(sorted(student_scores, reverse=True))
for x in sorted(student_scores, reverse=True):
    print(x)