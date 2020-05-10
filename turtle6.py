import sys
import turtle
import random

FIELD_DEFAULT = "classic"
LEVEL_ONE = "arrow"
LEVEL_TWO = "triangle"
LEVEL_THREE = "square"
LEVEL_FOUR = "circle"
LEVEL_FIVE = "turtle"

# sp = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

wn = turtle.Screen()
wn.screensize(400,400)
wn.reset()
wn.setworldcoordinates(-400,-400,400,400)
wn.bgcolor("black")
wn.title("game")
wn.mode("logo")
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

        t.setx(x*50)
        t.sety(y*50)
        # t.pendown()
        if abs(x) != 5 and abs(y) != 5:
            t.st()
            # isvisible()
        FIELD1.append(t)
    FIELD.append(FIELD1)
    FIELD1 = []
# print(FIELD)

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

# ランダムでレベル1を生成する
def create_new():
    # 空きスペースのみ取得
    empty_field = get_field_condition(1)
    # print(empty_field)
    # 空きスペースが０なら終了
    if len(empty_field) == 0:
        msg = """complete!!
        press q botton """

    # ランダムで空きスペースにレベル１を生成
    select_field = random.choice(empty_field)
    # print(select_field)
    # select_field.write(LEVEL_ONE, True, align="center")
    select_field.shape(LEVEL_ONE)

# 終了
def end():
    sys.exit()

def lu(sh):
    if sh == LEVEL_ONE:
        return LEVEL_TWO
    if sh == LEVEL_TWO:
        return LEVEL_THREE
    if sh == LEVEL_THREE:
        return LEVEL_FOUR
    if sh == LEVEL_FOUR:
        return LEVEL_FIVE

def corse_check(corse,pb):
    if len(corse) >= 2:
        if pb > 0:
            corse.sort(reverse=True)
        else:
            corse.sort()
        pre = [-200,FIELD[0][0],FIELD_DEFAULT]
        lu_flg = False
        for c in corse:
            if lu_flg == False:
                if c[1].shape() == pre[2]:
                    # del pre[2]
                    pre[1].shape(FIELD_DEFAULT)
                    c[1].shape(lu(c[1].shape()))
                    lu_flg = True
                else:
                    lu_flg = False
                c.append(c[1].shape())
                pre = c

# コースごとにアクティブタートル取得
def get_atfc(active_field,pb):
    # 隣り合う同レベルがいるか
    corse1 = []
    corse2 = []
    corse3 = []
    corse4 = []
    if abs(pb) == 1:
        for f in active_field:
            if f.xcor() == -150:
                corse1.append([f.ycor(),f])
            if f.xcor() == -50:
                corse2.append([f.ycor(),f])
            if f.xcor() == 50:
                corse3.append([f.ycor(),f])
            if f.xcor() == 150:
                corse4.append([f.ycor(),f])
    if abs(pb) == 2:
        for f in active_field:
            if f.ycor() == -150:
                corse1.append([f.xcor(),f])
            if f.ycor() == -50:
                corse2.append([f.xcor(),f])
            if f.ycor() == 50:
                corse3.append([f.xcor(),f])
            if f.ycor() == 150:
                corse4.append([f.xcor(),f])

    yield corse1
    yield corse2
    yield corse3
    yield corse4

def move2(corse,ncorse,pb):
    if pb > 0:
        print(corse)
        print(ncorse)
        print(1)
        corse.sort(reverse=True)
        ncorse.sort(reverse=True)
        if len(corse) != 0 and len(ncorse) != 0:
            while min(corse) < max(ncorse):
                pos = 150
                for c in corse:
                    print(c)
                    print(pos)

                    if c[0] == pos:
                        pos -= 100
                        continue
                    elif c[0] < pos:
                        c[0] += 100
                        if pb == 1:
                            c[1].sety(c[0])
                        else:
                            c[1].setx(c[0])
                        for n in ncorse:
                            if n[0] == c[0]:
                                n[0] -= 100
                                if pb == 1:
                                    n[1].sety(n[0])
                                else:
                                    n[1].setx(n[0])
                    pos -= 100
                    print(corse)
                    print(ncorse)
                    print(2)
                    corse.sort(reverse=True)
                    ncorse.sort(reverse=True)

                    yield(0)
    else:
        print(corse)
        print(ncorse)
        print(1)
        corse.sort()
        ncorse.sort()
        if len(corse) != 0 and len(ncorse) != 0:
            while max(corse) > min(ncorse):
                pos = -150
                for c in corse:
                    print(c)
                    print(pos)
                    if c[0] == pos:
                        pos += 100
                        continue
                    elif c[0] > pos:
                        c[0] -= 100
                        if pb == -1:
                            c[1].sety(c[0])
                        else:
                            c[1].setx(c[0])
                        for n in ncorse:
                            if n[0] == c[0]:
                                n[0] += 100
                                if pb == -1:
                                    n[1].sety(n[0])
                                else:
                                    n[1].setx(n[0])
                    pos += 100
                    print(corse)
                    print(ncorse)
                    print(2)
                    corse.sort()



                    ncorse.sort()
                    yield(0)

# 矢印を押した動作
def move(pb):
    # アクティブを取得
    active_field = get_field_condition(2)
    # コースごとジェネレータイテレータ up downはxグループ right leftはyグループ
    atgi = get_atfc(active_field,pb)
    for corse in atgi:
        if len(corse) >= 2:
            corse_check(corse,pb)

    active_field = get_field_condition(2)
    atgi = get_atfc(active_field,pb)
    nonactive_field = get_field_condition(1)
    natgi = get_atfc(nonactive_field,pb)

    corses = [move2(corse,ncorse,pb) for corse,ncorse in zip(atgi,natgi)]
    while True:
        if sum([next(c,1) for c in corses]) >= 4:
            break
    create_new()


wn.onkey(end,'q')

wn.onkey(create_new,'t')

wn.onkey(lambda: move(1),'Up')
wn.onkey(lambda: move(-1),'Down')
wn.onkey(lambda: move(2),'Right')
wn.onkey(lambda: move(-2),'Left')


wn.listen()
create_new()
# 同時に動かす
# https://teratail.com/questions/191385
wn.mainloop()
