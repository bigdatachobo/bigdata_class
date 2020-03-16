# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:07:27 2019

@author: sundooedu
"""

from socket import *
import threading
import time
# 클라이언트 동시 송수신
# 클라이언트에게 메세지 송신
isSendLoop = True
def send(sock):
    while isSendLoop:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))
    
# 클라이언트에게 메세지 수신    
def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))
        if recvData == 'quit':
            sock.close()
            sys.exit()
            global isSendLoop # isSendLoop 지역 아니고 전역 변수
            isSendLoop = False # send 무한반복 종료 >>> send(sock) 함수 스레드 종료하기 위함.
            break

port = 2000
serverSock = socket()
serverSock.bind(('',port)) # ' ' 비어있으면 127.0.0.1 이되고 해당 컴퓨터 ip가 배당됨.
serverSock.listen(1) 
print(f'{port}번 포트로 접속 대기중...')

while True:
    time.sleep(1)
    connectionSock, addr = serverSock.accept()
    print(str(addr), '에서 접속되었습니다.')
    #송수신 멀티스레드
    sender = threading.Thread(target=send, args = (connectionSock,))
    receiver = threading.Thread(target=receive, args = (connectionSock,))
    
    sender.start()
    receiver.start()
    