def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student.get("korean") + student.get("math") + \
        student.get("english") + student.get("science")

def student_get_avg(student):
    return student_get_sum(student) / 4

def student_toString(student):
    return "{}\t{}\t{}".format( \
        student.get("name"), \
        student_get_sum(student), \
        student_get_avg(student) \
    )

students = [
    create_student("윤인성", 88, 87, 95, 88),
    create_student("연하진", 88, 87, 95, 88),
    create_student("구지연", 88, 87, 95, 100),
    create_student("나선주", 88, 87, 90, 88),
    create_student("윤아린", 88, 99, 95, 88),
    create_student("윤명월", 88, 87, 95, 88),
]

print("이름", "총점", "평균", sep='\t')
for student in students:
    #print("이름:{}, 한국어:{}".format(item.get("name"), item.get("korean")))
    #score_sum = student_get_sum(student)
    #score_avg = student_get_avg(student)
    print(student_toString(student))