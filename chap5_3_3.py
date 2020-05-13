# 파일을 열고
f = open("./data/basic.txt", "w")
# 파일 쓰고
f.write("Hello Python Programming...!!")
# 파일 닫기
f.close()

f1 = open("./data/basic.txt", "a")
f1.write("\nAdded documents")
f1.close()

with open("./data/test.txt", "w") as f3:
    f3.write("\nWith sentence document")

content = "" 

with open("./data/test.txt", "r") as f4:
    content = f4.read()

print(content)