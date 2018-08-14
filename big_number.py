#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 求最大公约数


def gys(x, y):
	if y == 0:
		return x
	else:
		return gys(y, x%y)

x = eval(input("请输入第一个数："))
y = eval(input("请输入第二个数："))

z = gys(x, y)
w = x * y / z
print("{}和{}的最大公约数是：{}。".format(x, y, z))
print("{}和{}的最小公倍数是：{:.0f}。".format(x, y, w))
