import math
import pygame
from sys import exit

def drawTree(start_pos,end_pos,angle,mid_diff):

    len = ((((start_pos[0]-end_pos[0])**2)+((start_pos[1]-end_pos[1])**2))**0.5)*(2/3)

    if (len<1): return

    pygame.draw.line(screen,(255,255,255),start_pos,end_pos,2)

    x1 = end_pos[0] + math.cos(math.radians(angle)) * len
    y1 = end_pos[1] - math.sin(math.radians(angle)) * len
    x2 = end_pos[0] + math.cos(math.radians(angle+mid_diff)) * len
    y2 = end_pos[1] - math.sin(math.radians(angle+mid_diff)) * len

    start_pos = end_pos
    end_pos1 = (x1,y1)
    end_pos2 = (x2,y2)
    angle -= (mid_diff//2)

    drawTree(start_pos,end_pos1,angle,mid_diff)
    drawTree(start_pos,end_pos2,angle+mid_diff,mid_diff)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Fractal Tree")
clock = pygame.time.Clock()

angle = 0
flag = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))

    mid_diff = (180-(angle*2))
    drawTree((400,400),(400,280),angle,mid_diff)

    if flag:
        angle += 1
        if angle>=88 :
            flag = False
    else:
        angle -= 1
        if angle<=0:
            flag = True

    pygame.display.update()
    clock.tick(40)