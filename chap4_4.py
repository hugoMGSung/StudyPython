# numbers = [1, 2, 3, 4, 5, 6]

# for i in reversed(numbers):
#     print("첫번째 반복문 {}".format(i))

# for i in reversed(numbers):
#     print("두번째 반복문 {}".format(i))

example_list = ["itemA", "itemB", "itemC", "itemD"]

# 단순출력
print(example_list)
print()

# enumerate() 출력
print(enumerate(example_list))
print()

# enumerate() list 출력
print(list(enumerate(example_list)))
print()

# 반복문 조합
for i, value in enumerate(example_list):
    print("{}번째 요소는 {} ".format(i, value))

print()
example_dict = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
    "키D" : "값D",
}

# 딕셔너리 아이템 함수
print(example_dict.items())

for key, element in example_dict.items():
    print("dictionary[{}] = {}".format(key, element))

print()