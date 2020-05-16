import sys
import turtle
import random
import pyaudio
import wave
import time
import pathlib
import threading

FIELD_DEFAULT = "classic"
LEVEL_ONE = "arrow"
LEVEL_TWO = "triangle"
LEVEL_THREE = "square"
LEVEL_FOUR = "circle"
LEVEL_FIVE = "turtle"

# sp = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

#define callback
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

#open stream using callback
def create():
    global p
    global stream
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
    # return stream

def play_bgm():
    global bgm
    global stream
    global wf
    bgm = True
    wf = wave.open(r"BGM\loop3.wav", 'rb')
    create()
    stream.start_stream()

def check_bgm():
    global bgm
    global stream
    if not stream.is_active():
        bgm = False
    if bgm is False:
        create_thread()

def create_thread():
    mythreading = threading.Thread(target=play_bgm)
    mythreading.start()

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
    return turtle_list

# ランダムでレベル1を生成する
def create_new():
    empty_field = get_field_condition(1)
    # 空きスペースが０なら終了
    if len(empty_field) == 0:
        msg = """complete!!
        press q botton """
        t=turtle.Turtle()
        t.color('red')
        t.setpos(0,200)
        t.write(msg,True,"center",("Sans",30,"bold"))
        #stop stream
        stream.stop_stream()
        stream.close()
        wf.close()

        #close pyaudio
        p.terminate()

        return 0

    # ランダムで空きスペースにレベル１を生成
    select_field = random.choice(empty_field)
    set_lev(select_field)

# 終了
def end():
    sys.exit()

def set_lev(t,flg=False):
    if flg is True:
        t.shape(FIELD_DEFAULT)
        t.color('blue')
    else:
        if t.shape() == FIELD_DEFAULT:
            t.shape(LEVEL_ONE)
            t.color('yellow')
        elif t.shape() == LEVEL_ONE:
            t.shape(LEVEL_TWO)
            t.color('pink')
        elif t.shape() == LEVEL_TWO:
            t.shape(LEVEL_THREE)
            t.color('white')
        elif t.shape() == LEVEL_THREE:
            t.shape(LEVEL_FOUR)
            t.color('red')
        elif t.shape() == LEVEL_FOUR:
            t.shape(LEVEL_FIVE)
            t.color('green')

def corse_check(corse,pb):
    if len(corse) >= 2:
        if pb > 0:
            corse.sort(reverse=True)
        else:
            corse.sort()
        pre = [-200,FIELD[0][0],FIELD_DEFAULT]
        # フラグがフォルスなら
        lu_flg = False
        for c in corse:
            if lu_flg == False:
                if c[1].shape() == pre[2] and pre[2] != LEVEL_FIVE:
                    set_lev(pre[1],True)
                    set_lev(c[1])
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
        corse.sort(reverse=True)
        ncorse.sort(reverse=True)
        if len(corse) != 0 and len(ncorse) != 0:
            while min(corse) < max(ncorse):
                pos = 150
                for c in corse:
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
                    corse.sort(reverse=True)
                    ncorse.sort(reverse=True)

                    yield(0)
    else:
        corse.sort()
        ncorse.sort()
        if len(corse) != 0 and len(ncorse) != 0:
            while max(corse) > min(ncorse):
                pos = -150
                for c in corse:
                    if c[0] == pos:
                        pos += 100
                        continue
                    elif c[0] > pos:
                        c[0] -= 100
                        # ここから分割してみる
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
                    corse.sort()
                    ncorse.sort()
                    yield(0)

# 矢印を押した動作
def move(pb):
    check_bgm()
    global wait_flg
    if wait_flg is True:
        return 0
    wait_flg = True
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
    wait_flg = False


wait_flg = False
bgm = False

wn = turtle.Screen()
wn.screensize(400,400)
wn.reset()
wn.setworldcoordinates(-400,-400,400,400)
wn.bgcolor("black")
wn.title("game")
wn.mode("logo")

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
        FIELD1.append(t)
    FIELD.append(FIELD1)
    FIELD1 = []

# wf = wave.open(r"BGM\loop3.wav", 'rb')
# play_bgm()
# check_bgm(1)
create_thread()


wn.onkey(end,'q')

wn.onkey(lambda: move(1),'Up')
wn.onkey(lambda: move(-1),'Down')
wn.onkey(lambda: move(2),'Right')
wn.onkey(lambda: move(-2),'Left')

create_new()

wn.listen()
wn.mainloop()


# TODO: 100回カウンタ
# 動作なめらか
# 先のタートルで進化
# https://docs.python.org/ja/3/library/turtle.html
