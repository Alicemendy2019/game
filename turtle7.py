import sys
import turtle
import random
import pyaudio
import wave
import time
import pathlib
import threading
import operator

def reset_level(self):
    self.LEVEL = FIELD_DEFAULT
    self.shape(self.LEVEL[0])
    self.color(self.LEVEL[1])

def set_lev(self):
    if self.LEVEL == FIELD_DEFAULT:
        self.LEVEL = LEVEL_ONE
    elif self.LEVEL == LEVEL_ONE:
        self.LEVEL = LEVEL_TWO
    elif self.LEVEL == LEVEL_TWO:
        self.LEVEL = LEVEL_THREE
    elif self.LEVEL == LEVEL_THREE:
        self.LEVEL = LEVEL_FOUR
    elif self.LEVEL == LEVEL_FOUR:
        self.LEVEL = LEVEL_FIVE
    self.shape(self.LEVEL[0])
    self.color(self.LEVEL[1])

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

def get_field_condition(cond):
    turtle_list = [f for fs in FIELD for f in fs \
        if ((cond == 1 and f.shape() == FIELD_DEFAULT[0]) \
            or (cond == 2 and f.shape() != FIELD_DEFAULT[0]))]
    return turtle_list

def finish():
    msg = """finish!!
    end : press q botton
    retry : press r botton"""
    t=turtle.Turtle()
    t.color('red')
    t.setpos(0,-200)
    t.write(msg,True,"center",("Sans",20,"bold"))
    #stop stream
    stream.stop_stream()
    stream.close()
    wf.close()
    #close pyaudio
    p.terminate()
    active_field = get_field_condition(2)
    tp1 , tp2 , tp3 , tp4 , tp5 = [],[],[],[],[]
    for f in active_field:
        if f.LEVEL == LEVEL_ONE:
            tp1.append(f)
        elif f.LEVEL == LEVEL_TWO:
            tp2.append(f)
        elif f.LEVEL == LEVEL_THREE:
            tp3.append(f)
        elif f.LEVEL == LEVEL_FOUR:
            tp4.append(f)
        elif f.LEVEL == LEVEL_FIVE:
            tp5.append(f)
    tl = [turtle.Turtle() for i in range(0,5)]
    lg=(g for g in LEVEL_LIST)
    lpg=(pg for pg in [len(tp1),len(tp2),len(tp3),len(tp4),len(tp5)])
    i=0
    pl=[1,10,25,50,100]
    sum=0
    totalscoreturtle=turtle.Turtle()
    totalscoreturtle.penup()
    totalscoreturtle.hideturtle()
    totalscoreturtle.color('gold')
    totalscoreturtle.setpos(50,200)
    # totalscoreturtle.write('TOTAL SCORE:\n  ' + '  '+ str(sum),False,"left",("Sans",12,"bold"))
    totalscoreturtle.st()

    for t in tl:
        t.penup()
        t.hideturtle()
        ll=next(lg)
        lp=next(lpg)
        t.shape(ll[0])
        t.color(ll[1])
        t.setpos(-75,250-i*20)
        thp=pl[i]*lp
        t.write('    ×'+str(lp)+' = ' + str(thp),False,"left",("Sans",12,"bold"))
        sum += thp
        totalscoreturtle.undo()
        totalscoreturtle.write('  TOTAL SCORE:\n' + '      ' + str(sum) + ' POINTS',False,"left",("Sans",15,"bold"))
        t.st()
        i += 1
# ランダムでレベル1を生成する
def create_new():
    empty_field = get_field_condition(1)
    # 空きスペースが０なら終了
    if len(empty_field) == 0 or ct.COUNTER == 0:
        finish()
        return 0

    # ランダムで空きスペースにレベル１を生成
    select_field = random.choice(empty_field)
    select_field.set_lev(select_field)

# 終了
def end():
    sys.exit()

def corse_check_for_levelup(corse,pb):
    if len(corse) >= 2:
        if pb > 0:
            corse.sort(reverse=True)
        else:
            corse.sort()
        pre = [-200,FIELD[0][0],FIELD_DEFAULT[0]]
        # フラグがフォルスなら
        lu_flg = False
        for c in corse:
            if lu_flg == False:
                if c[1].shape() == pre[2] and pre[2] != LEVEL_FIVE[0]:
                    # pre[1].reset_level(pre[1])
                    # c[1].set_lev(c[1])
                    pre[1].set_lev(pre[1])
                    c[1].reset_level(c[1])
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
        mc1=operator.methodcaller('xcor')
        mc2=operator.methodcaller('ycor')
    elif abs(pb) == 2:
        mc2=operator.methodcaller('xcor')
        mc1=operator.methodcaller('ycor')
    for f in active_field:
        if mc1(f) == -150:
            corse1.append([mc2(f),f])
        if mc1(f) == -50:
            corse2.append([mc2(f),f])
        if mc1(f) == 50:
            corse3.append([mc2(f),f])
        if mc1(f) == 150:
            corse4.append([mc2(f),f])
    yield corse1
    yield corse2
    yield corse3
    yield corse4

