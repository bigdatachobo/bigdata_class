import socket
from tkinter import * # 모든 모듈 가져옮.
from tkinter import messagebox # 가독성을 위해 따로 표기함
def run_client(host, port, str):
    with socket.socket() as s:# 클라이언트 소켓
        s.connect((host, port)) # 연결요청, 서버 주소(아이피,포트)        
        msg = str
        s.sendall(msg.encode())#문자열인코딩 -> 바이트배열 
       
        resp = s.recv(1024) #서버응답메세지을 기다린다 
        print(resp.decode())#바이트배열 -> 문자열로 복원

def okClick(e):#이벤트받자
   run_client(host='192.168.0.137', port=3000, str=txt.get())
   messagebox.showinfo("전송","전송완료")        
   
# =============================================================================
#   UI 화면 구성 ↓
# =============================================================================
root = Tk()
root.title('마이클라이언트')
root.geometry("200x100") # 창너비와 높이  
# 버튼 클릭 이벤트 핸들러

 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)
 
# 버튼 클릭 이벤트와 핸들러 정의
#btn = Button(root, text="OK", command=okClick)
btn = Button(root, text="OK",background='green')
btn.bind("<Button-1>",okClick)
txt.bind("<Return>",okClick)
btn.grid(row=1, column=1)

root.mainloop()
