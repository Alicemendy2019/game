import sys
import turtle
import random

FIELD_DEFAULT = "arrow"
LEVEL_ONE = 1
LEVEL_TWO = 2
LEVEL_THREE = 3
LEVEL_FOUR = 4
LEVEL_FIVE = 5

sp = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

wn = turtle.Screen()
wn.screensize(400,400)
wn.reset()
wn.setworldcoordinates(-400,-400,400,400)
wn.bgcolor("black")
wn.title("game")

# FIELD = [[f for f in range(4)] for i in range (4)]
FIELD = []
FIELD1 = []
for x in [-3,-1,1,3]:
    for y in [-3,-1,1,3]:
        t=''
        t=turtle.Turtle()
        # t.shape("circle")
        t.penup()
        t.hideturtle()
        t.shape(FIELD_DEFAULT)
        t.color("blue")
        # t.speed(0)
        # t.goto((x+1)*100,(y+1)*100
        t.setx(x*50)
        t.sety(y*50)
        # t.pendown()
        t.st()
        FIELD1.append(t)
    FIELD.append(FIELD1)
    FIELD1 = []
print(FIELD)
# ランダムでレベル1を生成する
def create_new():
    # 空きスペースのみ取得
    empty_field = get_field_condition()
    print(empty_field)
    # 空きスペースが０なら終了
    if len(empty_field) == 0:
        msg = """complete!!
        press a botton """
    # ランダムで空きスペースにレベル１を生成
    select_field = random.choice(empty_field)
    print(select_field)
    # select_field.write(LEVEL_ONE, True, align="center")
    select_field.shape('triangle')

"""
フィールドの状態を取得する
１．空きスペース　from create_new
２．
"""
def get_field_condition():
    empty_field = []
    for fs in FIELD:
        for f in fs:
            if f.shape() == FIELD_DEFAULT:
                empty_field.append(f)
    # print(empty_field)
    return empty_field
# 終了
def end():
    sys.exit()
# 矢印を押した動作（上）
def move_up():
    # 盤面を取得

    # アクティブが上のみなら何もしない
    if len(active_field)

wn.onkey(end,'q')

wn.onkey(create_new,'Up')
wn.onkey(create_new,'Down')
wn.onkey(create_new,'Left')
wn.onkey(create_new,'Right')


wn.listen()




# while True:

#     t.dy -= gravity
#     t.sety(t.ycor() + t.dy)
#
#     if t.ycor() < -400:
#         t.dy *= -1
# #
wn.mainloop()
