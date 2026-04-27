match month := 3:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月可能有28天")
    case _:
        print(f"{month}月有?天")
#Python3.10新增了match case的条件判断方式，match后的对象会依次与case后的内容匹配，匹配成功则执行相应语句，否则跳过。其中_可以匹配一切

print("----------------------------------------------------")

#三目运算符
#表达式1 if 判断条件 else 表达式2
#使用 if 来获取两个数中较大的一个
num1 = 2
num2 = 3
if num1 > num2:
    max_num = num1
else:
    max_num = num2
print(max_num)
#以上代码可以通过三目运算符改写
num1 = 2
num2 = 3
max_num = num1 if num1 > num2 else num2
print(max_num)

print("----------------------------------------------------")

#while 后可以加上 else，当 while 表达式结果为 False 时会执行 else 中的语句。
rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
else:
    print(f"第{week}周有{rabbit}只兔子")
#此时else中代码，写在else中和写在循环外效果一样。else一般和 break一起使用，循环通过break终止后，else中的代码不会执行。
#for 循环后也可以加上 else，循环结束后会执行 else 中语句。

print("----------------------------------------------------")

#通过索引获取列表中元素
list1 = [100, 200, 300, 400, 500]
print(list1[1])  # 200
print(list1[-2])  # 400
#列表切片
list1 = [100, 200, 300, 400, 500]
print(list1)  # 取全部元素
print(list1[:])  # 复制整个列表
print(list1[2:4])  # 取索引从2开始到4(不包含)的元素
print(list1[2:])  # 取索引从2开始到末尾的元素
print(list1[:2])  # 取索引从0开始到2(不包含)的元素
print(list1[2:-1])  # 取索引从2开始到-1(不包含)的元素
print(list1[::-1])  # 倒序取元素
#向列表中添加元素
list1 = [100, 200, 300, 400, 500]
list1.append(600) # 在列表末尾追加元素
list1.insert(2,700) # 在列表指定的位置追加元素
print(list1)
#列表相加
list1 = [100, 200, 300]
list2 = ["a", "b", "c"]
print(list1 + list2)  # [100, 200, 300, 'a', 'b', 'c']
#列表乘法
list1 = [100, 200, 300]
print(list1 * 2)  # [100, 200, 300, 100, 200, 300]
#修改列表中元素
#通过下标修改。
list1 = [100, 200, 300, 400, 500]
list1[0] = -1
print(list1)
#通过切片修改。
list1 = [100, 200, 300, 400, 500]
list1[2:4] = ["a", "b", "c"]
print(list1)
#检查成员是否为列表中元素
list1 = [100, 200, 300]
print(100 in list1)  # True
#获取列表长度
list1 = [100, 200, 300]
print(len(list1))  # 3
#求列表中元素的最大值、最小值、加和
list1 = [100, 200, 300, 400, 500]
print(max(list1))  # 500
print(min(list1))  # 100
print(sum(list1))  # 1500
#遍历列表
#直接遍历列表元素
list1 = [100, 200, 300, 400, 500]
for i in list1:
    print(i)
#通过下标遍历列表
list1 = [100, 200, 300, 400, 500]
for i in range(len(list1)):
    print(i, list1[i])
#使用enumerate()同时获取列表的下标和元素
list1 = [100, 200, 300, 400, 500]
for i, val in enumerate(list1):
    print(i, val)
#删除列表指定位置元素或者切片
list1 = [100, 200, 300, 400, 500]
del list1[2]
print(list1)
#嵌套列表
#列表中元素可以为列表
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for inner_list in list1:
    print(inner_list)

print("----------------------------------------------------")

#如果stop小于或等于 start且step为正数，或者stop大于或等于start且step为负数，range() 函数将生成一个空序列。
#指定生成到stop（不包含stop）的数列，默认从0开始。
for i in range(10):
    print(i)
#指定生成数列的范围，从start到stop（不包含stop），可设定步长，默认步长为1，步长可正可负。
for i in range(-10, 10):
    print(i)

for i in range(10, -10, -3):
    print(i)

print("----------------------------------------------------")

zip() #函数可将多个可迭代对象中对应元素打包为一个个元组。
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
zipped = zip(list1, list2)
print(list(zipped))
