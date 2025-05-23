"""
练习视频中的知识点
"""

import ast


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# pylint: disable=invalid-name


def print_hi(name):
    """
    返回一个问候信息。
    返回:
        name: 问候信息。
    """
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')


print('special string: \', ", \\, \\\\, \\n, \\t')
print(r'''
'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
''')


# 作为变量（推荐）

template = "life is {0}, you need {1}"
print(template.format('short', 'Python'))

template = "life is {s}, you need {p}"  # 明确重新赋值
print(template.format(s='short', p='Python'))

# 作为逻辑常量
TEMPLATE_A = "life is {0}, you need {1}"
TEMPLATE_B = "life is {s}, you need {p}"

# dict1={'aa':1,'bb':2}
#
# for k in dict1:
#     print(dict1[k])


set1 = {1, 2, 3,'a'}

set1.update({2,34,6})
set1.add('1')
print(set1)

dic1={'a','b','c'}

dic2={}
print(set1 and dic1 and dic2)




num = 3.14159
result = float(f"{num:.3f}")
print(isinstance(result,float))

str1="[1,2,3,4]"
print(ast.literal_eval(str1))

t1=(1,2,3,4)
print(t1,type(t1))
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
