#1说说函数定义都包含哪些要素
#def关键字
#函数名
#参数列表
#冒号与缩进
#函数体
#返回值

print("***" * 10)

#2什么是形参和实参
#在定义函数时，指定的参数称为形式参数，简称为形参（函数的提供者）
#在调用函数时，给函数传递的参数称为实际参数，简称为实参（函数的调用者）

print("***" * 10)

#字符串String常用函数

#str.replace(old,new[,max])	把将字符串中的old替换成new,如果指定max，则替换不超过max次
# str.split([x][,n])	按x分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数
# str.rsplit([x][,n])	与split()类似，从右边开始分隔
# x.join(seq)	以x作为分隔符，将序列中所有的字符串合并为一个新的字符串
# str.strip([x])	截掉字符串两边的空格或指定字符
# str.lstrip([x])	截掉字符串左边的空格或指定字符
# str.rstrip([x])	截掉字符串右边的空格或指定字符
# str.removeprefix()	截掉字符串指定前缀
# str.removesuffix()	截掉字符串指定后缀
# str.upper()	将所有字符转为大写
# str.lower()	将所有字符转为小写
# str.swapcase()	反转字符串中字母大小写
# str.capitalize()	将字符串第一个字母变为大写，其他字母变为小写
# str.title()	将字符串每个单词首字母大写
# str.casefold()	返回适合无大小写比较的字符串版本
# len(str)	返回字符串长度
# max(str)	返回字符串中最大值
# min(str)	返回字符串中最小值
# str.find(x[,start][,end])	返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
# str.rfind(x[,start][,end])	与find()类似，从右边开始查找
# str.index(x[,start][,end])	返回字符串中第一个x的索引值，不存在则报错，可指定字符串开始结束范围
# str.rindex(x[,start][,end])	与index()类似，从右边开始查找
# str.count(x[,start][,end])	返回字符串中x的个数，可指定字符串开始结束范围
# str.startswith(x[,start][,end])	检查字符串是否以x开头，可指定字符串开始结束范围
# str.endswith(x[,start][,end])	检查字符串是否以x结尾，可指定字符串开始结束范围
# str.isspace()	检查字符串是否非空且只包含空白

print("***" * 10)

#集合常用函数

# set.add(x)	添加元素
# set.update(x)	添加元素，x可以为列表、元组、字符串、字典等可迭代对象
# set.union(x)	添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
# set.remove(x)	从集合中移除x，x不存在则报错
# set.discard(x) 	从集合中移除x，x不存在也不报错
# set.pop()	随机取出集合中的一个元素，如果集合为空则报错
# set.clear()	清空集合
# set.difference(x1,...)	求set1和x1的差集，返回一个新的集合
# set.difference_update(x1,...)	求set1和x1的差集
# set.intersection(x1,...)	求set1和x1的交集，返回一个新的集合
# set.intersection_update(x1,...)	求set1和x1的交集
# set1 & set2	两集合求交集
# set1 | set2	两集合求并集
# set1 - set2	两集合求差集
# set1.isdisjoint(set2)	判断两集合是否没有交集
# set1.issubset(set2)	判断set1是否为set2的子集
# set1.issuperset(set2)	判断set2是否为set1的子集
# set1.symmetric_difference(set2)	求两集合中不重复的元素，返回一个新的集合
# set1.symmetric_difference_update(set2)	求两集合中不重复的元素
# set.copy()	拷贝集合
# len(set)	返回集合元素个数
# max(set)	求集合中元素的最大值
# min(set)	求集合中元素的最小值
# sum(set)	求集合中元素的加和

print("***" * 10)

#字典常用函数

# del dict[key]	根据key删除键值对
# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
# dict.clear()	清空字典
# dict1.update(dict2)	将dict2中的键值对更新到dict1中
# dict.get(key[,default])	获取字典中key对应value，可设置默认值
# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值
# dict.keys()	获取字典所有的key，返回一个视图对象。字典改变，视图也会跟着变化
# dict.values()	获取字典所有的value，返回一个视图对象
# dict.items()	获取字典所有的(key,value)，返回一个视图对象
# dict.copy()	拷贝字典
# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值

print("***" * 10)

#函数定义
# Python 定义函数使用 def 关键字，一般格式如下：
# def 函数名 (参数列表) :
#         函数体
#         [return]






