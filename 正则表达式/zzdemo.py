import re

res1=re.match(r'^[a-zA-Z0-9]*@(qq|163).com$','dsa@qq.com')
if res1:
    print('匹配成功')
    print(res1.group())
else:
    print('匹配失败')

res2=re.match(r'^<(\w+)>\w+</\1>$','<html>dsadi</html>')
if res2:
    print('匹配成功')
    print(res2.group())
else:
    print('匹配失败')

res3=re.findall(r'^(?P<L1>\w+)\|(?P<L2>\d+)、(?P=L1)、(?P=L2)$'
              ,'aa|123、aa、123')
if res3:
    print('匹配成功')
    print(res3)
else:
    print('匹配失败')
    print(res3)

res4=re.sub(r'</?(\w+)>','','<html>innerHTML</html>')
print(res4)


#注： 正则表达式的范围取值后，跟上一个？，代表尽可能少的取值，非贪婪匹配，
# 比如{2,5}匹配2-5次，{2,5}？就是匹配2次

res5=re.match(r'\\',r'<html>inner\\\HTML</html>')
