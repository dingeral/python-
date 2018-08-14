#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:12:54 2018

@author: wxy
"""

import turtle
turtle.pencolor('gold')
turtle.pensize(4)
turtle.pu()
turtle.goto(0, -140)
turtle.pd()
turtle.circle(140)
turtle.pu()
turtle.goto(-30, 20)
turtle.seth(90)
turtle.pd()
turtle.circle(35, 180)
turtle.pu()
turtle.goto(100, 20)
turtle.seth(90)
turtle.pd()
turtle.circle(35,180)
turtle.pu()
turtle.goto(-55, -25)
turtle.pd()
turtle.seth(270)
turtle.circle(55, 180)
turtle.hideturtle()
turtle.done()