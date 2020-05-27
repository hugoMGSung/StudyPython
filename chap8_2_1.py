class Student:
    count = 0
    __radius = 0    

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        #self.__temp

        Student.count += 1

    @property
    def radius(self):
        return self.__radius    
    
    @radius.setter
    def radius(self, value):
        # if value <= 0:
        #     raise TypeError("양수")
        self.__radius = value

    def __del__(self):
        pass

    @classmethod
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format( \
            self.name, \
            self.get_sum(), \
            self.get_avg())

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

students = [
    Student("윤인성", 88, 87, 95, 88),
    Student("연하진", 88, 87, 95, 88),
    Student("구지연", 88, 87, 95, 100),
    Student("나선주", 88, 87, 90, 88),
    Student("윤아린", 88, 99, 95, 88),
    Student("윤명월", 88, 87, 95, 88),
    Student("홍길동", 100, 100, 100, 100),
]
#print('Student 클래스 인스턴스여부 :', isinstance(std, Student))
std = Student("홍길동", 100, 100, 100, 100)
std.radius = 100
print(std.radius)

print('생성한 학생수', Student.count)