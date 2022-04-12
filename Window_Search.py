from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

WINDOW_GEOMETRY = '595x400'

SELECT_CANCEL_BTN_WIDTH = 81

SEARCH_ENTRY_WIDTH = 460
SEARCH_BTN_WIDTH = 100
SEARCH_HEIGHT = 24

DIR_CSV_USER = "csv/user.csv"
DIR_CSV_BOOK = "csv/book.csv"
DIR_CSV_RENT = "csv/rent.csv"

# =========================================================
# 클래스: 회원 검색 결과 윈도우
# =========================================================
class Window_Search_User():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("회원 검색 결과")
        self.window.geometry(WINDOW_GEOMETRY)

        self.entry_search_user = Entry(self.window)
        self.entry_search_user.place(x=10, y=30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_user = Button(self.window, text="검색", command=self.event_user_search)
        self.btn_search_user.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_user = Label(self.window, text="회원 검색 결과: 2 개")
        self.label_search_user.place(x=10, y=75)

        self.btn_select_user = Button(self.window, text="선택", command=self.event_user_select)
        self.btn_select_user.place(x=400, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.btn_cancel = Button(self.window, text="취소", command=self.event_cancel)
        self.btn_cancel.place(x=500, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.load_table()

        self.window.mainloop()

    # 멤버 메소드: 테이블 불러오기
    def load_table(self):
        column_tuple = ("전화번호", "이름", "생년월일", "성별", "이메일", "등록")
        width_tuple = (100, 70, 90, 50, 200, 60)

        self.user_table = ttk.Treeview(self.window, column=column_tuple, displaycolumns=column_tuple)
        self.user_table.place(x=10, y=100, height=240)

        # 컬럼(헤더) 설정
        for i in range(6):
            self.user_table.column(column_tuple[i], width=width_tuple[i], anchor="center")
            self.user_table.heading(column_tuple[i], text=column_tuple[i], anchor="center")

        self.user_table["show"] = "headings"    # 열 인덱스를 표시하지 않음

        sample_value_1 = ("01025773617", "이승진", "1997-06-18", "남", "options3224@naver.com", True)
        sample_value_2 = ("01012345678", "홍길동", "1950-01-01", "남", "hgd@naver.com", True)
        self.user_table.insert("", "end", text="", value=sample_value_1, iid=sample_value_1[0])
        self.user_table.insert("", "end", text="", value=sample_value_2, iid=sample_value_2[0])

        self.scrollbar = Scrollbar(self.user_table, orient=HORIZONTAL)
        self.scrollbar.config()

    # 멤버 메소드: [검색] 버튼 이벤트
    def event_user_search(self):
        # 테이블 초기화
        for item in self.user_table.get_children():
            self.user_table.delete(item)
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        index_key = self.entry_search_user.get()
        condition = df_user[df_user["USER_NAME"].str.contains(index_key)]
        for user_phone in condition["USER_PHONE"]:
            user_name = condition["USER_NAME"].loc[user_phone]
            user_birthday = condition["USER_BIRTH"].loc[user_phone]
            user_sex = condition["USER_SEX"].loc[user_phone]
            user_email = condition["USER_MAIL"].loc[user_phone]
            user_reg = condition["USER_REG"].loc[user_phone]
            user_add = (user_phone,user_name,user_birthday,user_sex,user_email,user_reg)
            self.user_table.insert("","end",text="",value=user_add,iid=user_add[0])

    # 멤버 메소드: [선택] 버튼 이벤트
    def event_user_select(self):
        messagebox.showinfo("회원 선택", "회원 선택(이벤트 테스트)")

    # 멤버 메소드: [취소] 버튼 이벤트
    def event_cancel(self):
        self.window.quit()
        self.window.destroy()

# =========================================================


# =========================================================
# 클래스: 도서 검색 결과 윈도우
# =========================================================
class Window_Search_Book():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("도서 검색 결과")
        self.window.geometry(WINDOW_GEOMETRY)

        self.entry_search_book = Entry(self.window)
        self.entry_search_book.place(x=10, y=30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_book = Button(self.window, text="검색", command=self.event_book_search)
        self.btn_search_book.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_book = Label(self.window, text="도서 검색 결과: 2 개")
        self.label_search_book.place(x=10, y=75)

        self.btn_select_book = Button(self.window, text="선택", command=self.event_book_select)
        self.btn_select_book.place(x=400, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.btn_cancel = Button(self.window, text="취소", command=self.event_cancel)
        self.btn_cancel.place(x=500, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.load_table()

        self.window.mainloop()

    # 멤버 메소드: 테이블 불러오기
    def load_table(self):
        column_tuple = ("ISBN", "도서명", "저자", "출판사")
        width_tuple = (140, 160, 160, 110)

        self.book_table = ttk.Treeview(self.window, column=column_tuple, displaycolumns=column_tuple)
        self.book_table.place(x=10, y=100, height=240)

        # 컬럼(헤더) 설정
        for i in range(4):
            self.book_table.column(column_tuple[i], width=width_tuple[i], anchor="center")
            self.book_table.heading(column_tuple[i], text=column_tuple[i], anchor="center")

        self.book_table["show"] = "headings"    # 열 인덱스를 표시하지 않음

        sample_value_1 = ("9788970504773", "파이썬과 데이터 과학", "천인국, 박동규, 강영민", "생능출판")
        sample_value_2 = ("9788970509563", "명품 자바 에센셜", "황기태", "생능출판")
        self.book_table.insert("", "end", text="", value=sample_value_1, iid=sample_value_1[0])
        self.book_table.insert("", "end", text="", value=sample_value_2, iid=sample_value_2[0])

        self.scrollbar = Scrollbar(self.book_table, orient=HORIZONTAL)
        self.scrollbar.config()

    # 멤버 메소드: [선택] 버튼 이벤트
    def event_book_search(self):
        messagebox.showinfo("도서 검색", "도서 검색(이벤트 테스트)")

    # 멤버 메소드: [선택] 버튼 이벤트
    def event_book_select(self):
        messagebox.showinfo("도서 선택", "도서 선택(이벤트 테스트)")

    # 멤버 메소드: [취소] 버튼 이벤트
    def event_cancel(self):
        self.window.quit()
        self.window.destroy()

# =========================================================