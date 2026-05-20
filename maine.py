
face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)

A = compound([face, eye1, eye2])

box(size = vec(10, 1, 10), color = color. green)


face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)
A = compound([face, eye1, eye2])

while True :
    rate(100)
    k = keysdown()
    if 'a' in k and A.pos.x > -10 :
        A.pos.x = A.pos.x - 0.1
    if 'd' in k and A.pos.x < 10 :
        A.pos.x = A.pos.x + 0.1  
