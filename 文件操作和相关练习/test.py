import os
import sys
import time
import random

if sys.platform.startswith('win'):
    os_type = 'Windows'
elif sys.platform.startswith('linux'):
    os_type = 'Linux'
elif sys.platform == 'darwin':
    os_type = 'macOS'#ml-citation{ref="4,6" data="citationList"}

print(os.path.exists(r'C:\development\project\python\pythonDeme\document\子文件夹/'))
print(os.path.exists(r'document\子文件夹/')) #非绝对路径一律返回False
print(os.path.abspath(r'testfile.txt'))
print(os.path.abspath(r'phone_regex_test.py'))

t1=time.time()
t2=time.localtime()
t1_trans=time.ctime(t1) #把时间戳转化为格式时间字符串
t2_trans=time.asctime(t2) #把时间元组转换为格式时间字符串
t_normal=time.strftime('%Y-%m-%d %H:%M:%S', t2) #把时间元组转换成带格式的时间字符串
t_stuct=time.strptime(t_normal,'%Y-%m-%d %H:%M:%S') #把带格式的时间字符串转换成时间元组
print(t1_trans)
print(t2_trans)
print(t_normal)
print(t_stuct)
print(time.asctime())

print(random.random(),'随机数0-1')
print(random.uniform(1,10),'随机小数1-10')
print(random.randint(1,10),'随机整数1-10')
print(random.randrange(1,10,2),'随机整数1-10，步值为2')
print(random.choice('abcdefg'),'随机字符')
print(random.sample('abcgfdhghgf',3),'随机3个字符')
