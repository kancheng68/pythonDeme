"""
全局变量的使用和拆包
"""
# pylint:disable=invalid-name

import builtins
from functools import reduce


base_str = "Python Base"


def print_test(something: str):
    """

    :param something:
    :return:
    """
    # base_str="hello world"
    # something += base_str #当内部已经用global定义了外部全局变量时，函数内部不能定义同样名称的局部变量
    global base_str
    base_str += something
    print(base_str)


print_test("12345")
print_test("12345")

str_combine = lambda *str2: [*str2]
print(str_combine("kc", "666"))

# 使用匿名函数作为 sorted() 的 key 参数
names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names, type(sorted_names))  # 输出: ['Bob', 'Alice', 'David', 'Charlie']

print(dir(builtins))

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged)  # 输出: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = [7, 8]
dict1 = {'a': 10, 'b': 11, 'c': 12}

for item in zip(list1, tuple1, set1, dict1.values()):
    print(item)

print(list(zip(list1, tuple1, set1, dict1.values())))

print(list(map(lambda num: num + 1, list1)))

print(reduce(lambda x, y: x + y, list1))

tuple2 = (4, 5, 6)
a, b, c = tuple2
mult1, *mult_remain = tuple2
print(a, b, c)
print(mult1, mult_remain)

dict2 = {'n1': 10, 'n2': 11, 'n3': 12}


def test_dict(n1, n2, n3):
    """

    :param n1:
    :param n2:
    :param n3:
    :return:
    """
    print(n1, n2, n3)


test_dict(**dict2)
