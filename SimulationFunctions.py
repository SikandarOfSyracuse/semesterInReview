import random
import Utils

def generate_test_grade(mean, std_dev, num_grades):
    grades = []
    for grade in range(num_grades):
        grade = random.gauss(mean, std_dev)
        if grade > 100:
            grade = 100
        grade = Utils.truncate_float(grade, 2)
        grades.append(grade)
    return grades

def generate_students_grades():
    # I assume that the early tests have higher grades than the later tests
    test_grades = []
    test_grades.append(generate_test_grade(90,5,5))
    test_grades.append(generate_test_grade(80,5,5))
    test_grades.append(generate_test_grade(70,5,5))
    return test_grades

def get_group_average(students):
    group_average = 0
    for student_ in students:
        student_ = Utils.remove_lowest_values(student_,5)
        student_average = sum(student_) / len(student_)
        group_average += student_average
    group_average = group_average / len(students)
    return group_average