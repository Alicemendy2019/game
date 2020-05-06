import sys
import turtle
import random

FIELD_DEFAULT = "arrow"
LEVEL_ONE = "turtle"
LEVEL_TWO = "circle"
LEVEL_THREE = "square"
LEVEL_FOUR = "triangle"
LEVEL_FIVE = "classic"

# sp = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

wn = turtle.Screen()
wn.screensize(400,400)
wn.reset()
wn.setworldcoordinates(-400,-400,400,400)
wn.bgcolor("black")
wn.title("game")

# FIELD = [[f for f in range(4)] for i in range (4)]
FIELD = []
FIELD1 = []
for x in [-5,-3,-1,1,3,5]:
    for y in [-5,-3,-1,1,3,5]:
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
        if abs(x) != 5 and abs(y) != 5:
            t.st()
            # isvisible()
        FIELD1.append(t)
    FIELD.append(FIELD1)
    FIELD1 = []
print(FIELD)
# ランダムでレベル1を生成する
def create_new():
    # 空きスペースのみ取得
    empty_field = get_field_condition(1)
    print(empty_field)
    # 空きスペースが０なら終了
    if len(empty_field) == 0:
        msg = """complete!!
        press a botton """

    # ランダムで空きスペースにレベル１を生成
    select_field = random.choice(empty_field)
    print(select_field)
    # select_field.write(LEVEL_ONE, True, align="center")
    select_field.shape(LEVEL_ONE)

"""
フィールドの状態を取得する
１．空きスペース　from create_new
２．
"""
def get_field_condition(cond):
    turtle_list = []
    for fs in FIELD:
        for f in fs:
            if cond == 1:
                if f.shape() == FIELD_DEFAULT:
                    turtle_list.append(f)
            elif cond == 2:
                if f.shape() != FIELD_DEFAULT:
                    turtle_list.append(f)
    # print(empty_field)
    return turtle_list
# 終了
def end():
    sys.exit()
# 矢印を押した動作（上）
def move_up():
    # アクティブを取得
    active_field = get_field_condition(2)
    # レベルとポジションを取得
    # level_one_list = []
    # level_two_list = []
    # level_three_list = []
    # level_four_list = []
    # level_five_list = []
    # for al in active_field:
    #     if al.shape() == LEVEL_ONE:
    #         level_one_list.append(al)
    #     elif al.shape() == LEVEL_TWO:
    #         level_two_list.append(al)
    #     elif al.shape() == LEVEL_THREE:
    #         level_three_list.append(al)
    #     elif al.shape() == LEVEL_FOUR:
    #         level_four_list.append(al)
    #     elif al.shape() == LEVEL_FIVE:
    #         level_five_list.append(al)


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
