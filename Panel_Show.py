from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pandas as pd
from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book
from Window_Search import Window_Search_User
from Window_Search import Window_Search_Book
from PIL import Image
import os
from PIL import Image,ImageTk
from os import remove
SEARCH_ENTRY_WIDTH = 340
SEARCH_BTN_WIDTH = 50
SEARCH_HEIGHT = 24

BTN_WIDTH = 75

IMG_WIDTH = 120
IMG_HEIGHT = 160

INFO_BTN_Y = 315
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

        self.label_for_table = Label(text="전체 조회: 입력 없이 [검색] 클릭", font=("맑은 고딕", 8), fg="red")
        self.label_for_table.place(x=x+238, y=y)

        self.entry_search_user = Entry(window)
        self.entry_search_user.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_user = Button(window, text="검색", command=self.event_user_search)
        self.btn_search_user.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)

        self.btn_refresh_user = Button(window, text="원래대로", command=self.event_user_refresh)
        self.btn_refresh_user.place(x=x+240, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_save_user = None
#        self.btn_save_user = Button(window, text="수정", command=self.event_user_save)
#        self.btn_save_user.place(x=x+330, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.label_for_table = Label(text="대여중인 도서 목록")
        self.label_for_table.place(x=x, y=y+LABEL_FOR_TABLE_Y)

    # 멤버 메소드: [검색] 버튼 이벤트: 회원 검색 결과 윈도우 띄우기
    def event_user_search(self):
        self.Search = Window_Search_User(self.entry_search_user.get())

        # 취소 버튼 눌렀을 때 이벤트
        if self.Search.cancel == True:
            return None

        self.entry_search_user.delete("0","end")
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
        self.rent_count = select_user["USER_RENT_CNT"].loc[self.phone]
        self.select_address = select_user["USER_IMAGE"].loc[self.phone]
        self.photo = Image.open(self.select_address)
        resize_photo = self.photo.resize((IMG_WIDTH, IMG_HEIGHT))
        self.photo_tk = ImageTk.PhotoImage(resize_photo)
        self.user_editor.label_image.configure(image=self.photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.user_editor.label_image.image = self.photo_tk
        self.update_table()     # 대여 중인 도서 목록 새로고침
        
        

    # 멤버 메소드: 회원 정보 [원래대로] 버튼 이벤트
    def event_user_refresh(self):
        try:
            df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            select_user = df_user.loc[df_user['USER_PHONE']==self.phone]
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
            self.select_address = select_user["USER_IMAGE"].loc[self.phone]
            self.photo = Image.open(self.select_address)
            resize_photo = self.photo.resize((IMG_WIDTH, IMG_HEIGHT))
            self.photo_tk = ImageTk.PhotoImage(resize_photo)
            self.user_editor.label_image.configure(image=self.photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
            self.user_editor.label_image.image = self.photo_tk

            self.update_table()     # 대여 중인 도서 목록 새로고침

            # messagebox.showinfo("원래대로", "회원 정보가 원상복구되었습니다.")
        except:
            pass

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

        # 이미지 출력
        self.select_address = select_user["USER_IMAGE"].loc[self.phone]
        self.photo = Image.open(self.select_address)
        resize_photo = self.photo.resize((IMG_WIDTH, IMG_HEIGHT))
        self.photo_tk = ImageTk.PhotoImage(resize_photo)
        self.user_editor.label_image.configure(image=self.photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
        self.user_editor.label_image.image = self.photo_tk

        self.update_table()     # 대여 중인 도서 목록 새로고침

    # 멤버 메소드: 회원 정보 [수정] 버튼 이벤트
    def event_user_save(self):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        user_phone = df_user["USER_PHONE"].tolist()
        df_user["USER_PHONE"].loc[self.phone] = self.user_editor.get_phone()
        df_user["USER_NAME"].loc[self.phone] = self.user_editor.get_name()
        df_user["USER_BIRTH"].loc[self.phone] = self.user_editor.get_birthday()
        df_user["USER_SEX"].loc[self.phone] = self.user_editor.get_gender()
        df_user["USER_MAIL"].loc[self.phone] = self.user_editor.get_email()
        df_user["USER_REG"].loc[self.phone] = self.user_editor.get_REG()
        user_phone.remove(self.phone)

        df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)
        df_rent.index.name = "RENT_SEQ"     # Auto Increment를 인덱스로 하며, 별칭 설정

        # 해당 회원의 도서 대여 이력 중 '대여 중'에 해당하는 이력만 추출
        condition_filter_isbn = df_rent["USER_PHONE"] == self.phone
        condition_filter_rented = df_rent["RENT_RETURN_DATE"] == -1
        df_rent_rented = df_rent[["USER_PHONE"]][condition_filter_isbn & condition_filter_rented]

        if not df_rent_rented.empty and (self.phone != self.user_editor.get_phone()):
            messagebox.showerror("전화번호 수정 오류", "대여 중인 도서가 있는 회원은 전화번호를 수정할 수 없습니다.", icon='error')
            return -4

        if self.rent_count > 0 and (self.user_editor.get_REG() == False):    # 라디오버튼 '탈퇴'에 체크할 경우에만 조건 확인
            messagebox.showinfo("반납 오류", "반납을 모두 완료하시고 탈퇴를 진행하세요!")
            return 0
        if len(self.user_editor.get_phone()) < 13 and self.user_editor.get_phone().count("-") < 2:
            messagebox.showinfo("전화번호 형식 오류", "□□□-□□□□-□□□□ 형식을 지켜주세요!!")
            return 0
        if self.user_editor.get_phone() in user_phone:
            messagebox.showinfo("전화번호 중복", "전화번호"+self.user_editor.get_phone()+"가 중복되었습니다.")
            return 0
        if self.user_editor.get_name() =="":
            messagebox.showinfo("이름 빈공간 발생", "이름을 적어주세요!!")
            return 0
        if len(self.user_editor.get_birthday2()) < 10 and self.user_editor.get_birthday2().count("-") < 2:
            messagebox.showinfo("생일 형식 오류", "□□□□-□□-□□ 형식을 지켜주세요!!")
            return 0
        count = self.user_editor.return_count()
        address = "sample_image/"+self.user_editor.get_phone()+".png"
        if count == 0 :
            self.photo.save(address,"png")
        else:
            self.photo = self.user_editor.return_photo()
            self.photo.save(address,"png")
        # 이미지 파일 저장("전화번호.png")
        df_user["USER_IMAGE"].loc[self.phone] = address
        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
     # 수정한 회원 정보를 임시 변수에 저장([수정] 후 [원래대로] 버튼을 눌렀을 때 수정한 정보 반영하기 위함)
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        self.phone = self.user_editor.get_phone()
        self.name = df_user["USER_NAME"].loc[self.phone]
        self.birthday = df_user["USER_BIRTH"].loc[self.phone]
        self.birthday = str(self.birthday)
        self.birthday = self.birthday[:4]+"-"+self.birthday[4:6]+"-"+self.birthday[6:]
        self.gender = df_user["USER_SEX"].loc[self.phone]
        self.email = df_user["USER_MAIL"].loc[self.phone]
        self.REG = df_user["USER_REG"].loc[self.phone]
        self.rent_count = df_user["USER_RENT_CNT"].loc[self.phone]
        address = "sample_image/"+self.phone+".png"
        self.user_editor.image_button = 0
        messagebox.showinfo("회원 정보 수정", "회원 정보가 수정되었습니다.")

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

        self.label_for_table = Label(text="전체 조회: 입력 없이 [검색] 클릭", font=("맑은 고딕", 8), fg="red")
        self.label_for_table.place(x=x+238, y=y)

        self.entry_search_book = Entry(window)
        self.entry_search_book.place(x=x, y=y+30, width=SEARCH_ENTRY_WIDTH, height=SEARCH_HEIGHT)

        self.btn_search_book = Button(window, text="검색", command=self.event_book_search)
        self.btn_search_book.place(x=x+SEARCH_ENTRY_WIDTH+10, y=y+30, width=SEARCH_BTN_WIDTH, height=SEARCH_HEIGHT)

        self.btn_delete_book = Button(window, text="삭제", command=self.event_book_delete)
        self.btn_delete_book.place(x=x+150, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_refresh_book = Button(window, text="원래대로", command=self.event_book_refresh)
        self.btn_refresh_book.place(x=x+240, y=y+INFO_BTN_Y, width=BTN_WIDTH)

        self.btn_save_book = None
        # self.btn_save_book = Button(window, text="수정", command=self.event_book_save)
        # self.btn_save_book.place(x=x+330, y=y+INFO_BTN_Y, width=BTN_WIDTH)

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
            book_isbn = int(self.get_isbn())
        except:
            return 0

        # 선택한 도서의 최근 대여 이력 가져오기
        try:    
            rent_seq = max(df_rent[df_rent["BOOK_ISBN"] == book_isbn].index)
        except ValueError:
            return 0

        try:
            user_phone = df_rent["USER_PHONE"].loc[rent_seq]
            user_name = df_user["USER_NAME"].loc[user_phone]
            rent_date = df_rent["RENT_DATE"].loc[rent_seq]
            rent_due_date = df_rent["RENT_DUE_DATE"].loc[rent_seq]
        except KeyError:
            return 0

        # 대여 중인 도서이면 테이블에 레코드 추가
        if df_rent["RENT_RETURN_DATE"].loc[rent_seq] == -1:
            add_value = (user_phone, user_name, rent_date, rent_due_date)
            self.book_table.insert("", "end", text="", value=add_value, iid=add_value[0])



    # 멤버 메소드: [검색] 버튼 이벤트: 도서 검색 결과 윈도우 띄우기
    def event_book_search(self):
        try:
            self.Search = Window_Search_Book(self.entry_search_book.get())

            # 취소 버튼 눌렀을 때 이벤트
            if self.Search.cancel == True:
                return None

            # self.isbn = int 타입
            self.isbn = self.Search.getTable[0]
            df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949')
            df_book.set_index(df_book["BOOK_ISBN"], inplace=True)

            # entry 내용 삭제
            self.book_editor.entry_isbn.delete("0","end")
            self.book_editor.entry_title.delete("0","end")
            self.book_editor.entry_author.delete("0","end")
            self.book_editor.entry_publisher.delete("0","end")
            self.book_editor.entry_price.delete("0","end")
            self.book_editor.entry_link.delete("1.0","end")
            self.book_editor.entry_book_explain.delete("1.0", "end")

            # 도서 정보 검색
            self.title = df_book.loc[self.isbn, "BOOK_TITLE"]
            self.author = df_book.loc[self.isbn, "BOOK_AUTHOR"]
            self.publisher = df_book.loc[self.isbn, "BOOK_PUB"]
            self.price = df_book.loc[self.isbn, "BOOK_PRICE"]
            self.image_address = df_book.loc[self.isbn, "BOOK_IMAGE"]
            self.link = df_book.loc[self.isbn, "BOOK_LINK"]
            self.book_explain = df_book.loc[self.isbn, "BOOK_DESCRIPTION"]

            # 도서 이미지 찾기, 조절
            image = Image.open(self.image_address)
            reisze_image = image.resize((IMG_WIDTH, IMG_HEIGHT))
            self.image_tk = ImageTk.PhotoImage(reisze_image)

            # 도서 정보 출력
            self.book_editor.entry_isbn.insert("0",self.isbn)
            self.book_editor.entry_title.insert("0",self.title)
            self.book_editor.entry_author.insert("0",self.author)
            self.book_editor.entry_publisher.insert("0",self.publisher)
            self.book_editor.entry_price.insert("0",self.price)
            self.book_editor.entry_link.insert("1.0",self.link)
            self.book_editor.entry_book_explain.insert("1.0",self.book_explain)
            self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
            self.book_editor.label_image.image = self.image_tk
            self.update_table()
        except:
            pass

    # 멤버 메소드: 도서 정보 [삭제] 버튼 이벤트
    def event_book_delete(self):
        
        df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949', dtype= {"BOOK_TITLE":object, "BOOK_AUTHOR":object, \
            "BOOK_PUB":object, "BOOK_DESCRIPTION": object, "BOOK_LINK": object})
        df_book.set_index(df_book["BOOK_ISBN"], inplace=True)

        df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)
        df_rent.index.name = "RENT_SEQ"     # Auto Increment를 인덱스로 하며, 별칭 설정

        # self.isbn 값 없을 시 return 0
        # 삭제를 한 경우 또 삭제를 할 때,
        try:
            if self.isbn == "":
                messagebox.showinfo("도서 정보 삭제 오류", "도서 정보를 먼저 검색해주세요!", icon='error')
                return 0
            condition1 = df_rent["BOOK_ISBN"] == self.isbn
            condition2 = df_rent["RENT_RETURN_DATE"] == -1
            df_temp = df_rent[condition1 & condition2]
        except:
            messagebox.showinfo("도서 정보 삭제 오류", "도서 정보를 먼저 검색해주세요!", icon='error')
            return 0


        if -1 in list(df_temp["RENT_RETURN_DATE"]):
            messagebox.showinfo("도서 정보 삭제 불가", f"- 이미 대출 중인 도서 입니다.\n- {self.title}({self.isbn})를 먼저 반납해주세요!", icon='error')
            return 0
        df_book = df_book.drop(self.isbn)
        self.isbn = ""
        
        df_book.to_csv(DIR_CSV_BOOK, index=False, encoding='CP949')

        messagebox.showinfo("도서 정보 삭제 완료", "도서 정보를 삭제하였습니다.")

        # entry 내용 삭제
        self.book_editor.entry_isbn.delete("0","end")
        self.book_editor.entry_title.delete("0","end")
        self.book_editor.entry_author.delete("0","end")
        self.book_editor.entry_publisher.delete("0","end")
        self.book_editor.entry_price.delete("0","end")
        self.book_editor.entry_link.delete("1.0","end")
        self.book_editor.entry_book_explain.delete("1.0","end")
        self.book_editor.label_image.place_forget()

    # 멤버 메소드: 도서 정보 [원래대로] 버튼 이벤트
    def event_book_refresh(self):

        # entry 내용 삭제
        self.book_editor.entry_isbn.delete("0","end")
        self.book_editor.entry_title.delete("0","end")
        self.book_editor.entry_author.delete("0","end")
        self.book_editor.entry_publisher.delete("0","end")
        self.book_editor.entry_price.delete("0","end")
        self.book_editor.entry_link.delete("1.0","end")
        self.book_editor.entry_book_explain.delete("1.0","end")

        # 도서 정보 출력
        # 아무 검색 하지않고 원래대로 버튼 클릭시 오류 수정
        try:
            self.book_editor.entry_isbn.insert("0", self.isbn)
            self.book_editor.entry_title.insert("0",self.title)
            self.book_editor.entry_author.insert("0",self.author)
            self.book_editor.entry_publisher.insert("0",self.publisher)
            self.book_editor.entry_price.insert("0",self.price)
            self.book_editor.entry_link.insert("1.0",self.link)
            self.book_editor.entry_book_explain.insert("1.0",self.book_explain)
            self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
            self.book_editor.label_image.image = self.image_tk
            self.update_table()
        except:
            return 0

    # 멤버 메소드: 도서 정보 [수정] 버튼 이벤트
    def event_book_save(self):
        try:
            if self.isbn == "":
                messagebox.showinfo("도서 정보 수정 오류", "도서 정보를 먼저 검색해주세요!", icon='error')
                return 0
        except:
            messagebox.showinfo("도서 정보 수정 오류", "도서 정보를 먼저 검색해주세요!", icon='error')
            return 0
        df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949', dtype= {"BOOK_TITLE":object, "BOOK_AUTHOR":object, \
            "BOOK_PUB":object, "BOOK_DESCRIPTION": object, "BOOK_LINK": object})

        df_rent = pd.read_csv(DIR_CSV_RENT, encoding='CP949', index_col=0)
        df_rent.index.name = "RENT_SEQ"     # Auto Increment를 인덱스로 하며, 별칭 설정


        # SettingWithCopyWarning 무시
        pd.set_option('mode.chained_assignment',  None)

        ISBN = self.book_editor.get_isbn()
        book_title = self.book_editor.get_title()
        book_author = self.book_editor.get_author()
        book_publisher = self.book_editor.get_publisher()
        book_price = self.book_editor.get_price()
        book_link = self.book_editor.get_link()
        book_explain = self.book_editor.get_book_explain()
        book_image_address = "sample_image/"+ISBN+".png"


        # 해당 도서의 대여 이력 중 '대여 중'에 해당하는 이력만 추출
        condition_filter_isbn = df_rent["BOOK_ISBN"] == self.isbn
        condition_filter_rented = df_rent["RENT_RETURN_DATE"] == -1
        df_rent_rented = df_rent[["BOOK_ISBN"]][condition_filter_isbn & condition_filter_rented]

        if not df_rent_rented.empty and (int(self.isbn) != int(self.book_editor.get_isbn())):
            messagebox.showerror("ISBN 수정 오류", "대여 중인 도서는 ISBN을 수정할 수 없습니다.", icon='error')
            return -4

        message = messagebox.askquestion("도서 수정", "{}({})을(를) 수정하시겠습니까?".format(book_title, ISBN))
        if message == "yes":
            # 공백이 있는지부터 확인
            if ISBN.lstrip()=="" or book_title.lstrip()=="" or book_author.lstrip()=="" \
                or book_publisher.lstrip()=="" or book_price.lstrip()=="" or book_link.lstrip()=="" \
                or book_explain.lstrip()=="":
                messagebox.showinfo("도서 형식 오류", "도서 정보를 모두 입력해야합니다!", icon='error')
                return 0

            # ISBN 형식 오류부터 검사해야 중복 검사에서 ISBN을 정수형으로 변환 가능
            if not ISBN.isdigit():
                messagebox.showinfo("ISBN 형식 오류", "ISBN은 정수 입력만 가능합니다!", icon='error')
                return 0

            if self.isbn != int(ISBN):
                if int(ISBN) in list(df_book["BOOK_ISBN"]):
                    messagebox.showinfo("ISBN 중복", "ISBN {}는(은) 이미 등록된 도서입니다.".format(ISBN), icon='error')
                    return 0

            if not book_price.isdigit():
                messagebox.showinfo("가격 형식 오류", "가격은 정수 입력만 가능합니다!", icon='error')
                return 0
        elif message == 'no':
            return 0

        if self.isbn == int(ISBN):
            # (덮어쓰기)
            try:
                self.book_editor.image.save(book_image_address, "gif")
                image = Image.open(book_image_address)    
                resize_image = image.resize((IMG_WIDTH, IMG_HEIGHT))
                self.image_tk = ImageTk.PhotoImage(resize_image)
                self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
                self.book_editor.label_image.image = self.image_tk
            # (ISBN 과 파일 변경이 동일한 경우)            
            except:
                # 파일 ISBN, 사진 그대로 저장
                image = Image.open(self.image_address)
                image.save(book_image_address, "gif") # (덮어쓰기)
                reisze_image = image.resize((IMG_WIDTH, IMG_HEIGHT))
                self.image_tk = ImageTk.PhotoImage(reisze_image)
                self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
                self.book_editor.label_image.image = self.image_tk
        else:
            try:
                # ISBN, 파일 모두 변경
                self.book_editor.image.save(book_image_address, "gif")
                image = Image.open(book_image_address)
                # 만약 ISBN이 이전과 다르면 새로운 이름을 가진 파일이 추가되었을거임.
                resize_image = image.resize((IMG_WIDTH, IMG_HEIGHT))
                # 이미지 -> 원래대로를 위한 변경
                self.image_tk = ImageTk.PhotoImage(resize_image)
                self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
                self.book_editor.label_image.image = self.image_tk
                remove(self.image_address)
            except:
                image = Image.open(self.image_address)     
                image.save(book_image_address, "gif")
                image = Image.open(book_image_address)
                reisze_image = image.resize((IMG_WIDTH, IMG_HEIGHT))
                self.image_tk = ImageTk.PhotoImage(reisze_image)
                self.book_editor.label_image.configure(image=self.image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
                self.book_editor.label_image.image = self.image_tk
                remove(self.image_address)

        ISBN = int(ISBN)
        book_price = int(book_price)

        df_book[df_book["BOOK_ISBN"] == self.isbn] = ISBN
        df_book.set_index(df_book["BOOK_ISBN"], inplace=True)
        df_book.loc[ISBN, "BOOK_ISBN"] = ISBN
        df_book.loc[ISBN, "BOOK_TITLE"] = book_title
        df_book.loc[ISBN, "BOOK_AUTHOR"] = book_author
        df_book.loc[ISBN, "BOOK_PUB"] = book_publisher
        df_book.loc[ISBN, "BOOK_PRICE"] = book_price
        df_book.loc[ISBN, "BOOK_DESCRIPTION"] = book_explain
        df_book.loc[ISBN, "BOOK_IMAGE"] = book_image_address
        df_book.loc[ISBN, "BOOK_LINK"] = book_link

        df_book.to_csv(DIR_CSV_BOOK, index=False, encoding='CP949')
        
        # 저장 -> 원래대로
        self.isbn = ISBN
        self.title = book_title
        self.author = book_author
        self.publisher = book_publisher
        self.price = book_price
        self.book_explain = book_explain
        self.link = book_link
        self.image_address = book_image_address

        messagebox.showinfo("도서 수정 완료", "도서 정보를 수정하였습니다.")

    # 멤버 메소드: ISBN 리턴
    def get_isbn(self):
        return self.book_editor.get_isbn()

# ======================================================================================================================
