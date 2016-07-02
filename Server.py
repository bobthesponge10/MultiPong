import socket
import time
import random
import math
connections = []
s = socket.socket()
host = input("Your Comp's Ip: ")
print(host)
port = 10000
s.bind((host, port))

done1 = False
done2 = False

screensizes = [[0, 0], [0, 0]]
screenx = 0
screeny = 0

direction = []

player = 0

x = 0
y = 0

P1 = "0".encode()
S1 = 0

P2 = "0".encode()
S2 = 0

xSpeed = 0
ySpeed = 0

def randomdir(side):
    y = math.sin(random.randint(16,40))*3
    x = math.sqrt(9-(y*y))
    if side == 0:
        x *= -1
    if random.randint(0, 1) == 1:
        y *= -1
    return [x, y]

s.listen(5)

while not done1:
    c, addr = s.accept()
    screensizes[player][0] = int(c.recv(1024))
    c.send(b"1")
    screensizes[player][1] = int(c.recv(1024))
    c.send(b"1")
    print('Got connection from', addr,screensizes)
    connections.append(c)
    if len(connections) == 2:
        done1 = True
    player += 1

print(connections)

screenx = min(screensizes[0][0], screensizes[1][0])
screeny = min(screensizes[0][1], screensizes[1][1])

P1 = str(int((screeny/2)-(screeny/16))).encode()
P2 = str(int((screeny/2)-(screeny/16))).encode()

connections[0].send(str(screenx).encode())
connections[0].recv(1024)
connections[0].send(str(screeny).encode())
connections[0].recv(1024)
connections[1].send(str(screenx).encode())
connections[1].recv(1024)
connections[1].send(str(screeny).encode())
connections[1].recv(1024)

for i in connections:
    i.send("1".encode())
    print(i)

time.sleep(5)



direction = randomdir(random.randint(0, 1))
ySpeed = direction[1]
xSpeed = direction[0]

x = int((screenx/2) - 10)
y = int((screeny/2) - 10)

while not done2:
    if y >= (screeny-20):
        ySpeed *= -1
    if y <= 0:
        ySpeed *= -1
    if x <= 40 and y > int(P1)-19 and  y < (int(P1) + (screeny/8) + 19):
        xSpeed *= -1

    if x >= (screenx-60) and y > int(P2) - 19 and y < (int(P2) + (screeny / 8) + 19):
        xSpeed *= -1
    if x < -20:
        S2 += 1
        direction = randomdir(random.randint(0, 1))
        ySpeed = direction[1]
        xSpeed = direction[0]
        x = int((screenx / 2) - 10)
        y = int((screeny / 2) - 10)

    if x > screenx:
        S1 += 1
        direction = randomdir(random.randint(0, 1))
        ySpeed = direction[1]
        xSpeed = direction[0]
        x = int((screenx / 2) - 10)
        y = int((screeny / 2) - 10)

    x += xSpeed
    y += ySpeed
    print("1")
    connections[0].send(P2)
    print("2")
    P1 = connections[0].recv(1024)
    print("3")
    connections[1].send(P1)
    print("4")
    P2 = connections[1].recv(1024)
    print("5")
    print(S1, S2)
    connections[0].send(str(S1).encode())
    connections[0].recv(1024)
    connections[0].send(str(S2).encode())
    connections[0].recv(1024)
    connections[1].send(str(S2).encode())
    connections[1].recv(1024)
    connections[1].send(str(S1).encode())
    connections[1].recv(1024)
    connections[0].send(str(int(x)).encode())
    connections[0].recv(1024)
    connections[0].send(str(int(y)).encode())
    connections[0].recv(1024)
    connections[1].send(str(int((screenx-x))-20).encode())
    connections[1].recv(1024)
    connections[1].send(str(int(y)).encode())
    connections[1].recv(1024)



