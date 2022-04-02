from tkinter import *

from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book
from Window_Search import Window_Search_User
from Window_Search import Window_Search_Book

SEARCH_ENTRY_WIDTH = 340
SEARCH_BUTTON_WIDTH = 50
SEARCH_HEIGHT = 24
INFO_BUTTON_Y = 290

# ======================================================================================================================
# 클래스: 회원 정보 패널
# ======================================================================================================================
class Panel_Show_User():

    # 생성자
    def __init__(self, window, x, y):
        self.user_editor = Panel_Edit_User(window, x+135, 100)      # 회원 정보 입력하는 패널 붙이기
        self.load_widgets(window, x, y)

    # 멤버 메소드: 멤버 속성(위젯) 정의하고 패널에 붙이기
    def load_widgets(self, window, x, y):
        self.label = Label(text="[회원 정보]")
        self.label.place(x=x, y=y)

        self.entry_search_user = Entry(window)
        self.entry_search_user.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_user = Button(window, text="검색", command=self.load_window_search_user)
        self.btn_search_user.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BUTTON_WIDTH, height=SEARCH_HEIGHT)

        self.btn_refresh_user = Button(window, text="원래대로")
        self.btn_refresh_user.place(x=x+240, y=INFO_BUTTON_Y, width=75)

        self.btn_save_user = Button(window, text="저장")
        self.btn_save_user.place(x=x+330, y=INFO_BUTTON_Y, width=75)

    # 멤버 메소드: (이벤트) 회원 검색 결과 윈도우 띄우기
    def load_window_search_user(self):
        Window_Search_User()
# ======================================================================================================================


# ======================================================================================================================
# 클래스: 도서 정보 패널
# ======================================================================================================================
class Panel_Show_Book():

    # 생성자
    def __init__(self, window, x, y):
        self.book_editor = Panel_Edit_Book(window, x+135, 100)    # 도서 정보 입력하는 패널 붙이기
        self.load_widgets(window, x, y)

    # 멤버 메소드: 멤버 속성(위젯) 정의하고 패널에 붙이기
    def load_widgets(self, window, x, y):
        self.label1 = Label(text="[도서 정보]")
        self.label1.place(x=x, y=y)

        self.entry_search_book = Entry(window)
        self.entry_search_book.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_book = Button(window, text="검색", command=self.load_window_search_book)
        self.btn_search_book.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BUTTON_WIDTH, height=SEARCH_HEIGHT)

        self.btn_delete_book = Button(window, text="삭제")
        self.btn_delete_book.place(x=x+150, y=INFO_BUTTON_Y, width=75)

        self.btn_refresh_book = Button(window, text="원래대로")
        self.btn_refresh_book.place(x=x+240, y=INFO_BUTTON_Y, width=75)

        self.btn_save_book = Button(window, text="저장")
        self.btn_save_book.place(x=x+330, y=INFO_BUTTON_Y, width=75)

      #  self.btn_refresh = Button(window, text="원래대로")
      #  self.btn_refresh.place(x=x-200, y=260, width=75)

      #  self.btn_save = Button(window, text="저장")
      #  self.btn_save.place(x=x-110, y=260, width=75)

    # 멤버 메소드: (이벤트) 도서 검색 결과 윈도우 띄우기
    def load_window_search_book(self):
        Window_Search_Book()

# ======================================================================================================================