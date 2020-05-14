import random

hanguls = list("민경수진욱상은채섭철건예")

with open("./data/result.txt", "w") as f:
    f.write("{}, {}, {}\n".format("이름", "몸무게", "키"))

    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(150, 200)

        f.write("{}, {}, {}\n".format(name, weight, height))

print("파일생성이 완료되었습니다")