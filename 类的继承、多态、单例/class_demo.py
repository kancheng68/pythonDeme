"""
练习类的继承、多态、单例模式
"""
class GenderFather(object):
    def drive(self):
        print('开车')
    @staticmethod
    def color_detail():
        print('是黄种人')

class Father(GenderFather):
    """
    父类示例
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def fix_machine(self):
        """
        修理方法
        :return:
        """
        print('修好了')

class Son(Father):
    # pass
    def __init__(self, name, age):
        super().__init__(name, age)
    def fix_machine(self):
        super().fix_machine()
        print('改进更好了')
        super().drive()

xiaoming = Son('xiaoming', 18)
xiaoming.fix_machine()
Son.color_detail()
xiaoming.color_detail()
print(Son.__mro__)



class Person:
    """
    人类类型
    """
    def __init__(self, name, age=None):
        print('self: ',self)
        self.name = name
        self.age = age  # 新增 age 属性
    def __call__(self, *args, **kwargs):
        print('让类对象可以被调用，且执行这个函数',f'年龄:{self.age} ')
    height = 190
    @classmethod
    def from_birth_year(cls, name, birth_year):
        print('cls: ',cls)
        return cls(name, 2024 - birth_year)  # 将 age 传入构造函数

# 调用示例
p1 = Person.from_birth_year("Alice", 1990)
p1.height=192
print(p1.name, p1.age)  # 输出: Alice 34
print(Person.height,p1.height)


class Animal(object):
    all_life=None
    def __init__(self, name, age):
        if not hasattr(self, 'has_init'):
            self.has_init=True
            self.name = name
            self.age = age
            print('执行init')

    def __new__(cls, *args, **kwargs):
        if not cls.all_life:
            cls.all_life = super().__new__(cls)
        print('执行new方法')
        return cls.all_life  # 3. 返回初始化后的实例

anm=Animal("xiong mao", 18)
anm1=Animal("chang jin lu", 5)
print(id(anm),id(anm1))
anm.name='niao'
print(anm.name,anm1.name)
