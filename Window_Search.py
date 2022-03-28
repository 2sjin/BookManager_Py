from tkinter import *


# =========================================================
# 클래스: 회원 검색 결과 윈도우
# =========================================================
class Window_Search_User():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("회원 검색 결과")
        self.window.geometry('300x100')

        self.label = Label(self.window, text="회원 검색 결과")
        self.label.place(x=0, y=0)

        self.window.mainloop()
# =========================================================


# =========================================================
# 클래스: 도서 검색 결과 윈도우
# =========================================================
class Window_Search_Book():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("도서 검색 결과")
        self.window.geometry('300x100')

        self.label = Label(self.window, text="도서 검색 결과")
        self.label.place(x=0, y=0)

        self.window.mainloop()
# =========================================================