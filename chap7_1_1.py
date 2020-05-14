import sys
import os
import datetime
from urllib.request import urlopen

from math import *
import math

# print(sys.argv)
# print(sys.getwindowsversion())
# print(sys.copyright)
# print(sys.version)

# print("OS : ", os.name)
# print("폴더 : ", os.getcwd())
# print("files : ", os.listdir())

#os.mkdir("hello")
#os.rmdir("hello")
#os.system("tree")
# current = datetime.datetime.now()
# print("{}년 {}월 {}일 {}시 {}분 {}초 {}ms".format(
#     current.year,
#     current.month,
#     current.day,
#     current.hour,
#     current.minute,
#     current.second,
#     current.microsecond
# ))

#target = request.urlopen("https://www.google.com")

try:
    target = urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
except Exception as ex:
    print(ex)

# output = target.read()
# print(output)
#status = target.getheaders()

#for item in status:
#    print(item)
print(target.status)
