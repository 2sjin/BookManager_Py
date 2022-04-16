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
    def __init__(self,show_entry=""):
        self.window = Tk()
        self.window.title("회원 검색 결과")
        self.window.geometry(WINDOW_GEOMETRY)
        self.entry_search_user = Entry(self.window)
        self.entry_search_user.place(x=10, y=30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)
        self.entry_search_user.insert(0,show_entry)

        self.btn_search_user = Button(self.window, text="검색", command=self.event_user_search)
        self.btn_search_user.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_user = Label(self.window, text="회원 검색 결과: 0 개")
        self.label_search_user.place(x=10, y=75)

        self.btn_select_user = Button(self.window, text="선택", command=self.event_user_select)
        self.btn_select_user.place(x=400, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.btn_cancel = Button(self.window, text="취소", command=self.event_cancel)
        self.btn_cancel.place(x=500, y=360, width=SELECT_CANCEL_BTN_WIDTH)

        self.load_table()
        def clicked_table(event):
            select_Table = self.user_table.focus()
            self.getTable = self.user_table.item(select_Table).get('values')
        self.user_table.bind('<ButtonRelease-1>',clicked_table)
        if show_entry !="":
            self.event_user_search()
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
        try:
            int(index_key[0])
            condition = df_user[df_user["USER_PHONE"].str.contains(index_key)]
            count = 0
            for user_phone in condition["USER_PHONE"]:
                user_name = condition["USER_NAME"].loc[user_phone]
                user_birthday = condition["USER_BIRTH"].loc[user_phone]
                user_sex = condition["USER_SEX"].loc[user_phone]
                user_email = condition["USER_MAIL"].loc[user_phone]
                user_reg = condition["USER_REG"].loc[user_phone]
                user_add = (user_phone,user_name,user_birthday,user_sex,user_email,user_reg)
                self.user_table.insert("","end",text="",value=user_add,iid=user_add[0])
                count+=1
            self.label_search_user.config(text=f"회원 검색 결과: {count} 개")
        except:
            condition = df_user[df_user["USER_NAME"].str.contains(index_key)]
            count = 0
            for user_phone in condition["USER_PHONE"]:
                user_name = condition["USER_NAME"].loc[user_phone]
                user_birthday = condition["USER_BIRTH"].loc[user_phone]
                user_sex = condition["USER_SEX"].loc[user_phone]
                user_email = condition["USER_MAIL"].loc[user_phone]
                user_reg = condition["USER_REG"].loc[user_phone]
                user_add = (user_phone,user_name,user_birthday,user_sex,user_email,user_reg)
                self.user_table.insert("","end",text="",value=user_add,iid=user_add[0])
                count+=1
            self.label_search_user.config(text=f"회원 검색 결과: {count} 개")

    # 멤버 메소드: [선택] 버튼 이벤트
    def event_user_select(self):
        messagebox.showinfo("회원 선택", f"{self.getTable[1]}({self.getTable[0]})를 선택하였습니다.")
        self.window.quit()
        self.window.destroy()

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
        def clicked_table(event):
            select_Table = self.book_table.focus()
            self.getTable = self.book_table.item(select_Table).get('values')
        self.book_table.bind('<ButtonRelease-1>',clicked_table)
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

        self.scrollbar = Scrollbar(self.book_table, orient=HORIZONTAL)
        self.scrollbar.config()

    # 멤버 메소드: [검색] 버튼 이벤트
    def event_book_search(self):
        # 테이블 초기화
        for item in self.book_table.get_children():
            self.book_table.delete(item)
        # 중복 방지 리스트, 한꺼번에 출력 - Ex) 도서 제목과 저자의 검색어 포함이 동일한 경우
        search_isbn_list = []
        df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949')
        df_book.set_index(df_book["BOOK_ISBN"], inplace=True)
        # 도서를 Window_Add에서 추가하지 않고 csv 파일에서 직접 추가하면 불러올 때, ISBN이 실수형으로 처리되는 문제
        index_key = self.entry_search_book.get().strip().split()
        book_title_list = list(df_book["BOOK_TITLE"])
        book_author_list = list(df_book["BOOK_AUTHOR"])
        for search_word in index_key:
            for match_word in book_title_list:
                if search_word in match_word:
                    condition = df_book.loc[df_book["BOOK_TITLE"] == match_word]
                    # condition 이 ISBN 은 다르지만 동인한 책이름을 여러개 찾는다면? 
                    condition = list(condition["BOOK_ISBN"])
                    for i in condition:
                        if i in search_isbn_list:
                            continue
                        search_isbn_list.append(i)
            for match_word in book_author_list:
                if search_word in match_word:
                    condition = df_book.loc[df_book["BOOK_AUTHOR"] == match_word]
                    # condition 이 ISBN 은 다르지만 동인한 책 저자를 여러개 찾는다면? 
                    condition = list(condition["BOOK_ISBN"])
                    for i in condition:
                        if i in search_isbn_list:
                            continue
                        search_isbn_list.append(i)
            for ISBN in search_isbn_list:
                book_isbn = df_book.loc[ISBN, "BOOK_ISBN"]
                book_title = df_book.loc[ISBN, "BOOK_TITLE"]
                book_author = df_book.loc[ISBN, "BOOK_AUTHOR"]
                book_publish = df_book.loc[ISBN, "BOOK_PUB"]
                book_add = (book_isbn, book_title, book_author, book_publish)
                self.book_table.insert("","end",text="",value=book_add,iid=book_add[0])

    # 멤버 메소드: [선택] 버튼 이벤트
    def event_book_select(self):
        messagebox.showinfo("도서 선택", f"{self.getTable[1]}({self.getTable[0]})를 선택하였습니다.")
        self.window.quit()
        self.window.destroy

    # 멤버 메소드: [취소] 버튼 이벤트
    def event_cancel(self):
        self.window.quit()
        self.window.destroy()

# =========================================================