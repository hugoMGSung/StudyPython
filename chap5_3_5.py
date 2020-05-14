lists = []

with open("./data/result.txt", "r") as f:
    for line in f:
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue

        bmi = (int(weight) / (int(height) * int(height))) * 10000
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"
        
        lists.append([name, weight, height, bmi, result])
        # print('\n'.join([
        #     "이름 : {}",
        #     "몸무게 : {}",
        #     "키 : {}",
        #     "BMI : {}",
        #     "결과 : {}"
        # ]).format(name, weight, height, bmi, result))
        # print()

with open("./data/outputs.txt", "w") as f:
    f.write("{}, {}, {}, {}, {}\n".format("이름", "몸무게", "키", "BMI", "결과"))

    for item in lists:        
        f.write("{}, {}, {}, {}, {}\n".format(item[0],item[1],item[2],item[3],item[4]))

print("파일생성이 완료되었습니다")