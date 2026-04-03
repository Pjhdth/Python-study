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

#在程序中定义name、age变量，将你的名字和年龄赋值，并输出到控制台
name = "zhangsan"
age = 22
print("Hello, My name is " + name + "," + str(age) + " years old.")

print("--------------------------------------------------------")

#将十进制数 42 转换为二进制表示
dec_num1 = 42
print(bin(dec_num1))

print("--------------------------------------------------------")

#将二进制数 110110 转换为十进制表示
bin_num2 = 0b110110
print(int(bin_num2))

print("--------------------------------------------------------")

#将二进制数 1101 转换为十六进制表示
bin_num3 = 0b1101
print(hex(bin_num3))

print("--------------------------------------------------------")

#将十六进制数 1A3 转换为二进制表示
hex_num4 = 0x1a3
print(bin(hex_num4))

print("--------------------------------------------------------")

#有十进制数-8，请用八位二进制小数表示的它的原码、反码、补码
#原码：10001000 反码：11110111 补码：11111000

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
