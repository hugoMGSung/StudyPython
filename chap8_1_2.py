class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format( \
            self.name, \
            self.get_sum(), \
            self.get_avg())

    

students = [
    Student("윤인성", 88, 87, 95, 88),
    Student("연하진", 88, 87, 95, 88),
    Student("구지연", 88, 87, 95, 100),
    Student("나선주", 88, 87, 90, 88),
    Student("윤아린", 88, 99, 95, 88),
    Student("윤명월", 88, 87, 95, 88)
]

print("이름", "총점", "평균", sep='\t')
for student in students:
    print(str(student))