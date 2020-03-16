# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:19:16 2020

@author: sundooedu
"""
#%%
import os
import numpy as np

os.chdir('C:/Users/sundooedu/Downloads/BIGDATA BACKUP/Python/Re_New_Teacher/source')
#%%
# initialization
height = 5 #그리드 설정
Width = 5 
posX = 0 #시작점 설정
posY = 0 
endX = Width-1 #도착점 설정
endY = height-1
actions = [0, 1, 2, 3] #액션 설정
stateCount = height*Width #총 상태갯수
actionCount = len(actions) #총 액션갯수
#%%
# Actions
episode=100
for i in range(episode):
    posX = 0
    posY = 0
    done = False; 
    while not done:
        action = np.random.choice(actions) #임의의 액션        
        if action==0: posX = posX-1 if posX>0 else posX # left 
        if action==1: posX = posX+1 if posX<Width-1 else posX# right
        if action==2: posY = posY-1 if posY>0 else posY# up
        if action==3: posY = posY+1 if posY<height-1 else posY# down
        done = posX==endX and posY==endY #도착하면 done
        nextState = Width*posY + posX #각 위치를 25개의 숫자로 매치시켜줌
        reward = 1 if done else 0 #도착했으면 보상
        
    # Drawing    
    for i in range(height):
        for j in range(Width):
            if posY==i and posX==j:
                print("O", end=''); #시작점에 동그라미
            elif endY==i and endX==j:
                print("T", end=''); #끝나는 점에 T
            else:
                print(".", end=''); #나머지는 점
        print("");        
#%%
import numpy as np
import pygame

# initialization
height = 5 #그리드 설정
Width = 5 
posX = 0 #시작점 설정
posY = 0 
endX = Width-1 #도착점 설정
endY = height-1
actions = [0, 1, 2, 3] #액션 설정
stateCount = height*Width #총 상태갯수
actionCount = len(actions) #총 액션갯수

episode=100
for i in range(episode):

    
    flag = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
                pygame.quit()
                exit(0) #게임 끝내기
                
        pygame.init() #초기화
        screen = pygame.display.set_mode([840,859]) #화면
        screen.fill(0) #화면색
        player = pygame.image.load('../image/lego.png') #이미지로딩  
        screen.blit(player, (0,0)) # 플레이어  그리기
        pygame.display.update() # 보여주기
        pygame.time.delay(100)                    
        screen.blit(player, (posX*100, posY*100)) #플레이이어 그리기
        pygame.display.update() #보여주기
#%%
import numpy as np
import pygame
# initialization
height = 5 #그리드 설정
Width = 5 
posX = 0 #시작점 설정
posY = 0 
endX = Width-1 #도착점 설정
endY = height-1
actions = [0, 1, 2, 3] #액션 설정
stateCount = height*Width #총 상태갯수
actionCount = len(actions) #총 액션갯수

pygame.init() #초기화
screen = pygame.display.set_mode([500,500]) #화면
screen.fill(0) #화면색
player = pygame.image.load('../image/lego.png') #이미지로딩
player = pygame.transform.scale(player,(100,100))  
steps_list= []
#%%        
episode=100
for i in range(episode):
    
    flag = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
                pygame.quit()
                exit(0) #게임 끝내기
                
        posX = 0
        posY = 0
        done = False
        steps = 0
        while not done:
            action = np.random.choice(actions) #임의의 액션        
            if action==0: posX = posX-1 if posX>0 else posX # left 
            if action==1: posX = posX+1 if posX<Width-1 else posX# right
            if action==2: posY = posY-1 if posY>0 else posY# up
            if action==3: posY = posY+1 if posY<height-1 else posY# down
            done = posX==endX and posY==endY #도착하면 done
            nextState = Width*posY + posX #각 위치를 25개의 숫자로 매치시켜줌
            reward = 1 if done else 0 #도착했으면 보상
            
            screen.fill(0)
            screen.blit(player, (posX*100, posY*100)) #플레이이어 그리기
            pygame.display.update() #보여주기
            pygame.time.delay(100) 
            steps += 1
            print('action: ',action, [posX, posY])
        print('total steps: ', steps)
        steps_list.append(steps)
        
        # Drawing    
        for i in range(height):
            for j in range(Width):
                if posY==i and posX==j:
                    print("O", end=''); #시작점에 동그라미
                elif endY==i and endX==j:
                    print("T", end=''); #끝나는 점에 T
                else:
                    print(".", end=''); #나머지는 점
            print("");           