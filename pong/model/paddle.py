import pygame

class Paddle:

    WIDTH=20
    SPEED=70

    def __init__(self,game_speed,screen,x_pos=600):
        self.height=screen.get_height()//7
        self.width=Paddle.WIDTH
        self.speed=Paddle.SPEED*game_speed
        self.movement=0
        self.screen=screen
        self.rect=pygame.Rect(x_pos,screen.get_height()//2-self.height//2,self.width,self.height)

    def move_up(self):
        self.movement=-self.speed
    
    def move_down(self):
        self.movement=self.speed

    def stop(self):
        self.movement=0

    def update(self):
        #move
        if self.movement:
            if (self.rect.y<=0 and self.movement<0) or (self.rect.y>=self.screen.get_height()-self.height and self.movement>0):
                self.stop()
            else:
                self.rect.move_ip(0,self.movement)
        #draw
        pygame.draw.rect(self.screen,(255,255,255),self.rect)
