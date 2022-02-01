import pygame
import time
from tjaFileRead import read
#import tjaFileRead
pygame.init()                                         #初始化Pygame
screen=pygame.display.set_mode([960,544])             #更改窗口大小
pygame.display.set_caption("Taiko no tatsujin DEMO")  #更改窗口标题
SDon=pygame.mixer.Sound("SDon.wav")
SKa=pygame.mixer.Sound("SKa.wav")
clock=pygame.time.Clock()

tapper=0
keep_going=True

basicInfo,Pad=read("songs/shennvpiguan/shennvpiguan.ply")
scoreInit=int(basicInfo.get("SCOREINIT"))
OFFSET=abs(float(basicInfo.get("OFFSET")))
BPM=int(basicInfo.get("BPM"))*4
scoreDiff=int(basicInfo.get("SCOREDIFF"))

t_on=time.perf_counter()
while keep_going:
    for event in pygame.event.get():
        if event.type==256:
            keep_going=False
    if time.perf_counter()-t_on>=60/BPM:
        t_on=time.perf_counter() - ((time.perf_counter() - t_on) - 60/BPM)
        tapper+=1
        if not int(Pad[tapper])==0:
            if Pad[tapper]=='1' or Pad[tapper]=='3':
                SDon.play()
            elif Pad[tapper]=='2' or Pad[tapper]=='4':
                SKa.play()
    clock.tick(60)
pygame.quit()

