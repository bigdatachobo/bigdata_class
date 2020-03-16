# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:07:34 2019

@author: sundooedu
"""

from socket import *
import threading
import time
import sys
isLoop = True

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))
        if sendData == 'quit': # 통신종료 명령어
            sock.close()
            sys.exit()
            break
            
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))
        
port = 2000        
clientSock = socket()
clientSock.connect(('127.0.0.1',port)) # accept()로 연결요청
print('접속 완료')

# 챗팅서비스(메세지 송수신) 요청진행된다.     
sender = threading.Thread(target=send, args = (clientSock,))# ',' 있는 이유는 튜플임을 강조하기위함
receiver = threading.Thread(target=receive, args = (clientSock,))
    
sender.start()
receiver.start()

sender.join()
receiver.join()
