"""
递归函数
"""


def addsum(num: float):
    """
    用递归实现累加指定数字合
    :param num:
    :return:
    """
    num -= 1
    if num <= 0:
        return num
    return round(num + addsum(num - 1), 2)


totalNum = addsum(100.00)
print(totalNum)  # 输出6.56


def simplesum(num: float):
    """
    用for循环实现累加指定数字合
    :param num:
    :return:
    """
    tem = 0
    for i in range(1, int(num) + 1):
        tem += i
    return round(tem, 2)


print(simplesum(100))


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[n - 2] + fib_list[n - 3])
        return fib_list


print(fibonacci(10))


def fibonacci_simple(n):
    last_list = []
    if n <= 2:
        if n <= 0:
            last_list = []
        elif n == 1:
            last_list = [1]
        elif n == 2:
            last_list = [1, 1]
    else:
        last_list = [1, 1]
        for i in range(2, n):
            last_list.append(last_list[i - 1] + last_list[i - 2])
    return last_list


print(fibonacci_simple(3))


def add_one(func):
    """
    让数字加一
    :param func:
    :return:
    """

    def inner(num):
        tem = func(num)
        return str(tem) + "元"

    return inner


@add_one
def sq(num):
    return num ** 2


print(sq(3), "平方")


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(3, 5))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __testsl(self):
        print(123)
    def talk(self):
        print(f"我叫{self.name}今年{self.age}岁")
        self.__testsl()
    def __del__(self):
        print(f"执行了清除方法")

xiaoming=person("xiaoming", 18)
xiaoming.talk()