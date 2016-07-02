import pygame
import socket

screenx = 0
screeny = 0

ready = False
ready1 = 0

pygame.init()
pygame.display.set_caption("Pong")
icon = pygame.image.load("icon.bmp")
pygame.display.set_icon(icon)
font1 = pygame.font.SysFont('Calibri', 25, True, False)
clock = pygame.time.Clock()

s = socket.socket()
host = socket.gethostname()
port = 10000
connect = input("Connect to: ")
s.connect((connect, port))

s.send(str(pygame.display.Info().current_w).encode())
s.recv(1024)
s.send(str(pygame.display.Info().current_h).encode())
s.recv(1024)

Fullscreen = 0

x = 0
y = 0

P1 = 0
S1 = 0

P2 = 0
S2 = 0


speed = 0

screenx = int(s.recv(1024))
s.send(b"1")
screeny = int(s.recv(1024))
s.send(b"1")

P1 = (screeny/2)-(screeny/16)
P2 = (screeny/2)-(screeny/16)

x = (screenx/2) - 10
y = (screeny/2) - 10

print(screenx)
print(screeny)

s.recv(1024)

screen = pygame.display.set_mode((screenx, screeny), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screenx, screeny))
pygame.mouse.set_visible(True)

done = False



while not done:
    print("1")
    P2 = int(s.recv(1024))
    print("2")
    s.send(str(int(P1)).encode())
    print("3")
    S1 = int(s.recv(1024))
    s.send(b"1")
    S2 = int(s.recv(1024))
    s.send(b"1")
    x = int(s.recv(1024))
    s.send(b"1")
    y = int(s.recv(1024))
    s.send(b"1")

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                done = True
            if event.key == pygame.K_UP:
                    speed -=3
            if event.key == pygame.K_DOWN:
                    speed += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed += 3
            if event.key == pygame.K_DOWN:
                speed -= 3
            if event.key == pygame.K_f:
                if Fullscreen == 1:
                    pygame.display.set_mode((screenx, screeny))
                    pygame.mouse.set_visible(True)
                    Fullscreen = 0
                else:
                    pygame.display.set_mode((screenx, screeny), pygame.FULLSCREEN)
                    pygame.mouse.set_visible(False)
                    Fullscreen = 1


    if speed < 0:
        if P1-3 < 0:
            if P1-2 < 0:
                if not P1-1 < 0:
                    P1-=1
            else:
                P1-=2
        else:
            P1-=3

    if speed > 0:
        if P1 + 3 + (screeny/8) > screeny:
            if P1 + 2 + (screeny/8) > screeny:
                if not P1 + 1 + (screeny/8) > screeny:
                    P1 += 1
            else:
                P1 += 2
        else:
            P1 += 3
    print(S1, S2)
    text1 = font1.render(("Score: " + str(S1)), True, (0, 0, 0))
    text2 = font1.render(("Score: " + str(S2)), True, (0, 0, 0))
    screen.blit(text1, [(screenx/2) - 50 - font1.size(("Score: " + str(S1)))[0], 0])
    screen.blit(text2, [screenx/2+50, 0])
    pygame.draw.rect(screen, (0, 0, 0), [20, P1, 20, screeny/8])
    pygame.draw.rect(screen, (0, 0, 0), [screenx-40, P2, 20, screeny / 8])
    pygame.draw.rect(screen, (0, 0, 0), [x, y, 20, 20])
    pygame.draw.line(screen, (0, 0, 0), [(screenx/2),0], [(screenx)/2, screeny])

    pygame.display.flip()
    clock.tick(60)
