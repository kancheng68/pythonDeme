from logging import exception

try:
    from collections.abc import Iterable  # 优先尝试新路径
except ImportError:
    from collections import Iterable  # 回退到旧路径:ml-citation{ref="2,4" data="citationList"}

list1 = {'a': 1, 'v': 'pppp'}
print(isinstance(list1, (int, float, str)))
Iterator1 = iter(list1)
print(next(Iterator1))


class num_iterable(object):
    def __init__(self, number):
        self.num = number

    def __iter__(self): #这是创建迭代器的函数，不现实__next__的时候，可以直接通过这种方法构建一个生成器
        while self.num < 10:
            self.num += 1
            # if (self.num >= 10):
            #     raise StopIteration()  #生成器不需要也不能这样抛出停止异常
            yield self.num
         # return self #当实现了__next__的时候返回的就是一个合法迭代器

    # def __next__(self): #这是迭代器向下next的函数
    #     self.num += 1
    #     if (self.num >= 10):
    #         raise StopIteration()
    #     return self.num


n1= num_iterable(3)
print(n1)
#print(next(n1),'num_iterable(3) 手动next')
print(n1,'num_iterable(3)是一个可迭代类')
for i in n1:
    print(i,' num_iterable(3)生成器产出')
# 列表推导式
list2 = [i ** 2 for i in range(10)]
# 生成器推导式
generator1 = (i ** 2 for i in range(10))
# 生成器函数 所有yield返回的函数都是生成器函数
def test(rangenum):
    for i in range(1,rangenum):
        yield i

print(list2)
print(next(generator1))
print(next(generator1))

print(test(10))
#如果直接调用生成器函数，将每次重新指向第一次结果
print(next(test(10)))
print(next(test(10)))
print(next(test(10)))

print('-----------------------')
#用变量保存后，每一次都是同一词生成器函数对象，则会每次向下生成
tt=test(10)
print(next(tt))
print(next(tt))
print(next(tt))


# for i in test(10):
#     print(i)
