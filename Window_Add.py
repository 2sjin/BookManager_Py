from tkinter import *
from tkinter import messagebox
from urllib.parse import uses_fragment
import pandas as pd
from Panel_Edit import Panel_Edit_User
from Panel_Edit import Panel_Edit_Book

DIR_CSV_USER = "csv/USER.csv"
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
        new_user = pd.DataFrame.from_dict([{ "USER_PHONE": user_phone, "USER_NAME": user_name,"USER_BIRTH": user_birthday,
        "USER_SEX": user_gender,"USER_MAIL": user_email,"USER_IMAGE": "1", "USER_REG": True,"USER_RENT_CNT": 0 }])
        df_user = pd.concat([df_user,new_user])
        df_user = df_user.set_index(df_user['USER_PHONE'])
        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
# ========================================================================================================


# ========================================================================================================
# 클래스: 신규 도서 추가 윈도우
# ========================================================================================================
class Window_Add_Book():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.geometry('420x230')
        self.window.title("신규 도서 추가")
        def func_exit(event):
            self.window.quit()
            self.window.destroy()
        self.book_editor = Panel_Edit_Book(self.window, x=140, y=10)   # 도서 Edit 패널을 윈도우에 포함시킴
        self.button_check = Button(self.window,text="확인",width=7, command=self.add_book)  # [확인] 버튼 이벤트 추가
        self.button_check.place(x=240,y=195)
        self.button_cancel = Button(self.window,text="취소",width=7)
        self.button_cancel.bind("<ButtonRelease-1>",func_exit)
        self.button_cancel.place(x=320,y=195)
        
        self.window.mainloop()

    # 멤버 메소드: [확인] 버튼 이벤트
    def add_book(self):
        messagebox.showinfo("신규 도서 추가", "신규 도서 추가 완료(이벤트 테스트)")
          
# ========================================================================================================