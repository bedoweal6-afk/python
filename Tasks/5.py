def add(c,d):
    return c+d
result =add(5,5)
print(result)
def square (num):
    return num*2
result =square(6)
print(result)
def add_all(*args):
    return sum(args)
print(add_all(1,2,3,4,5))
def factorial(n):
    if n==1:
        return 1
    return n *n-1
print(factorial(7))