"""
练习copy相关的操作
"""
# pylint: disable=invalid-name

import copy
from enum import Enum

# 这里是赋值，所以list1和list2是完全一样
list1 = [1, 2, 3, 4, [6, 7]]
list2 = list1
list1[4][0] = 66
list1[3] = 44
print(list1, list2)
print(id(list1), id(list2))

# 这里是浅拷贝，只有值赋值过去了，地址则是分开
list1_1 = [1, 2, 3, 4, [6, 7]]
list2_1 = copy.copy(list1_1)
list1_1[4][0] = 66
list1_1[3] = 44
print(list1_1, list2_1)
print(id(list1_1), id(list2_1))

# 深拷贝
list1_2 = [1, 2, 3, 4, [6, 7]]
list2_2 = copy.deepcopy(list1_2)
list1_2[4][0] = 66
list1_2[3] = 44
print(list1_2, list2_2)
print(id(list1_2), id(list2_2))


class Color(Enum):
    """
    枚举：颜色
    """
    RED = 0
    GREE = 1
    BLUE = 2


for item in Color:
    print(item.name, item.value)


def print_params(s1: str = "helloWorld"):
    """
    直接打印
    :param s1:
    :return:
    """
    print(s1)


def print_tuples(*args):
    """
    直接打印
    :param args: 
    :return: 
    """
    print(args, id(args))


def print_list(out_list: list):
    """

    :param out_list:
    :return:
    """
    print(out_list, id(out_list))


print_params("123")

arg_str = "123"
print(id(arg_str))
print_tuples(arg_str, 1, 3, 4)

dict1 = {'aa': 'tt'}
if 'aa' in dict1:
    print("yes")


def print_kwargs(**kwargs):
    """

    :param kwargs:
    :return:
    """
    print(kwargs)


print_kwargs(a=1, b=2, c=3)
