# 마지막 테스트 파이썬
import json

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)


# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기

print(dic_mcu)

# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기
