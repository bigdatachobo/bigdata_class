# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:15:32 2019

@author: sundooedu
"""

import socket

def run_server(port=3000):
    host='192.168.0.137' # 127.0.0.1 Loop back 주소
    # 연결하다 = 연결(=소켓=전화기)을 연다.
    with socket.socket() as s:
        s.bind((host, port)) # 소켓에 주소(아이피 + 포트) 설정 || (host,port)를 튜플로 받음.
        # 한번에 처리가능 client 수를 설정
        s.listen(1)#(대기) ## 한번에 처리가능 max N client( 나머지 연결대기) 최대   
        
        print('서버 시작')
        # listen:클리이언트 요청(송신=전화가 온다)을 기다린다.
        # accept 함수에서 대기하다가 클라이어트가 접속하면 새로운 소켓을 리턴
        # 그리고 접속한 클라이언트의 주소(아이피, 포트)가 리턴
        conn, addr = s.accept()  # <<<<<<이 부분에서 STOP!!!
        # 2. 송수신(통신처리)
        print('Connected',addr)
        msg = conn.recv(1024) # 3.클라이언트 요청메세지(데이터)를 최대 1024개를 받겠다. 기다린다.
        print(msg.decode()) # 수신 메세지 decode()하여 출력
        print("수신 바이트수 : ",len(msg)) # 수신 메세지 바이트수 출력
        # 요청메세지 msg ( 직렬화된 바이트 배열 )
        # 응답메세지 rMsg
        # 바아트 배열 >>> 'utf-8' 문자열로 복원 euc-kr
        rMsg = reverse(msg.decode()) # 바이트 배열 >>> 'utf-8' 문자열로 복원
        print(rMsg) # 송신바이트수 = 트래픽 (= 부하)
        print("송신 바이트수 : ",len(rMsg))
        
        #conn.sendall(rMsg.encode()) # 문자열 인코딩 >>> 바이트 배열
        conn.send(rMsg.encode()) # send는 전송 바이트수를 리턴함.
        conn.close()
        
def reverse(str):
    return ''.join(reversed(str)) 
       
if __name__ == '__main__':
    run_server() # 서버 실행
    
    
    
        