from math import sin,cos


WIDTH = 80
HEIGHT = 22

tilt = 0.5
sinA = sin(tilt)
cosA = cos(tilt)

screen = [[' ']*WIDTH for _ in range(HEIGHT)]
zbuffer = [[0]*WIDTH for _ in range(HEIGHT)]

#Clear screen to start
for r in range(HEIGHT):
    for c in range(WIDTH):
        screen[r][c] = ' '
        zbuffer[r][c] = 0

#Loop around the tube cross section
theta = 0
while theta < 6.28:
    phi = 0
    while phi < 6.28:
        sinT = sin(theta)
        cosT = cos(theta)
        sinP = sin(phi)
        cosP = cos(phi)

        R = cosT + 2 # Radius (How far away is the point from the donut center)
        D = 1 / (sinP * R * sinA + sinT * cosA + 5) # How close is the point to the camera
        t = sinP * R * cosA - sinT * sinA # Vertical position of the point after donut is tilted

        x = int(40 + 30 * D * (cosP * R))
        y = int(12 + 15 * D * t)

        N = 8 * (sinT * sinA - sinP * cosT * cosA- sinP * cosT * sinA - sinT * cosA)

        if (y > 0 and y < HEIGHT and x > 0 and x < WIDTH and D > zbuffer[y][x]):
            zbuffer[y][x] = D
            screen[y][x] = ".,-~:;=!*#$@"[int(N) if N > 0 else 0]
        phi += 0.02
    theta += 0.07

for r in range(HEIGHT):
    for c in range(WIDTH):
        print(screen[r][c],end="")
    print("")
