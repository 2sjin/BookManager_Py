from tkinter import *
from tkinter import ttk

SEARCH_ENTRY_WIDTH = 400
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
        self.window.geometry('595x400')

        self.entry_search_user = Entry(self.window)
        self.entry_search_user.place(x=10, y=30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_user = Button(self.window, text="검색")
        self.btn_search_user.place(x=SEARCH_ENTRY_WIDTH+20, y=30, width=SEARCH_BUTTON_WIDTH, height=SEARCH_HEIGHT)
        
        self.label_search_user = Label(self.window, text="회원 검색 결과")
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

        sample_value = ("01025773617", "이승진", "1997-06-18", "남", "options3224@naver.com", True)
        self.user_table.insert("", "end", text="", value=sample_value, iid=0)

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
        self.window.geometry('500x400')

        self.label = Label(self.window, text="도서 검색 결과")
        self.label.pack()

        self.window.mainloop()
# =========================================================