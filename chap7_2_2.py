import sympy

print(sympy.isprime(5))
counter = 0
lists = []

"""for item in range(1, 100):
    if sympy.isprime(item) is True:
        counter += 1
        lists.append(item)

print("100 ~ 1000 소수 갯수{}".format(counter))"""
# print("소수 리스트", lists)
print(list(sympy.primerange(1, 100)))
print(len(list(sympy.primerange(1, 100))))