import random
import itertools

import pandas as pd
import SimulationFunctions as SF

num_tests = 15
num_students_miss_0_tests = 1000
num_students_miss_1_tests = 1000
num_students_miss_2_tests = 1000
num_students_miss_5_tests = 1000
num_students_miss_6_tests = 1000



data = pd.DataFrame()
data['# of tests missed'] = [0,1,2,5,6]

num_semesters = 50

for semester in range(num_semesters):

    students0 = []
    students1 = []
    students2 = []
    students5 = []
    students6 = []

    for student in range(num_students_miss_0_tests):
        test_grades = SF.generate_students_grades()
        test_grades = list(itertools.chain.from_iterable(test_grades))
        students0.append(test_grades)

    for student in range(num_students_miss_1_tests):
        test_grades =  SF.generate_students_grades()
        test_grades = list(itertools.chain.from_iterable(test_grades))
        missed_test =  int(random.triangular(0, 14, 14)) #assume that students who miss 1 test are most likely to skip the last test
        test_grades[missed_test] = 0
        students1.append(test_grades)

    for student in range(num_students_miss_2_tests):
        test_grades = SF.generate_students_grades()
        test_grades = list(itertools.chain.from_iterable(test_grades))
        missed_tests = [random.randint(0, 14) for _ in range(5)]
        for test in missed_tests:
            test_grades[test] = 0
        students2.append(test_grades)

    for student in range(num_students_miss_5_tests):
        test_grades = SF.generate_students_grades()
        test_grades = list(itertools.chain.from_iterable(test_grades))
        missed_tests = [random.randint(0, 14) for _ in range(5)]
        for test in missed_tests:
            test_grades[test] = 0
        students5.append(test_grades)

    for student in range(num_students_miss_5_tests):
        test_grades = SF.generate_students_grades()
        test_grades = list(itertools.chain.from_iterable(test_grades))

        missed_tests = [random.randint(0, 14) for _ in range(5)]
        for test in missed_tests:
            test_grades[test] = 0
        students5.append(test_grades)
        students6.append(test_grades)

    data['Semester '+ str(semester)] = [SF.get_group_average(students0), SF.get_group_average(students1),SF.get_group_average(students2), SF.get_group_average(students5), SF.get_group_average(students6)]



# add an average column  that averages the rows
data['Average'] = data.mean(axis=1)

print(data)