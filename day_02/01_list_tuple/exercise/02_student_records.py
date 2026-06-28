student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)
student_sections = ("Section-I", "Section-II", "Section-III")
# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""

print()
print("Student Records:")
for section, name, score in zip(student_sections, student_names, student_scores):
    print(f"From {section} Student: {name} scored {score} in the exam")
