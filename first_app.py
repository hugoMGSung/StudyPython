# 압축의 개념
# 압축하기와 압축풀기

data = "66666ttttaaaaddddzzzzzzzzQQQQ7777777"
encoded = ''
planed = ''

count = 1
for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        count += 1
    else:
        encoded += data[i - 1] + str(count)
        count = 1

    if i == len(data) - 1:
        encoded += data[i] + str(count)

print(encoded)

for j in range(0, len(encoded), 2):
    planed += encoded[j] * int(encoded[j + 1])
    j += 2

print(planed)