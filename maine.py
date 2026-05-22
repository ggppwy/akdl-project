1일차
face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)

A = compound([face, eye1, eye2])

box(size = vec(10, 1, 10), color = color. green)




while True :
    rate(100)
    k = keysdown()
    if 'a' in k and A.pos.x > -10 :
        A.pos.x = A.pos.x - 0.1
    if 'd' in k and A.pos.x < 10 :
        A.pos.x = A.pos.x + 0.1  

2일차
canvas(background=color.white)

ground = box(pos = vec(0,-0.5,0), size = vec(10,1,10), color = color.black)

face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)

BOX = compound([face, eye1, eye2], pos = vec(0,10,0), color = color.cyan)

while True :
    rate(100)
    k = keysdown()
    if 'a' in k and BOX.pos.x > -5 :
        BOX.pos.x = BOX.pos.x - 0.1
    if 'd' in k and BOX.pos.x < 5 :
        BOX.pos.x = BOX.pos.x + 0.1
        
g = vec(0,-9.8,0)

BOX.v = vec(0,0,0)
dt = 0.01    
    
    while BOX.pos.y >=0:
    rate(100)
    
    BOX.pos = BOX.pos + BOX.v*dt

    BOX.v = BOX.v + g*dt
