#-*-coding:utf-8-*-
from random import *
import time


def one():
	s = 0
	a = randint(0, 100)
	print("{:-^22}".format("猜数字游戏"))
	print("请输入一个0～100之间的整数：", end="")

	while True:

		if s > 0:
			print("再输一次：",end="")
		nb = input("")
		s += 1
		
		if nb.isnumeric():
			n = eval(nb)
			if n not in range(0,101):
				print("{:-^22}".format("注意范围!"))
			elif n > a: 
				print("很遗憾，太大了！")
			elif n < a:
				print("很遗憾，太小了！")
			elif n == a:
				print("-恭喜你猜中了！共猜测了{}次。-".format(s))
				break
			else:
				print("你输入的是什么鬼？")
		else:
			print("你输入的是什么鬼？")

def onemore():
	one()

	while True:
		print("再来一次？y or n: ", end="")
		sr = input()

		if  sr in ["y", "Y"]:
			onemore()
			break
		elif sr in ["n", "N"]:
			print("正在退出...")
			break
		else:
			print("{:-^22}".format("输入错误！"))

onemore()
time.sleep(0.6)
