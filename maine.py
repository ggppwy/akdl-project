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

3일차
ground = box(pos = vec(0,-1,0), size = vec(11.2,1,1), color = color.green)

face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)


BOX = compound([face, eye1, eye2], pos = vec(0,10,0), color = color.cyan)

g = vec(0,-9.8,0)
BOX.v = vec(0,0,0)
dt = 0.01   

# 상자가 지면에 닿는 중심 y 좌표 (지면 표면 -0.5 + 상자 절반 0.5 = 0.0)
ground_level = 0.0

while True:
    rate(100)
    k = keysdown()
    
    # [조건 변경] 상자가 공중에 떠 있을 때만(BOX.pos.y > ground_level) 작동합니다.
    if BOX.pos.y > ground_level:
        
        # 1. 공중에 있을 때만 좌우 이동 가능
        if 'a' in k and BOX.pos.x > -5:
            BOX.pos.x -= 0.1
        if 'd' in k and BOX.pos.x < 5:
            BOX.pos.x += 0.1
            
        # 2. 공중에 있으므로 중력 적용 및 하강
        BOX.v = BOX.v + g * dt
        BOX.pos = BOX.pos + BOX.v * dt

    else:
        # 3. 지면에 닿은 순간: 속도를 완전히 0으로 지우고 y축 위치 고정
        BOX.v = vec(0,0,0)
        BOX.pos.y = ground_level
4일차
# 1.바닥 생성

ground = box(pos = vec(0,-1,0), size = vec(11.2,1,1), color = color.green)

# 2. 상자의 얼굴과 눈 생성
face = box(pos = vec(0,0,0), size = vec(1,1,1))
eye1 = sphere(radius=0.1, pos = vec(0.2, 0.2, 0.55), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2, 0.2, 0.55), color = color.black)

# 3. 컴파운드로 병합 및 초기 위치 설정
BOX = compound([face, eye1, eye2], pos = vec(0,10,0), color = color.cyan)

# 물리 상수 설정
g = vec(0,-9.8,0)
BOX.v = vec(0,0,0)
dt = 0.01   
ground_level = 0.0

# 시뮬레이션 루프
while True:
    rate(100)
    k = keysdown()
    
    # [추가] 공중에 있을 때 스페이스바를 누르면 즉시 지면으로 강제 이동
    if ' ' in k and BOX.pos.y > ground_level:
        BOX.v = vec(0,0,0)         # 속도 지우기
        BOX.pos.y = ground_level   # 지면으로 좌표 고정

    # 일반적인 공중 상태 (스페이스바를 누르지 않았을 때)
    elif BOX.pos.y > ground_level:
        # 1. 좌우 이동 제어
        if 'a' in k and BOX.pos.x > -5:
            BOX.pos.x -= 0.1
        if 'd' in k and BOX.pos.x < 5:
            BOX.pos.x += 0.1

    # 스페이스바 없이 자연스럽게 지면에 도달했을 때
    else:
        BOX.v = vec(0,0,0)
        BOX.pos.y = ground_level
