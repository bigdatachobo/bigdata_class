# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:06:18 2019

@author: sundooedu
"""
import socket
def run_client(host, port, strList):
    with socket.socket() as s: # 클라이언트 소켓
        s.connect((host,port))  # 연결요청, 서버 주소(아이피, 포트) || (host,port)를 튜플로 보냄
        msg = " ".join(strList) # 클라이언트 요청 메세지
        a=s.sendall(msg.encode())
        # s.sendall(b'abc')
        print("바이트수=",a)
        resp = s.recv(1024) # 서버응답 메세지를 기다린다. # <<<<<<이 부분에서 STOP!!!
        print(resp.decode()) # 바이트배열 -> 문자열로 복원
        
if __name__ == '__main__':
    run_client(host='192.168.0.138', port = 3000, strList=['오늘은 야근 ㄴㄴ'] ) 

#%% up-version
def run_client(host, port, strList):
    with socket.socket() as s: # 클라이언트 소켓
        s.connect((host,port))  # 연결요청, 서버 주소(아이피, 포트) || (host,port)를 튜플로 보냄
        msg = " ".join(strList) # 클라이언트 요청 메세지
        a=s.sendall(msg.encode())
        # s.sendall(b'abc')
        print("바이트수=",a)
        resp = s.recv(1024) # 서버응답 메세지를 기다린다. # <<<<<<이 부분에서 STOP!!!
        print(resp.decode()) # 바이트배열 -> 문자열로 복원
        
if __name__ == '__main__':
    run_client(host='192.168.0.137', port = 3000, strList=['a','b','c'] )
#%% up-version 2
def run_client(host, port, strList):
    with socket.socket() as s: # 클라이언트 소켓
        s.connect((host,port))  # 연결요청, 서버 주소(아이피, 포트) || (host,port)를 튜플로 보냄
        msg = " ".join(strList) # 클라이언트 요청 메세지
        print(msg)
        #a=s.sendall(msg.encode('utf-8')) # 문자열 'utf-8' 기본값이라 생략 가능 >>> 바이트배열
        #a = s.sendall(b'i know i know iknow') #b는 바이트를 의미 >>> 바이트 인코딩으로 보내라는 의미임.
        a = s.send(msg.encode()) # send는 전송 바이트수를 리턴함.
        print("송신 바이트수=",a)
        resp = s.recv(1024) # 서버응답 메세지를 기다린다. # <<<<<<이 부분에서 STOP!!!
        print(resp.decode()) # 바이트배열 -> 문자열로 복원
        print("수신바이트수=",len(resp))
        
if __name__ == '__main__':
    run_client(host='192.168.0.137', port = 3000, strList=['a','b','c'] )    
#%% up_version 3

def run_client(host, port, strList):
    with socket.socket() as s: # 클라이언트 소켓
        s.connect((host,port))  # 연결요청, 서버 주소(아이피, 포트) || (host,port)를 튜플로 보냄
        msg = " ".join(strList) # 클라이언트 요청 메세지
        print(msg)
        #a=s.sendall(msg.encode('utf-8')) # 문자열 'utf-8' 기본값이라 생략 가능 >>> 바이트배열
        #a = s.sendall(b'i know i know iknow') #b는 바이트를 의미 >>> 바이트 인코딩으로 보내라는 의미임.
        a = s.send(msg.encode()) # send는 전송 바이트수를 리턴함.
        print("송신 바이트수=",a)
        while True: # 응답메세지를 1024개씩 나누어서 반복 수신
            resp = s.recv(1024) # 서버응답 메세지를 기다린다. # <<<<<<이 부분에서 STOP!!!
            if not resp: # 응답메세지 없으면
                break    # 종료
                
            print(resp.decode()) # 바이트배열 -> 문자열로 복원
            print("수신바이트수=",len(resp))
        
if __name__ == '__main__':
    run_client(host='192.168.0.137', port = 3000, strList=['a','b','c'] )      
    
import tkinter
root = tkinter.Tk()
root.title("전송메세지")
root.geometry()    
    



















       