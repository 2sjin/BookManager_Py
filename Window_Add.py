from tkinter import *
from tkinter import messagebox
import pandas as pd
from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book
from PIL import Image
from PIL import Image,ImageTk

DIR_CSV_USER = "csv/user.csv"
DIR_CSV_BOOK = "csv/book.csv"
DIR_CSV_RENT = "csv/rent.csv"

# ========================================================================================================
# 클래스: 신규 회원 추가 윈도우
# ========================================================================================================
class Window_Add_User():
    
    # 생성자
    def __init__(self):
        
        self.window = Tk()
        self.window.geometry('420x220')
        self.window.title("신규 회원 추가")
        def func_exit(event):
            self.window.quit()
            self.window.destroy()
        self.user_editor = Panel_Edit_User(self.window, x=140, y=10)   # 회원 Edit 패널을 윈도우에 포함시킴
        self.user_editor.forget_regis()
        self.button_check = Button(self.window,text="확인",width=7, command=self.add_user)  # [확인] 버튼 이벤트 추가
        self.button_check.place(x=240,y=180)
        self.button_cancel = Button(self.window,text="취소",width=7)
        self.button_cancel.bind("<ButtonRelease-1>",func_exit)
        self.button_cancel.place(x=320,y=180)
        
        self.window.mainloop()
        
    # 멤버 메소드: [확인] 버튼 이벤트
    def add_user(self):
        df_user = pd.read_csv(DIR_CSV_USER, encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        user_phone = self.user_editor.get_phone()
        user_name = self.user_editor.get_name()
        user_birthday = self.user_editor.get_birthday()
        user_gender = self.user_editor.get_gender()
        user_email = self.user_editor.get_email()
        address = "sample_image/"+user_phone+".png"
        new_user = pd.DataFrame.from_dict([{ "USER_PHONE": user_phone, "USER_NAME": user_name,"USER_BIRTH": user_birthday,
        "USER_SEX": user_gender,"USER_MAIL": user_email,"USER_IMAGE": address, "USER_REG": True,"USER_RENT_CNT": 0 }])
        if len(self.user_editor.get_phone()) < 13 and self.user_editor.get_phone().count("-") < 2:
            messagebox.showinfo("전화번호 형식 오류", "□□□-□□□□-□□□□ 형식을 지켜주세요!!")
            return 0
        if user_phone in list(df_user["USER_PHONE"]):
            messagebox.showinfo("전화번호 중복", "전화번호"+user_phone+"가 중복되었습니다.")
            return 0
        if self.user_editor.get_name() =="":
            messagebox.showinfo("이름 빈공간 발생", "이름을 적어주세요!!")
            return 0
        if len(self.user_editor.get_birthday2()) < 10 and self.user_editor.get_birthday2().count("-") < 2:
            messagebox.showinfo("생일 형식 오류", "□□□□-□□-□□ 형식을 지켜주세요!!")
            return 0
        str = messagebox.askquestion("USER_ADD", user_name+"("+user_phone+")추가 하시겠습니까?")
        if str == "yes":
            try:
                self.user_editor.photo.save(address,"gif")
            except:
                image = Image.open("sample_image/Default_Image.png")
                image.save(address,"gif")
            df_user = pd.concat([df_user,new_user])
            df_user = df_user.set_index(df_user['USER_PHONE'])
            df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
            self.window.quit()
            self.window.destroy()
            
# ========================================================================================================


# ========================================================================================================
# 클래스: 신규 도서 추가 윈도우
# ========================================================================================================
class Window_Add_Book():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry('420x290')
        self.window.title("신규 도서 추가")
        def func_exit(event):
            self.window.quit()
            self.window.destroy()
        self.book_editor = Panel_Edit_Book(self.window, x=140, y=10)   # 도서 Edit 패널을 윈도우에 포함시킴
        self.button_check = Button(self.window,text="확인",width=7, command=self.add_book)  # [확인] 버튼 이벤트 추가
        self.button_check.place(x=240,y=240)
        self.button_cancel = Button(self.window,text="취소",width=7)
        self.button_cancel.bind("<ButtonRelease-1>",func_exit)
        self.button_cancel.place(x=320,y=240)
        
        self.window.mainloop()

    # 멤버 메소드: [확인] 버튼 이벤트
    def add_book(self):
        # df_book 1차 추가에서 ISBN부터 끝까지 숫자로 입력할 경우,
        # 2차 추가에서 숫자가 있는 데이터 타입을 모두 정수형으로 인식하는 문제 발생
        df_book = pd.read_csv(DIR_CSV_BOOK, encoding='CP949', dtype= {"BOOK_TITLE":object, "BOOK_AUTHOR":object, \
            "BOOK_PUB":object, "BOOK_DESCRIPTION": object, "BOOK_LINK": object})
        
        book_isbn = self.book_editor.get_isbn()
        book_title = self.book_editor.get_title()
        book_author = self.book_editor.get_author()
        book_publisher = self.book_editor.get_publisher()
        book_price = self.book_editor.get_price()
        book_link = self.book_editor.get_link()
        book_explain = self.book_editor.get_book_explain()
        book_image = "sample_image/"+book_isbn+".png"

        message = messagebox.askquestion("신규 도서 추가", "{}({})을(를) 추가하시겠습니까?".format(book_title, book_isbn))
        if message == "yes":
            if book_isbn.lstrip()=="" or book_title.lstrip()=="" or book_author.lstrip()=="" \
                or book_publisher.lstrip()=="" or book_price.lstrip()=="" or book_link.lstrip()=="" \
                or book_explain.lstrip()=="":
                messagebox.showinfo("도서 형식 오류", "도서 정보를 모두 입력해야합니다!", icon='error')
                return 0
            # ISBN 중복검사를 위한 형식검사 우선
            if not book_isbn.isdigit():
                messagebox.showinfo("ISBN 형식 오류", "ISBN은 정수 입력만 가능합니다!", icon='error')
                return 0
            if int(book_isbn) in list(df_book['BOOK_ISBN']):
                messagebox.showinfo("ISBN 중복", "ISBN {}는(은) 이미 등록된 도서입니다.".format(book_isbn), icon='error')
                return 0
            if not book_price.isdigit():
                messagebox.showinfo("가격 형식 오류", "가격은 정수 입력만 가능합니다!", icon='error')
                return 0
        elif message == 'no':
            return 0

        try:
            self.book_editor.image.save(book_image, "gif")
        except:
            messagebox.showinfo("이미지 형식 오류", "도서 이미지를 입력해야합니다!", icon='error')
            return 0

        new_book = pd.DataFrame.from_dict([{ "BOOK_ISBN": book_isbn, "BOOK_TITLE": book_title, "BOOK_AUTHOR": book_author, 
        "BOOK_PUB": book_publisher, "BOOK_PRICE": book_price,"BOOK_DESCRIPTION": book_explain, "BOOK_IMAGE": book_image, "BOOK_LINK": book_link }])

        df_book = pd.concat([df_book, new_book])
        df_book.set_index(df_book['BOOK_ISBN'], inplace=True)

        # 도서를 Window_Add에서 추가하지 않고 csv 파일에서 직접 추가하면 불러온 다음, 
        # 추가하는 데이터를 포함한 모든 ISBN이 실수형으로 처리되는 문제 발생
        
        df_book.to_csv(DIR_CSV_BOOK, index=False, encoding='CP949')
        messagebox.showinfo("새 도서 추가 완료", "ISBN {}이 등록되었습니다.".format(book_isbn))
        self.window.quit()
        self.window.destroy()

# ========================================================================================================