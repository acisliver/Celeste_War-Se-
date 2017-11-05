#게임 종료시 나타나는 win or lose문구
import pygame

class WL:
    exitcode=0
    screen=None

    def __init__(self,screen,exitcode):
        self.screen=screen
        self.exitcode=exitcode
        self.regame=None

    def printf(self,exitcode):
        self.exitcode=exitcode
        if self.exitcode == 0:              #exitcode는
            pygame.font.init()              #폰트 초기화
            font=pygame.font.Font("resources/font/consola.ttf",100)     #폰트 불러오기
            text=font.render("You Lose",True,(255, 0, 0))                 #빨간색 폰트 객체 생성
            textRect=text.get_rect()                                        #폰트 위치 불러오기
            textRect.center=(350,400)       #폰트 위치 지정
            self.screen.blit(text,textRect)                                 #폰트 블릿

        else:
            pygame.font.init()                                              #위와 같은 과정
            font = pygame.font.Font("resources/font/consola.ttf", 100)
            text = font.render("You Win!!", True, (29,219,22))
            textRect = text.get_rect()
            textRect.center = (300, 400)
            self.screen.blit(text, textRect)

        regame = pygame.font.Font("resources/font/consola.ttf", 30)
        regametext = regame.render("Regame", True, (255, 255, 255))
        regametextRect = regametext.get_rect()
        regametextRect.center = (350, 500)
        self.regame = regametextRect
        self.screen.blit(regametext, regametextRect)




        pygame.display.flip()