def move2(corse,ncorse,pb):
    if pb > 0:
        cond={'reverse':True,'start_pos':150,'step_pos':-100,'corse1':corse,'corse2':ncorse,'neg':1}
    else:
        cond={'reverse':False,'start_pos':-150,'step_pos':100,'corse1':ncorse,'corse2':corse,'neg':-1}
    corse.sort(reverse=cond['reverse'])
    ncorse.sort(reverse=cond['reverse'])
    if len(corse) != 0 and len(ncorse) != 0:
        while min(cond['corse1']) < max(cond['corse2']):
            pos = cond['start_pos']
            for c in corse:
                if c[0] == pos:
                    pos += cond['step_pos']
                    continue
                elif c[0]*cond['neg'] < pos*cond['neg']:
                    c[0] += cond['step_pos']*-1
                    if pb == 1*cond['neg']:
                        c[1].sety(c[0])
                    else:
                        c[1].setx(c[0])
                    for n in ncorse:
                        if n[0] == c[0]:
                            n[0] += cond['step_pos']
                            if pb == 1*cond['neg']:
                                n[1].sety(n[0])
                            else:
                                n[1].setx(n[0])
                pos += cond['step_pos']
                corse.sort(reverse=cond['reverse'])
                ncorse.sort(reverse=cond['reverse'])
                yield(0)

# 矢印を押した動作
def move(pb):
    check_bgm()
    global wait_flg
    if wait_flg is True:
        return 0
    wait_flg = True
    ct.COUNTER -= 1
    ct.undo()
    ct.write('COUNTER:'+str(ct.COUNTER),False,"center",("Sans",10,"bold"))
    # アクティブを取得
    active_field = get_field_condition(2)
    # コースごとアクティブタートルジェネレータイテレータ
    atgi = get_atfc(active_field,pb)
    # ２つ以上アクティブならレベルアップ用にコースチェックする
    for corse in atgi:
        if len(corse) >= 2:
            corse_check_for_levelup(corse,pb)
    # アクティブタートルとノンアクティブタートル取得
    active_field = get_field_condition(2)
    atgi = get_atfc(active_field,pb)
    nonactive_field = get_field_condition(1)
    natgi = get_atfc(nonactive_field,pb)
    # 移動する
    corses = [move2(corse,ncorse,pb) for corse,ncorse in zip(atgi,natgi)]
    while True:
        if sum([next(c,1) for c in corses]) >= 4:
            break
    create_new()
    wait_flg = False

def retry():
    global COUNTER
    global wait_flg
    global bgm
    global FIELD
    global ct
    global stream
    global wf
    global p

    if wait_flg is True:
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()
    wn.reset()
    wn.clear()
    wn.screensize(400,400)
    wn.reset()
    wn.setworldcoordinates(-400,-400,400,400)
    wn.bgcolor("black")
    wn.title("game")
    wn.mode("logo")

    COUNTER = 50
    wait_flg = False
    bgm = False
    FIELD = []
    FIELD1 = []
    for x in [-3,-1,1,3]:
        for y in [-3,-1,1,3]:
            t=''
            t=turtle.Turtle()
            t.penup()
            t.hideturtle()
            setattr(t,'LEVEL',LEVEL)
            setattr(t,'reset_level',reset_level)
            setattr(t,'set_lev',set_lev)
            t.reset_level(t)
            t.setx(x*50)
            t.sety(y*50)
            if abs(x) != 5 and abs(y) != 5:
                t.st()
            FIELD1.append(t)
        FIELD.append(FIELD1)
        FIELD1 = []

    create_thread()

    ct=object()
    ct=turtle.Turtle()
    ct.penup()
    ct.color('white')
    ct.setpos(-200,200)
    setattr(ct,'COUNTER',COUNTER)
    ct.write('COUNTER:'+str(ct.COUNTER),False,"center",("Sans",10,"bold"))

    wn.onkey(retry,'r')
    wn.onkey(end,'q')
    wn.onkey(lambda: move(1),'Up')
    wn.onkey(lambda: move(-1),'Down')
    wn.onkey(lambda: move(2),'Right')
    wn.onkey(lambda: move(-2),'Left')

    create_new()

    wn.listen()
    wn.mainloop()


FIELD_DEFAULT = ("classic",'blue')
LEVEL_ONE = ("arrow",'yellow')
LEVEL_TWO = ("triangle",'pink')
LEVEL_THREE = ("square",'white')
LEVEL_FOUR = ("circle",'red')
LEVEL_FIVE = ("turtle",'green')

LEVEL_LIST=[LEVEL_ONE,LEVEL_TWO,LEVEL_THREE,LEVEL_FOUR,LEVEL_FIVE]
LEVEL = FIELD_DEFAULT

wn = turtle.Screen()
wait_flg = False
retry()

# wn.onkey(retry,'r')
# wn.onkey(end,'q')
# wn.onkey(lambda: move(1),'Up')
# wn.onkey(lambda: move(-1),'Down')
# wn.onkey(lambda: move(2),'Right')
# wn.onkey(lambda: move(-2),'Left')
#
# create_new()
#
# wn.listen()
# wn.mainloop()

# TODO: 100回カウンタ
# 動作なめらか
# 先のタートルで進化
# https://docs.python.org/ja/3/library/turtle.html
