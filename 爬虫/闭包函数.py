def func():
    a = 10
    def in_func():
        print(a)

    return in_func

x = func()
print(x)
i = x()
