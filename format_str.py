import locale

# print(locale.setlocale(locale.LC_ALL, "ko_KR"))
print(locale.format("%d", 1235000, grouping=True))
# print(format(1235000, ',d'))