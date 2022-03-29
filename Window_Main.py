from tkinter import *

from Window_Add import Window_Add_User
from Window_Add import Window_Add_Book
from Window_Search import Window_Search_User
from Window_Search import Window_Search_Book
from Panel_Show import Panel_Show_Book
from Panel_Show import Panel_Show_User


# ===========================================================================================
# 클래스: 메인 윈도우
# ===========================================================================================
class Window_Main():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("도서 대여 프로그램")
        self.window.geometry('1000x400')

        self.load_panels()      # 멤버 메소드 호출: 외부 패널 붙이기
        self.load_widgets()     # 멤버 메소드 호출: 위젯 붙이기

        self.window.mainloop()

    # 멤버 메소드: 위젯(외부 클래스의 객체) 생성
    def load_panels(self):
        Panel_Show_User(self.window, x=0, y=70)     # 회원 정보 패널 붙이기
        Panel_Show_Book(self.window, x=500, y=70)   # 도서 정보 패널 붙이기

    # 멤버 메소드: 멤버 속성(위젯) 정의하고 윈도우에 붙이기
    def load_widgets(self):
        self.btn_add_user = Button(self.window, text="신규 회원 추가", command=self.load_window_add_user)
        self.btn_add_user.place(x=0, y=0)

        self.btn_add_book = Button(self.window, text="신규 도서 추가", command=self.load_window_add_book)
        self.btn_add_book.place(x=250, y=0)

        self.btn_search_user = Button(self.window, text="회원 검색", command=self.load_window_search_user)
        self.btn_search_user.place(x=0, y=30)

        self.btn_search_book = Button(self.window, text="도서 검색", command=self.load_window_search_book)
        self.btn_search_book.place(x=500, y=30)

    # 멤버 메소드: (이벤트) 신규 회원 추가 윈도우 띄우기
    def load_window_add_user(self):
        Window_Add_User()

    # 멤버 메소드: (이벤트) 신규 도서 추가 윈도우 띄우기
    def load_window_add_book(self):
        Window_Add_Book()

    # 멤버 메소드: (이벤트) 회원 검색 결과 윈도우 띄우기
    def load_window_search_user(self):
        Window_Search_User()

    # 멤버 메소드: (이벤트) 도서 검색 결과 윈도우 띄우기
    def load_window_search_book(self):
        Window_Search_Book()
# ===========================================================================================