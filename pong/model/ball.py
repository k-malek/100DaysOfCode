import pygame,random

class Ball:

    SIZE=20
    SPEED=100

    def __init__(self,game_speed,screen):
        self.position=(screen.get_width()//2,screen.get_height()//2)
        self.size=Ball.SIZE
        self.screen=screen
        self.game_speed=game_speed
        self.rect=pygame.Rect(self.position[0]-self.size//2,self.position[1]-self.size//2,self.size,self.size)
        self.spawn_vector_pos()
        self.reset()

    def reset(self):
        self.speed=Ball.SPEED*self.game_speed
        self.rect=pygame.Rect(self.position[0]-self.size//2,self.position[1]-self.size//2,self.size,self.size)
        self.spawn_vector_pos()

    def spawn_vector_pos(self):
        x=random.randint(30,70)/100
        y=1-x
        self.vector=random.choice([[x,y],[-x,y],[x,-y],[-x,-y]])

    def wall_collision_det(self):
        if self.rect.y<=0 or self.rect.y>=self.screen.get_height()-self.size:
            self.vector[1]=-self.vector[1]

    def paddles_collision_det(self,paddles):
        for paddle in paddles:
            if (self.rect.left >= paddle.rect.left and self.rect.left <= paddle.rect.right) or (self.rect.right >= paddle.rect.left and self.rect.right <= paddle.rect.right):
                if self.rect.centery>=paddle.rect.top and self.rect.centery<=paddle.rect.bottom:
                    self.vector[0]=-self.vector[0]
                    self.speed+=0.5

    def goal_detection(self):
        if self.rect.centerx<0:
            self.reset()
            return 0,1
        elif self.rect.centerx>self.screen.get_width():
            self.reset()
            return 1,0

    def update(self,paddles):
        self.wall_collision_det()
        self.paddles_collision_det(paddles)
        self.rect.move_ip(self.vector[0]*self.speed,self.vector[1]*self.speed)
        is_goal=self.goal_detection()
        if is_goal:
            return is_goal
        pygame.draw.ellipse(self.screen,(255,255,255),self.rect)
