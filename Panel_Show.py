from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pandas as pd

from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book
from Window_Search import Window_Search_User
from Window_Search import Window_Search_Book
from PIL import Image
from PIL import Image,ImageTk
SEARCH_ENTRY_WIDTH = 340
SEARCH_BTN_WIDTH = 50
SEARCH_HEIGHT = 24

BTN_WIDTH = 75

IMG_WIDTH = 120
IMG_HEIGHT = 160

INFO_BTN_Y = 280
LABEL_FOR_TABLE_Y = 340

DIR_CSV_USER = "csv/user.csv"
DIR_CSV_BOOK = "csv/book.csv"
DIR_CSV_RENT = "csv/rent.csv"

# 전역 함수: 데이터프레임 불러오기
def load_dataframes():
    # csv 파일에서 데이터프레임 불러오기
    df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
    df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949')
    df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)

    # 데이터프레임 인덱스 설정
    df_user = df_user.set_index(df_user['USER_PHONE'])  # 전화번호를 인덱스로 설정
    df_book = df_book.set_index(df_book['BOOK_ISBN'])   # ISBN을 인덱스로 설정
    df_rent.index.name = "RENT_SEQ"     # Auto Increment를 인덱스로 하며, 별칭 설정

    return df_user, df_book, df_rent


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
        self.Search = Window_Search_User()
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        self.phone = self.Search.getTable[0]
        # 행 찾기
        select_user = df_user.loc[df_user['USER_PHONE']==self.phone]
        # entry 내용 삭제
        self.user_editor.entry_name.delete("0","end")
        self.user_editor.entry_phone.delete("0","end")
        self.user_editor.entry_birthday.delete("0","end")
        self.user_editor.entry_email.delete("0","end")
        # 찾은 행 값 삽입하기
        self.user_editor.entry_phone.insert(0,self.phone)
        self.name = select_user["USER_NAME"].loc[self.phone]
        self.user_editor.entry_name.insert(0,self.name)
        self.birthday = str(select_user["USER_BIRTH"].loc[self.phone])
        self.birthday = self.birthday[:4]+"-"+self.birthday[4:6]+"-"+self.birthday[6:]
        self.user_editor.entry_birthday.insert(0,self.birthday)
        self.gender = select_user["USER_SEX"].loc[self.phone]
        if self.gender=="남":
            self.user_editor.gender_rb1.select()
        else:
            self.user_editor.gender_rb2.select()
        self.email = select_user["USER_MAIL"].loc[self.phone]
        self.user_editor.entry_email.insert(0,self.email)
        self.REG = select_user["USER_REG"].loc[self.phone]
        if self.REG:
            self.user_editor.registration_rb1.select()
        else:
            self.user_editor.registration_rb2.select()
            
        self.select_address = select_user["USER_IMAGE"].loc[self.phone]
        self.photo = Image.open(self.select_address)
        resize_photo = self.photo.resize((IMG_WIDTH, IMG_HEIGHT))
        self.photo_tk = ImageTk.PhotoImage(resize_photo)
        self.user_editor.label_image.configure(image=self.photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.user_editor.label_image.image = self.photo_tk
        self.update_table()     # 대여 중인 도서 목록 새로고침
        

    # 멤버 메소드: 회원 정보 [원래대로] 버튼 이벤트
    def event_user_refresh(self):
        self.user_editor.entry_name.delete("0","end")
        self.user_editor.entry_phone.delete("0","end")
        self.user_editor.entry_birthday.delete("0","end")
        self.user_editor.entry_email.delete("0","end")
        self.user_editor.entry_phone.insert(0,self.phone)
        self.user_editor.entry_name.insert(0,self.name)
        self.user_editor.entry_birthday.insert(0,self.birthday)
        if self.gender=="남":
            self.user_editor.gender_rb1.select()
        else:
            self.user_editor.gender_rb2.select()
        self.user_editor.entry_email.insert(0,self.email)
        if self.REG:
            self.user_editor.registration_rb1.select()
        else:
            self.user_editor.registration_rb2.select()
            
        self.user_editor.label_image.configure(image=self.photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.user_editor.label_image.image = self.photo_tk

        self.update_table()     # 대여 중인 도서 목록 새로고침

        messagebox.showinfo("원래대로", "회원 정보가 원상복구되었습니다.")

    # 멤버 메소드: 도서 반납 시 회원 정보 패널에 대여자(반납자)의 정보 출력
    def event_show_return_user(self, return_user_phone):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        self.phone = return_user_phone
        # 행 찾기
        select_user = df_user.loc[df_user['USER_PHONE']==self.phone]
        # entry 내용 삭제
        self.user_editor.entry_name.delete("0","end")
        self.user_editor.entry_phone.delete("0","end")
        self.user_editor.entry_birthday.delete("0","end")
        self.user_editor.entry_email.delete("0","end")
        # 찾은 행 값 삽입하기
        self.user_editor.entry_phone.insert(0,self.phone)
        self.name = select_user["USER_NAME"].loc[self.phone]
        self.user_editor.entry_name.insert(0,self.name)
        self.birthday = str(select_user["USER_BIRTH"].loc[self.phone])
        self.birthday = self.birthday[:4]+"-"+self.birthday[4:6]+"-"+self.birthday[6:]
        self.user_editor.entry_birthday.insert(0,self.birthday)
        self.gender = select_user["USER_SEX"].loc[self.phone]
        if self.gender=="남":
            self.user_editor.gender_rb1.select()
        else:
            self.user_editor.gender_rb2.select()
        self.email = select_user["USER_MAIL"].loc[self.phone]
        self.user_editor.entry_email.insert(0,self.email)
        self.REG = select_user["USER_REG"].loc[self.phone]
        if self.REG:
            self.user_editor.registration_rb1.select()
        else:
            self.user_editor.registration_rb2.select()
        self.update_table()     # 대여 중인 도서 목록 새로고침

    # 멤버 메소드: 회원 정보 [저장] 버튼 이벤트
    def event_user_save(self):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        df_user["USER_PHONE"].loc[self.phone] = self.user_editor.get_phone()
        df_user["USER_NAME"].loc[self.phone] = self.user_editor.get_name()
        df_user["USER_BIRTH"].loc[self.phone] = self.user_editor.get_birthday()
        df_user["USER_SEX"].loc[self.phone] = self.user_editor.get_gender()
        df_user["USER_MAIL"].loc[self.phone] = self.user_editor.get_email()
        address = "sample_image/"+self.phone+".gif"
        self.user_editor.photo.save(address,"gif")
        df_user["USER_IMAGE"].loc[self.phone] = address
        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')

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

        # 열 인덱스를 표시하지 않음
        self.book_table["show"] = "headings"

        # 테이블 갱신
        self.update_table()

    # 멤버 메소드: '대여 정보' 테이블 갱신
    def update_table(self):
        # 테이블 초기화
        for item in self.book_table.get_children():
            self.book_table.delete(item)

        # 데이터프레임 불러오기
        __dummy__, df_book, df_rent = load_dataframes()

        # 선택한 회원의 전화번호 가져오기
        try:
            user_phone = self.get_phone()
        except ValueError:
            return 0

        # 선택한 회원에 대한 대여 이력 필터링
        condition1 = df_rent["USER_PHONE"] == user_phone
        condition2 = df_rent["RENT_RETURN_DATE"] == -1
        df_temp = df_rent[condition1 & condition2] 

        # 테이블에 레코드 추가
        for book_isbn in df_temp["BOOK_ISBN"]:
            book_title = df_book["BOOK_TITLE"].loc[book_isbn]
            book_author = df_book["BOOK_AUTHOR"].loc[book_isbn]
            add_value = (book_isbn, book_title, book_author)
            self.book_table.insert("", "end", text="", value=add_value, iid=add_value[0])

    # 멤버 메소드: 전화번호 리턴
    def get_phone(self):
        return self.user_editor.get_phone()

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

        self.label_for_table = Label(text="대여 정보")
        self.label_for_table.place(x=x, y=y+LABEL_FOR_TABLE_Y)

    # 멤버 메소드: '대여 정보' 테이블 불러오기
    def load_table(self, window, x, y):
        column_tuple = ("전화번호", "이름", "대여일", "반납예정일")
        width_tuple = (120, 85, 100, 100)

        self.book_table = ttk.Treeview(window, column=column_tuple, displaycolumns=column_tuple)
        self.book_table.place(x=x, y=y+LABEL_FOR_TABLE_Y+25, height=120)

        # 컬럼(헤더) 설정
        for i in range(4):
            self.book_table.column(column_tuple[i], width=width_tuple[i], anchor="center")
            self.book_table.heading(column_tuple[i], text=column_tuple[i], anchor="center")

        # 열 인덱스를 표시하지 않음
        self.book_table["show"] = "headings"

        # 테이블 갱신
        self.update_table()


    # 멤버 메소드: '대여 정보' 테이블 갱신
    def update_table(self):
        # 테이블 초기화
        for item in self.book_table.get_children():
            self.book_table.delete(item)

        # 데이터프레임 불러오기
        df_user, __dummy__, df_rent = load_dataframes()

        # 선택한 도서의 ISBN 가져오기
        try:
            book_isbn = self.get_isbn()
        except ValueError:
            return 0

        # 선택한 도서의 최근 대여 이력 가져오기
        rent_seq = max(df_rent[df_rent["BOOK_ISBN"] == book_isbn].index)
        user_phone = df_rent["USER_PHONE"].loc[rent_seq]
        user_name = df_user["USER_NAME"].loc[user_phone]
        rent_date = df_rent["RENT_DATE"].loc[rent_seq]
        rent_due_date = df_rent["RENT_DUE_DATE"].loc[rent_seq]

        # 대여 중인 도서이면 테이블에 레코드 추가
        if df_rent["RENT_RETURN_DATE"].loc[rent_seq] == -1:
            add_value = (user_phone, user_name, rent_date, rent_due_date)
            self.book_table.insert("", "end", text="", value=add_value, iid=add_value[0])


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
   
    # 멤버 메소드: ISBN 리턴
    def get_isbn(self):
        return self.book_editor.get_isbn()

# ======================================================================================================================
