import turtle
import math

def draw_taegukgi():
    B = 400 
    A = B * 1.5  
    D = B / 2  
    R = D / 2  

    screen = turtle.Screen()
    screen.setup(A + 100, B + 100)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    angle = math.degrees(math.atan2(B, A))


    def draw_taegeuk():
        t.penup()
        t.goto(-83, 57)
        t.setheading(270 - angle) 

        t.color("#0047A0")
        t.begin_fill()
        t.circle(R, 180)      
        t.circle(R/2, 180)    
        t.setheading(t.heading() + 180) 
        t.circle(R/2, -180)   
        t.end_fill()

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

    def draw_gwae(name, pos_angle):
        gwae_l = D / 2
        gwae_w = D / 3
        th = gwae_w / 4
        gap = th / 2
        
        dist = R + (D / 4) + (gwae_w / 2)
        
        rad = math.radians(pos_angle)
        cx = dist * math.cos(rad)
        cy = dist * math.sin(rad)
        
        bars = {"건": (1,1,1), "곤": (0,0,0), "감": (0,1,0), "리": (1,0,1)}[name]
        
        for i in range(3):
            t.penup()
            offset = (i - 1) * (th + gap)
            t.goto(cx, cy)
            t.setheading(pos_angle + 0) 
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

    draw_taegeuk()
    draw_gwae("건", 180 - angle) 
    draw_gwae("곤", -angle)       
    draw_gwae("감", angle)        
    draw_gwae("리", -180 + angle) 
    screen.mainloop()

draw_taegukgi()


