# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고" , "설탕", "메타주아황산나트륨", "치자황색소"],
    "origin" : "Philippines"
}

value = dictionary.get("price")
# 여러작업이 존재
print("값:", value)

if value == None:
    print("에러났습니다")

for key in dictionary:
    # 출력
    atom = dictionary.get(key)
    if type(atom) is list:
        for item in atom:
            print("list 값 :", item)
    else:
        print("값 : ", atom)
    