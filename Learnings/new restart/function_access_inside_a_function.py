def test(a):
        def add(b):
                nonlocal a
                a += 0
                return a+b
        return add
func= test(10)
print(func(10))
