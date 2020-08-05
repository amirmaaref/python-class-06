from pprint import pprint
import json

with open('students.txt', 'rt') as student_file:
    raw_students_string = student_file.read()
raw_student_list = raw_students_string.split('\n')

student_dict = {}
for raw_student in raw_student_list:
    name, family, year, lessions = raw_student.split(':')
    lessions = lessions.split(',')
    sum_of_grades = 0
    sum_of_indexes = 0
    new_student = {
        'name': name,
        'family': family,
        'year': year,
    }
    new_student['lessions'] = []
    for lession in lessions:
        lession_name, lession_grade, lession_index = lession.split(';')
        lession_grade = float(lession_grade)
        lession_index = int(lession_index)
        sum_of_indexes += lession_index
        sum_of_grades += (lession_grade * lession_index)
        lession_dict = {}
        if lession_grade>=10:
            lession_dict['status'] = True
        else:
            lession_dict['status'] = False
        lession_dict['name'] = lession_name
        lession_dict['indexes'] = lession_index
        new_student['lessions'].append(lession_dict)
    average = round(sum_of_grades / sum_of_indexes, 2)
    new_student['average'] = average
    new_student['all_index'] = sum_of_indexes

    if average >= 14:
        student_dict[family] = new_student
# pprint(student_dict)

with open('student-report.json', 'wt') as student_report_file:
    report_to_write = json.dumps(student_dict)
    student_report_file.write(report_to_write)
