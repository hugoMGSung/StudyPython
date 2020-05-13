def print_3_times():
    print("Hello World")
    print("안녕하세요")
    print("구텐 타크")

# 가변매개변수와 충돌로 실행안됨
# def print_n_times(value, n=3):
#     for i in range(n):
#         print(value, end=" ")

# def print_n_times(value):
#     for i in range(10):
#         print(value, end=" ")

def print_n_times(*values, n=3):
    for i in range(n):
        for value in values:
            print(value, end=" ")
        print()

def func(a, b=10, c=20):
    print(a + b + c)

def return_test():
    print("Value A")
    return
    #print("Value B")

def multi_all(start, end):
    output = 1

    for i in range(start, end + 1):
        output *= i
    
    return output

# print_3_times()
#print_n_times("Hello", "World", n=2)
# print_n_times(2, "안녕하세요", "즐거운", "파이썬", "프로그래밍")
#print_n_times("안녕하세요", n=1)
#print_n_times("안녕하세요", "즐거운", "파이썬", "프로그래밍", n=1)

# func(10)
# func(c=100, a=50, b=50) #이렇게 쓰지 맙시다

#value = return_test()
value = None
#print("value 는 {}".format(value))
if (value == None):
    print("value 값이 없습니다")
else:
    print("value 는 {}".format(value))

print("1 to 100", multi_all(1, 100))
print("1 to 1000", multi_all(1, 1000))