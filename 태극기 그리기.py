import turtle
import math

def draw_taegukgi():
    # 1. 화면 및 기준 설정
    B = 400  # 세로 기준
    A = B * 1.5  # 가로 600
    D = B / 2  # 태극 지름 200
    R = D / 2  # 태극 반지름 100

    screen = turtle.Screen()
    screen.setup(A + 100, B + 100)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # 대각선 각도 (약 33.69도)
    angle = math.degrees(math.atan2(B, A))

    # 2. 태극 문양 (중앙 0,0에서 빈틈없이 작도)
    def draw_taegeuk():
        t.penup()
        t.goto(-83, 57)
        t.setheading(270 - angle) # 대각선 방향으로 회전

        # 파란색 (음)
        t.color("#0047A0")
        t.begin_fill()
        t.circle(R, 180)      # 아래 큰 반원
        t.circle(R/2, 180)    # 왼쪽 작은 반원 (안쪽)
        t.setheading(t.heading() + 180) # 방향 반전하여 구멍 메우기
        t.circle(R/2, -180)   # 오른쪽 작은 반원 (바깥쪽)
        t.end_fill()

        # 빨간색 (양)
        t.penup()
        t.goto(83, -55)
        t.setheading(90 - angle)
        t.color("#CD2E3A")
        t.begin_fill()
        t.circle(R, 180)
        t.circle(R/2, 180)
        t.setheading(t.heading() + 180)
        t.circle(R/2, -180)
        t.end_fill()

    # 3. 4괘(건곤감리) 정밀 작도
    def draw_gwae(name, pos_angle):
        gwae_l = D / 2
        gwae_w = D / 3
        th = gwae_w / 4
        gap = th / 2
        
        # [핵심] 태극에서 1/4D만큼 확실히 띄움 (R + D/4 + 괘너비/2)
        dist = R + (D / 4) + (gwae_w / 2)
        
        rad = math.radians(pos_angle)
        cx = dist * math.cos(rad)
        cy = dist * math.sin(rad)
        
        bars = {"건": (1,1,1), "곤": (0,0,0), "감": (0,1,0), "리": (1,0,1)}[name]
        
        for i in range(3):
            t.penup()
            offset = (i - 1) * (th + gap)
            t.goto(cx, cy)
            t.setheading(pos_angle + 0) # 대각선 수직 정렬
            t.forward(offset)
            t.left(90)
            t.forward(gwae_l / 2)
            t.right(180)
            
            t.color("black")
            t.pendown()
            
            if bars[i] == 1:
                t.begin_fill()
                for _ in range(2): t.forward(gwae_l); t.left(90); t.forward(th); t.left(90)
                t.end_fill()
            else:
                p_l = (gwae_l - gap) / 2
                for _ in range(2):
                    t.begin_fill()
                    for _ in range(2): t.forward(p_l); t.left(90); t.forward(th); t.left(90)
                    t.end_fill()
                    t.penup(); t.forward(p_l + gap); t.pendown()

    # 실행
    draw_taegeuk()
    draw_gwae("건", 180 - angle) # 왼쪽 위
    draw_gwae("곤", -angle)       # 오른쪽 아래
    draw_gwae("감", angle)        # 오른쪽 위
    draw_gwae("리", -180 + angle) # 왼쪽 아래

    screen.mainloop()

draw_taegukgi()
