from turtle import Turtle, Screen

scr = Screen()
scr.setup(450,450)
scr.screensize(200,200)

# 亀を動かす
def move(t):
    for _ in range(4):
        for _ in range(0,100,4):
            t.forward(3)
            yield(0)
        t.left(90)

# 亀の生成と初期位置の設定
ts = []
for x,y in [(-100,100),(100,-100),(100,100),(-100,-100)]:
    t = Turtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    ts.append(t)

# 亀を動かすgenerator
gs = [move(t) for t in ts]
while True:
    if sum([next(g,1) for g in gs]) >= 4:
        break
