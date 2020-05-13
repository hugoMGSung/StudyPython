
# for i in range(0, 10, 2):
#     print(i, "= 반복변수")

# print()

# array = [11, 22, 33, 44, 55, 66]
# for i in range(len(array)):
#     print(i+1, "번째 array값", array[i])

# print()

# for i in range(10, 0 - 1, -1):
#     print(i)

# while True:
#     print(".", end="")

# i = 0
# while True:
#     print("{}번째 반복".format(i))
#     i += 1

#     #반복 종료
#     input_text = input("> 종료합니까?(y)")
#     if input_text in ["y", "Y"]:
#         print("반복 종료")
#         break

numbers = [5,15,6,60,7,25]

for num in numbers:
    if num < 10:
        continue

    print(num)