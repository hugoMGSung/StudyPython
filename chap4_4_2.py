array = []
# 빈값 리스트 생성

# for문 
for i in range(1, 20, 1):
    array.append(2 ** i)

# 출력
print(list(array))
print()

array2 = [2 ** i for i in range(4, 20)]
print(array2)
print()

# 조건활용리스트
array3 = ["사과", "자두", "초콜릿", "바나나", "체리"]
#output = ["사과", "자두", "바나나", "체리"]
output = [fruit for fruit in array3 if fruit != "초콜릿"]
print(output)
