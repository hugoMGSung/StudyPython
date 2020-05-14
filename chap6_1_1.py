# # try except 연습

lists = [52, 273, 32, 72, 100]

try:
    inputs = int(input("정수 입력 > "))      

    # print("원의 반지름 : ", radius)
    # print("원의 둘레 : ", 2 * 3.14159265 * radius)
    # print("원의 넓이 : ", 3.14159265 * radius * radius) 
    print("{}번째 요소 :값 {}".format(inputs, lists[inputs]))
    예외.발생해주세요()
except ValueError as ex:
    print(ex)
    print("제발 쫌!! 정수를 입력하세요")
except IndexError as ex:
    print("인덱스가 벗어났습니다. 작은수를 넣으세요")   
# except NameError as ex:
#     print("정말이상한 에러가 났습니다")  
except Exception as ex:
    print(ex)
    print("뭔 에러를 내는 겁니까? 퇴사하세요~!!")
# else:
#     print("에러가 발생하지 않았습니다")
# finally:
#     print("프로그램 종료")    

# lists = ['11', '22', '33', '44', '하이', '55']
# outputs = []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#     except:
#         pass
    
# print(outputs)

# f = open("./data/basic.txt", "r")

# try:     
#     f.write("TEST!!")  
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# print("파일 클로즈?", f.closed)

# def test():
#     print("test() start")
#     try:
#         print("test() try")
#         return
#         print("test() after return")
#     except:
#         print("test() except")
#     else:
#         print("test() else")
#     finally:
#         print("test() finally")

#     print("test() end")

# test()