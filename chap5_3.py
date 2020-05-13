def test_func():
    return (10, 20)

# a, b = 10, 20
# print("swap 전 ", end="")
# print("a", a, "b", b)

# a, b = b, a
# print("swap 후 ", end="")
# print("a", a, "b", b)

c, d = test_func()
print("c", c, "d", d)
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("Hello World")

call_10_times(print_hello)