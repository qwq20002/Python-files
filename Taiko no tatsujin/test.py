import pygame
pygame.init()
screen=pygame.display.set_mode([960,544])
pygame.display.set_caption("Taiko no tatsujin DEMO")

keep_going=True
clock=pygame.time.Clock()
#标记已按下按键
mousedown=False
tappedButton=[]
Don=True
Ka=True
#导入图片
#Import Note picture
Don=pygame.image.load("Don.png")
Ka=pygame.image.load("Ka.png")
LDon=pygame.image.load("LDon.png")
LKa=pygame.image.load("LKa.png")
#Import background picture
notesOnPlate=pygame.sprite.Group()
class notes(pygame.sprite.Sprite):
    scale=100
    def __init__(self,vel,shape):
        print("生成音符")
        pygame.sprite.Sprite.__init__(self)
        #设置音符类型
        if shape==1:
            self.image=Don
        elif shape==2:
            self.image=Ka
        elif shape==3:
            self.image=LDon
        elif shape==4:
            self.image=LKa
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=100
        self.image=pygame.transform.scale(self.image,(self.scale,self.scale))
    def update(self):
        self.rect.x-=self.vel
        if Don:
            pass

while keep_going:
    for event in pygame.event.get():
        if event.type==256:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousedown=True
        if event.type==pygame.MOUSEBUTTONUP:
            mousedown=False
    #显示背景
    screen.fill((0,0,0))
    if mousedown:
        newNote=notes(5,1)
        notesOnPlate.add(newNote)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
