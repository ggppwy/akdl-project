
face = box()
eye1 = sphere(radius=0.1, pos = vec(0.2,0.2,0.5), color = color.black)
eye2 = sphere(radius=0.1, pos = vec(-0.2,0.2,0.5), color = color.black)

A = compound([face, eye1, eye2])
