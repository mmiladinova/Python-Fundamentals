def fill_students(students_num, students_dict):
    for x in range(students_num):
        student = input()
        student_grade = float(input())

        if student not in students_dict:
            students_dict[student] = list()

        students_dict[student].append(student_grade)

    return students_dict


def print_students(students_dict):
    for key, value in students_dict.items():
        grade_sum = 0
        for grade in value:
            grade_sum += grade

        average_grade = grade_sum / len(value)
        if average_grade >= 4.5:
            print(f"{key} -> {average_grade:.2f}")


n = int(input())
students_dictionary = dict()

print_students(fill_students(n, students_dictionary))
