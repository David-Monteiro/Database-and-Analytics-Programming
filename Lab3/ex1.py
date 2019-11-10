###Exercise 1


def mul_by_num(num):
    return lambda a: a * num

x = mul_by_num(5)
y = mul_by_num(2)

print(x(3))
print(y(-4))
