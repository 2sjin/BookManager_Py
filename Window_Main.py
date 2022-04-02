from tkinter import *

from Window_Add import Window_Add_User
from Window_Add import Window_Add_Book
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
        self.window.geometry('900x575')

        Panel_Show_User(self.window, x=10, y=20)    # 회원 정보 패널 붙이기
        Panel_Show_Book(self.window, x=475, y=20)   # 도서 정보 패널 붙이기
        self.load_menu()                            # 메뉴바 붙이기

        self.window.mainloop()

    # 멤버 메소드: 윈도우 상단에 메뉴 붙이기
    def load_menu(self):
        # 메뉴바 추가
        self.menubar = Menu(self.window, tearoff=0)
        self.window.config(menu = self.menubar)

        # [파일] 메뉴 추가
        self.menu_1 = Menu(self.menubar)
        self.menubar.add_cascade(label="파일", menu=self.menu_1)

        # [파일] 메뉴의 하위 항목 추가
        self.menu_1.add_command(label="프로그램 종료", command=quit)

        # [신규 데이터 추가] 메뉴 추가
        self.menu_2 = Menu(self.menubar)
        self.menubar.add_cascade(label="신규 데이터 추가", menu=self.menu_2)

        # [신규 데이터 추가] 메뉴의 하위 항목 추가
        self.menu_2.add_command(label="신규 회원 추가", command=self.load_window_add_user)
        self.menu_2.add_separator()
        self.menu_2.add_command(label="신규 도서 추가", command=self.load_window_add_book)

    # 멤버 메소드: (이벤트) 신규 회원 추가 윈도우 띄우기
    def load_window_add_user(self):
        Window_Add_User()

    # 멤버 메소드: (이벤트) 신규 도서 추가 윈도우 띄우기
    def load_window_add_book(self):
        Window_Add_Book()

# ===========================================================================================