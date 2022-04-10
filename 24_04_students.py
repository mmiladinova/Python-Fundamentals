info = input()
courses = dict()

while ":" in info:
    info = info.split(":")
    name = info[0]
    student_id = info[1]
    course = info[2]

    if course not in courses:
        courses[course] = dict()

    courses[course][student_id] = name
    info = input()

search_course = " ".join(info.split("_"))

for key, value in courses.items():
    if key == search_course:
        for st_id, name in value.items():
            print(f"{name} - {st_id}")
