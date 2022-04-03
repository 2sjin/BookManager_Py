from tkinter import *
from tkinter import ttk

WINDOW_GEOMETRY = '595x400'

SEARCH_ENTRY_WIDTH = 460
SEARCH_BUTTON_WIDTH = 100
SEARCH_HEIGHT = 24

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

        self.btn_search_user = Button(self.window, text="검색")
        self.btn_search_user.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BUTTON_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_user = Label(self.window, text="회원 검색 결과: 2 개")
        self.label_search_user.place(x=10, y=75)

        self.btn_search_user = Button(self.window, text="선택", width=10)
        self.btn_search_user.place(x=400, y=360)

        self.btn_search_user = Button(self.window, text="취소", width=10)
        self.btn_search_user.place(x=500, y=360)

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

        self.btn_search_book = Button(self.window, text="검색")
        self.btn_search_book.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BUTTON_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_book = Label(self.window, text="도서 검색 결과: 2 개")
        self.label_search_book.place(x=10, y=75)

        self.btn_search_book = Button(self.window, text="선택", width=10)
        self.btn_search_book.place(x=400, y=360)

        self.btn_search_book = Button(self.window, text="취소", width=10)
        self.btn_search_book.place(x=500, y=360)

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
# =========================================================