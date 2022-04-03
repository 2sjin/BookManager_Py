from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book
from Window_Search import Window_Search_User
from Window_Search import Window_Search_Book

SEARCH_ENTRY_WIDTH = 340
SEARCH_BTN_WIDTH = 50
SEARCH_HEIGHT = 24

BTN_WIDTH = 75

INFO_BTN_Y = 280
LABEL_FOR_TABLE_Y = 340
RENT_RETURN_BTN_Y = 500

# ======================================================================================================================
# 클래스: 회원 정보 패널
# ======================================================================================================================
class Panel_Show_User():

    # 생성자
    def __init__(self, window, x, y):
        self.user_editor = Panel_Edit_User(window, x+135, 100)      # 회원 정보 입력하는 패널 붙이기
        self.load_widgets(window, x, y)
        self.load_table(window, x, y)

    # 멤버 메소드: 멤버 속성(위젯) 정의하고 패널에 붙이기
    def load_widgets(self, window, x, y):
        self.label_for_table = Label(text="[회원 정보]")
        self.label_for_table.place(x=x, y=y)

        self.entry_search_user = Entry(window)
        self.entry_search_user.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_user = Button(window, text="검색", command=self.event_user_search)
        self.btn_search_user.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)

        self.btn_refresh_user = Button(window, text="원래대로", command=self.event_user_refresh)
        self.btn_refresh_user.place(x=x+240, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_save_user = Button(window, text="저장", command=self.event_user_save)
        self.btn_save_user.place(x=x+330, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.label_for_table = Label(text="대여중인 도서 목록")
        self.label_for_table.place(x=x, y=y+LABEL_FOR_TABLE_Y)

    # 멤버 메소드: [검색] 버튼 이벤트: 도서 검색 결과 윈도우 띄우기
    def event_user_search(self):
        Window_Search_User()

    # 멤버 메소드: 회원 정보 [원래대로] 버튼 이벤트
    def event_user_refresh(self):
        messagebox.showinfo("원래대로", "회원 정보 원래대로(이벤트 테스트)")

    # 멤버 메소드: 회원 정보 [저장] 버튼 이벤트
    def event_user_save(self):
        messagebox.showinfo("회원 정보 수정", "회원 정보 저장 완료(이벤트 테스트)")

    # 멤버 메소드: '대여 중인 도서목록' 테이블 불러오기
    def load_table(self, window, x, y):
        column_tuple = ("ISBN", "도서명", "저자")
        width_tuple = (120, 150, 135)

        self.book_table = ttk.Treeview(window, column=column_tuple, displaycolumns=column_tuple)
        self.book_table.place(x=x, y=y+LABEL_FOR_TABLE_Y+25, height=120)

        # 컬럼(헤더) 설정
        for i in range(3):
            self.book_table.column(column_tuple[i], width=width_tuple[i], anchor="center")
            self.book_table.heading(column_tuple[i], text=column_tuple[i], anchor="center")

        self.book_table["show"] = "headings"    # 열 인덱스를 표시하지 않음

        sample_value = ("9788970504773", "파이썬과 데이터 과학", "천인국, 박동규, 강영민")
        self.book_table.insert("", "end", text="", value=sample_value, iid=sample_value[0])
# ======================================================================================================================


# ======================================================================================================================
# 클래스: 도서 정보 패널
# ======================================================================================================================
class Panel_Show_Book():

    # 생성자
    def __init__(self, window, x, y):
        self.book_editor = Panel_Edit_Book(window, x+135, 100)    # 도서 정보 입력하는 패널 붙이기
        self.load_widgets(window, x, y)
        self.load_table(window, x, y)

    # 멤버 메소드: 멤버 속성(위젯) 정의하고 패널에 붙이기
    def load_widgets(self, window, x, y):
        self.label1 = Label(text="[도서 정보]")
        self.label1.place(x=x, y=y)

        self.entry_search_book = Entry(window)
        self.entry_search_book.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_book = Button(window, text="검색", command=self.event_book_search)
        self.btn_search_book.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)

        self.btn_delete_book = Button(window, text="삭제", command=self.event_book_delete)
        self.btn_delete_book.place(x=x+150, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_refresh_book = Button(window, text="원래대로", command=self.event_book_refresh)
        self.btn_refresh_book.place(x=x+240, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_save_book = Button(window, text="저장", command=self.event_book_save)
        self.btn_save_book.place(x=x+330, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_save_book = Button(window, text="대여", command=self.event_book_rent)
        self.btn_save_book.place(x=x+240, y=y+RENT_RETURN_BTN_Y, width=BTN_WIDTH)

        self.btn_save_book = Button(window, text="반납", command=self.event_book_return)
        self.btn_save_book.place(x=x+330, y=y+RENT_RETURN_BTN_Y, width=BTN_WIDTH)

        self.label_for_table = Label(text="대여 정보")
        self.label_for_table.place(x=x, y=y+LABEL_FOR_TABLE_Y)

    # 멤버 메소드: '대여 중인 도서목록' 테이블 불러오기
    def load_table(self, window, x, y):
        column_tuple = ("전화번호", "이름", "대여일", "반납예정일")
        width_tuple = (120, 85, 100, 100)

        self.book_table = ttk.Treeview(window, column=column_tuple, displaycolumns=column_tuple)
        self.book_table.place(x=x, y=y+LABEL_FOR_TABLE_Y+25, height=120)

        # 컬럼(헤더) 설정
        for i in range(4):
            self.book_table.column(column_tuple[i], width=width_tuple[i], anchor="center")
            self.book_table.heading(column_tuple[i], text=column_tuple[i], anchor="center")

        self.book_table["show"] = "headings"    # 열 인덱스를 표시하지 않음

        sample_value = ("01012345678", "홍길동", "2022-04-01", "2022-04-15")
        self.book_table.insert("", "end", text="", value=sample_value, iid=sample_value[0])

    # 멤버 메소드: [검색] 버튼 이벤트: 도서 검색 결과 윈도우 띄우기
    def event_book_search(self):
        Window_Search_Book()

    # 멤버 메소드: 도서 정보 [삭제] 버튼 이벤트
    def event_book_delete(self):
        messagebox.showinfo("도서 삭제", "도서 삭제 완료(이벤트 테스트)")

    # 멤버 메소드: 도서 정보 [원래대로] 버튼 이벤트
    def event_book_refresh(self):
        messagebox.showinfo("원래대로", "도서 정보 원래대로(이벤트 테스트)")

    # 멤버 메소드: 도서 정보 [저장] 버튼 이벤트
    def event_book_save(self):
        messagebox.showinfo("도서 정보 수정", "도서 정보 수정 완료(이벤트 테스트)")

    # 멤버 메소드: 도서 [대여] 버튼 이벤트
    def event_book_rent(self):
        messagebox.showinfo("도서 대여", "도서 대여 완료(이벤트 테스트)")

    # 멤버 메소드: 도서 [반납] 버튼 이벤트
    def event_book_return(self):
        messagebox.showinfo("도서 반납", "도서 반납 완료(이벤트 테스트)")

# ======================================================================================================================