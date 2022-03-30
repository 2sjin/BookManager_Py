from tkinter import *
from tkinter import messagebox

from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book


# ========================================================================================================
# 클래스: 신규 회원 추가 윈도우
# ========================================================================================================
class Window_Add_User():
    
    # 생성자
    def __init__(self):
        
        self.window = Tk()
        self.window.geometry('400x215')
        self.window.title("신규 회원 추가")
        def func_exit(event):
            self.window.quit()
            self.window.destroy()
        self.user_editor = Panel_Edit_User(self.window, x=140, y=0)   # 회원 Edit 패널을 윈도우에 포함시킴
        self.button_check = Button(self.window,text="확인",width=7, command=self.add_user)  # [확인] 버튼 이벤트 추가
        self.button_check.place(x=240,y=180)
        self.button_cancel = Button(self.window,text="취소",width=7)
        self.button_cancel.bind("<ButtonRelease-1>",func_exit)
        self.button_cancel.place(x=320,y=180)
        
        self.window.mainloop()

    def add_user(self):
        yes_or_no = messagebox.showinfo("신규 회원 추가", "신규 회원 추가 완료(이벤트 테스트)")
# ========================================================================================================


# ========================================================================================================
# 클래스: 신규 도서 추가 윈도우
# ========================================================================================================
class Window_Add_Book():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x100')
        self.window.title("신규 도서 추가")

        self.book_editor = Panel_Edit_Book(self.window, x=0, y=0)   # 도서 Edit 패널을 윈도우에 포함시킴
        
        self.window.mainloop()        
# ========================================================================================================