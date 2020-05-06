import sys
import os
import turtle
import random

wn = turtle.Screen()
wn.screensize(400,400)

gi = r"C:\Users\yohei\OneDrive\画像\giphy.gif"
wn.register_shape(gi)

t=turtle.Turtle(gi)
t.penup()
t.goto(-280, -280)
# FIELD_DEFAULT = "square"
# LEVEL_ONE = 1
# LEVEL_TWO = 2
# LEVEL_THREE = 3
# LEVEL_FOUR = 4
# LEVEL_FIVE = 5
#
# wn = turtle.Screen()
# wn.screensize(400,400)
# wn.reset()
# wn.setworldcoordinates(-400,-400,400,400)
# wn.bgcolor("black")
# wn.title("game")
#
# # FIELD = [[f for f in range(4)] for i in range (4)]
# FIELD = []
# FIELD1 = []
# for x in [-3,-1,1,3]:
#     for y in [-3,-1,1,3]:
#         t=''
#         t=turtle.Turtle()
#         # t.shape("circle")
#         t.penup()
#         t.hideturtle()
#         t.shape(FIELD_DEFAULT)
#         t.color("blue")
#         # t.speed(0)
#         # t.goto((x+1)*100,(y+1)*100
#         t.setx(x*50)
#         t.sety(y*50)
#         # t.pendown()
#         t.st()
#         FIELD1.append(t)
#     FIELD.append(FIELD1)
#     FIELD1 = []
# print(FIELD)
# # ランダムでレベル1を生成する
# def create_new():
#     # 空きスペースのみ取得
#     empty_field = get_field_condition()
#     print(empty_field)
#     # 空きスペースが０なら終了
#     if len(empty_field) == 0:
#         msg = """complete!!
#         press a botton """
#     # ランダムで空きスペースにレベル１を生成
#     select_field = random.choice(empty_field)
#     print(select_field)
#     # select_field.write(LEVEL_ONE, True, align="center")
#     select_field.shape('triangle')
#
# """
# フィールドの状態を取得する
# １．空きスペース　from create_new
# ２．
# """
# def get_field_condition():
#     empty_field = []
#     for fs in FIELD:
#         for f in fs:
#             if f.shape() == FIELD_DEFAULT:
#                 empty_field.append(f)
#     # print(empty_field)
#     return empty_field
#
# def fn1():
#     sys.exit()
#
# def fn2():
#     FIELD[1][1].shape('circle')
#
# def fn3():
#     FIELD[1][1].shape('triangle')
#
# def fn4():
#     FIELD[1][1].shape('classic')
#
#
# wn.onkey(fn1,'a')
# wn.onkey(fn2,'b')
# wn.onkey(fn3,'c')
# wn.onkey(fn4,'d')
#
# wn.onkey(create_new,'Up')
# wn.onkey(create_new,'Down')
# wn.onkey(create_new,'Left')
# wn.onkey(create_new,'Right')
#
#
# wn.listen()




# while True:

#     t.dy -= gravity
#     t.sety(t.ycor() + t.dy)
#
#     if t.ycor() < -400:
#         t.dy *= -1
# #
wn.mainloop()
