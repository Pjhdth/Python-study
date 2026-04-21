#单行注释

'''多行
   注释'''

"""多行
   注释"""

print("--------------------------------------------------------")

print("hello world")
print("""hello
world""") #三个引号出现的位置不同，作用也不一样

print("--------------------------------------------------------")

a = 10 #变量赋值
b = "zhangsan"
print(a)
print(b)

b = 20 #改变数据
print(b)

print("--------------------------------------------------------")

# var1 = var2 = var3 = 666
var1 , var2 , var3 = 666 , 777 , 888 #批量赋值

print(var1)
print(var2)
print(var3)

print("--------------------------------------------------------")

num1 = 10
num2 = 20
print(num1, num2)
num1, num2 = num2, num1 #交换数据，涉及元组知识
print(num1, num2)

print("--------------------------------------------------------")

#可以使用 type() 来查看变量类型，使用 isinstance() 来判断变量类型。
#type() 和 isinstance() 的区别在于 type() 不会认为子类是一种父类类型，isinstance() 会认为子类是一种父类类型
num1 = True
num2 = 10
print(type(num1))  # <class 'bool'>
print(type(num2))  # <class 'int'>
print(type(num1) == type(num2))  # False
print(isinstance(num1, bool))  # True
print(isinstance(num1, int))  # True，Python3中，bool是int的子类
print(isinstance(num2, int))  # True
