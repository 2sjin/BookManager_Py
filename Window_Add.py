from tkinter import *

from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book


# ========================================================================================================
# 클래스: 신규 회원 추가 윈도우
# ========================================================================================================
class Window_Add_User():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x100')
        self.window.title("신규 회원 추가")
        
        self.user_editor = Panel_Edit_User(self.window, x=0, y=0)   # 회원 Edit 패널을 윈도우에 포함시킴
        
        self.window.mainloop()
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