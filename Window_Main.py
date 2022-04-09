from tkinter import *
from tkinter import messagebox

import pandas as pd

from Window_Add import Window_Add_User
from Window_Add import Window_Add_Book
from Panel_Show import Panel_Show_Book
from Panel_Show import Panel_Show_User

BOOK_INFO_X = 475
BOOK_INFO_Y = 20
BTN_WIDTH = 75

DIR_CSV_USER = "csv/user.csv"
DIR_CSV_RENT = "csv/rent.csv"

# ===========================================================================================
# 클래스: 메인 윈도우
# ===========================================================================================
class Window_Main():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("도서 대여 프로그램")
        self.window.geometry('900x575')

        self.userinfo = Panel_Show_User(self.window, x=10, y=20)    # 회원 정보 패널 붙이기
        self.bookinfo = Panel_Show_Book(self.window, x=BOOK_INFO_X, y=BOOK_INFO_Y)   # 도서 정보 패널 붙이기

        # 대여 버튼
        self.btn_save_book = Button(self.window, text="대여", command=self.event_book_rent)
        self.btn_save_book.place(x=BOOK_INFO_X+240, y=BOOK_INFO_Y+500, width=BTN_WIDTH)

        # 반납 버튼
        self.btn_save_book = Button(self.window, text="반납", command=self.event_book_return)
        self.btn_save_book.place(x=BOOK_INFO_X+330, y=BOOK_INFO_Y+500, width=BTN_WIDTH)

        self.load_menu()    # 메뉴바 붙이기

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

    # 멤버 메소드: [대여] 버튼 이벤트
    def event_book_rent(self):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])

        df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)
        df_rent.index.name = "RENT_SEQ"

        isbn = self.bookinfo.get_isbn()
        phone = self.userinfo.get_phone()

        new_rent = { "BOOK_ISBN": isbn,\
                    "USER_PHONE": phone,\
                    "RENT_DATE": 20221101,\
                    "RENT_DUE_DATE": 20221115,\
                    "RENT_RETURN_DATE": -1 }
        df_rent = df_rent.append(new_rent, ignore_index=True)

        df_user["USER_RENT_CNT"].loc[phone] += 1

        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
        df_rent.to_csv(DIR_CSV_RENT, index=True, encoding='CP949')

        messagebox.showinfo("도서 대여", "도서 대여 완료(이벤트 테스트)")

    # 멤버 메소드: [반납] 버튼 이벤트
    def event_book_return(self):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])

        df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)
        df_rent.index.name = "RENT_SEQ"

        isbn = self.bookinfo.get_isbn()
        seq = max(df_rent[df_rent["BOOK_ISBN"] == isbn].index)
        rent_phone = df_rent["USER_PHONE"].loc[seq]

        df_rent["RENT_RETURN_DATE"].loc[seq] = 20221111
        df_user["USER_RENT_CNT"].loc[rent_phone] -= 1

        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
        df_rent.to_csv(DIR_CSV_RENT, index=True, encoding='CP949')

        messagebox.showinfo("도서 반납", "도서 반납 완료(이벤트 테스트)")

# ===========================================================================================