import pygame
from time import perf_counter
from tjaFileRead import read
pygame.init()                                         #初始化Pygame
screen=pygame.display.set_mode([960,544])             #更改窗口大小
pygame.display.set_caption("Taiko no tatsujin DEMO")  #更改窗口标题

keep_going=True
clock=pygame.time.Clock()
#标记已按下按键
tappedButton=[]
isDon=False
isKa=False
#导入图片
#导入音符图片
Don=pygame.image.load("Don.png")
Ka=pygame.image.load("Ka.png")
LDon=pygame.image.load("LDon.png")
LKa=pygame.image.load("LKa.png")
empty=pygame.image.load("empty.png")
font=pygame.font.SysFont("score",45)
#导入谱面

PADS=[]
#导入背景图片
bgPicture=pygame.image.load("bgPicture.png")
#导入音效
SDon=pygame.mixer.Sound("SDon.wav")
SKa=pygame.mixer.Sound("SKa.wav")
bgmusic=pygame.mixer.Sound("songs/shennvpiguan/shennvpiguan.ogg")
mousedown=False
#导入鼓面图片
LeftKa=pygame.image.load("LeftKa.png")
LeftDon=pygame.image.load("LeftDon.png")
RightDon=pygame.image.load("RightDon.png")
RightKa=pygame.image.load("RightKa.png")
basicInfo,Pad=read("songs/shennvpiguan/shennvpiguan.ply")
#{'TITLE': 'ShennvPiguan', 'BPM': '95', 'OFFSET': '-8.68', 'SCOREINIT': '1140', 'SCOREDIFF': '260'}
scoreInit=int(basicInfo.get("SCOREINIT"))
OFFSET=abs(float(basicInfo.get("OFFSET")))
BPM=int(basicInfo.get("BPM"))*4
scoreDiff=int(basicInfo.get("SCOREDIFF"))
#建议在窗口内的音符集合
notesOnPlate=pygame.sprite.Group()
class notes(pygame.sprite.Sprite):
    scale=100
    def __init__(self,vel,shape):
        pygame.sprite.Sprite.__init__(self)
        #设置音符类型
        if shape==1:
            self.image=Don
            self.shape="D"
        elif shape==2:
            self.image=Ka
            self.shape="K"
        elif shape==3:
            self.image=LDon
            self.shape="LD"
        elif shape==4:
            self.image=LKa
            self.shape="LK"
        if shape==1 or shape ==2:
            self.rect=self.image.get_rect()
            self.rect.x=960
            self.rect.y=34
        if shape==3 or shape==4:
            self.rect=self.image.get_rect()
            self.rect.x=960
            self.rect.y=18
        self.vel=vel
    def update(self):
        self.rect.x-=self.vel
        
#分数信息
GREAT=0  #良
GOOD=0   #可
BAD=0    #不可
combo=0 #COMBO
tapper=0
time1=perf_counter()
#bgmusic.play()
while keep_going:
    for event in pygame.event.get():
        if event.type==256:
            keep_going=False
        if event.type==pygame.KEYDOWN:
            #100D,107K
            #102F,106J
            if event.key==100:           #如果按下按键
                SKa.play()               #播放音效
                tappedButton.append("D") #将按下的按键放入tappedButton
                isKa=True
            if event.key==107:
                SKa.play()
                tappedButton.append("K")
                isKa=True
            if event.key==102:
                SDon.play()
                tappedButton.append("F")
                isDon=True
            if event.key==106:
                SDon.play()
                tappedButton.append("J")
                isDon=True
        if event.type==pygame.KEYUP:
            if event.key==100:
                tappedButton.remove("D")
                isKa=False
            if event.key==107:
                tappedButton.remove("K")
                isKa=False
            if event.key==102:
                tappedButton.remove("F")
                isDon=False
            if event.key==106:
                tappedButton.remove("J")
                isDon=False
    #显示背景
    screen.fill((0,0,0))
    screen.blit(bgPicture,(0,0))
    time2=perf_counter()
    if time2-time1 >= OFFSET:
        time1=perf_counter() - ((perf_counter() - time1) - 60/BPM)
        OFFSET=9999999999
    if OFFSET==9999999999:
        if time2-time1>=60/BPM:
            time1=perf_counter() - ((perf_counter() - time1) - 60/BPM)
            tapper+=1
            if not int(Pad[tapper])==0:
                newNote=notes(7,int(Pad[tapper]))
                notesOnPlate.add(newNote)
    #显示音符
    notesOnPlate.update()
    notesOnPlate.draw(screen)
    #显示鼓面
    for i in tappedButton:
        if i=="D":
            screen.blit(LeftKa,(132,11))
        if i=="F":
            screen.blit(LeftDon,(150,20))
        if i=="J":
            screen.blit(RightDon,(190,20))
        if i=="K":
            screen.blit(RightKa,(186,11))
    #判定
    if not(notesOnPlate.__len__()==0): #若不是空谱面才开始判定
        if isDon:#如果按下的是“咚”
            if notesOnPlate.sprites()[0].shape=="D" or notesOnPlate.sprites()[0].shape=="LD":    #第一个音符是“咚”
                dis=abs(notesOnPlate.sprites()[0].rect.x-(275 if notesOnPlate.sprites()[0].shape=="D" else 263))
                if dis<=5:
                    GREAT+=1
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                    combo+=1
                elif dis<=10:
                    GOOD+=1
                    combo+=1
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                elif dis<=20:
                    BAD+=1
                    combo=0
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                else:
                    pass
                if dis<=30:
                    if combo%10==0:
                        score+=scoreDiff
        elif isKa: #如果按下的是“咔”
            if notesOnPlate.sprites()[0].shape=="K"  or notesOnPlate.sprites()[0].shape=="LK":    #第一个音符是“咔”
                dis=abs(notesOnPlate.sprites()[0].rect.x-(275 if notesOnPlate.sprites()[0].shape=="K" else 263))
                if dis<=5:
                    GREAT+=1
                    combo+=1
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                elif dis<=10:
                    GOOD+=1
                    combo+=1
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                elif dis<=20:
                    BAD+=1
                    combo=0
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
                else:
                    pass
                if dis<=30:
                    if combo%10==0:
                        score+=scoreDiff
        else:
            if notesOnPlate.sprites()[0].rect.x<=220:
                if not notesOnPlate.sprites()[0].shape=="E":
                    BAD+=1
                    combo=0
                    notesOnPlate.remove(notesOnPlate.sprites()[0])
    #显示分数
    score=int(GREAT*scoreInit+GOOD*scoreInit*0.6)
    scoreFont=font.render(str(score),True,(255,255,255))
    scoreRect=scoreFont.get_rect()
    scoreRect.x=5
    scoreRect.y=5
    screen.blit(scoreFont,scoreRect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
