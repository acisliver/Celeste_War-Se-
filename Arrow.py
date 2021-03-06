#화살의 움직임
import pygame

class Arrow(pygame.Rect):
    speed=0
    screen = None
    arrow = pygame.image.load("resources/images/arrow1.png")

    def __init__(self,screen,x,y,speed):
        super().__init__(self.arrow.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.height+=10
        self.top=x-5
        self.left=y
        self.speed=speed
        self.screen=screen
        self.name='Arrow'

    def move(self):         #화살의 움직임 함수
        self.left -= self.speed
        self.screen.blit(self.arrow,(self.top+30,self.left))