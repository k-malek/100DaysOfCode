import pygame
from model import Ball,Paddle

(WIDTH, HEIGHT) = (1200, 740)
FPS=60
GAME_SPEED=6/FPS
PADDLE_SCREEN_DISTANCE=70

screen = pygame.display.set_mode((WIDTH, HEIGHT))

paddle_A=Paddle(GAME_SPEED,screen,PADDLE_SCREEN_DISTANCE)
paddle_B=Paddle(GAME_SPEED,screen,WIDTH-PADDLE_SCREEN_DISTANCE-Paddle.WIDTH)
ball = Ball(GAME_SPEED,screen)
score = [0,0]

clock = pygame.time.Clock()
running=True

pygame.init()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_A.move_up()
            if event.key == pygame.K_s: 
                paddle_A.move_down()
            if event.key == pygame.K_UP: 
                paddle_B.move_up()
            if event.key == pygame.K_DOWN: 
                paddle_B.move_down()
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w,pygame.K_s): 
                paddle_A.stop()
            if event.key in (pygame.K_UP,pygame.K_DOWN): 
                paddle_B.stop()
        if event.type == pygame.QUIT:
            running = False
        
    #drawing scene
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255,255,255), (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    #updating on-screen objects
    paddle_A.update()
    paddle_B.update()
    goal=ball.update([paddle_A,paddle_B])
    if goal:
        score[0]+=goal[0]
        score[1]+=goal[1]
        goal=None
    screen.blit(pygame.font.SysFont('Calibri', 50).render(str(score[0]), True, (255,255,255)), (WIDTH//2-60, 50))
    screen.blit(pygame.font.SysFont('Calibri', 50).render(str(score[1]), True, (255,255,255)), (WIDTH//2+40, 50))
    
    pygame.display.flip()
    