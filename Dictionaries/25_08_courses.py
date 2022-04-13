def print_courses(courses_dict):
    for courses, students in courses_dict.items():
        print(f"{courses}: {len(students)}")
        for courses_student in students:
            print(f"-- {courses_student}")


command = input()
course_dict = {}

while command != 'end':
    command = command.split(' : ')
    course = command[0]
    student = command[1]

    if course not in course_dict:
        course_dict[course] = list()

    course_dict[course].append(student)
    command = input()

print_courses(course_dict)


