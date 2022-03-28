from tkinter import *


# =======================================================================================
# 클래스: 회원을 추가하거나 수정할 때, 회원 정보 및 이미지를 입력하는 위젯을 모아놓은 패널
# =======================================================================================
class Panel_Edit_User():

    # 생성자
    def __init__(self, window, x, y):
        self.label_phone = Label(window, text="전화번호")        
        self.label_phone.place(x=x, y=y)

        self.label_name = Label(window, text="이름")
        self.label_name.place(x=x, y=y+20)

        self.entry_phone = Entry(window)
        self.entry_phone.place(x=x+60, y=y)

        self.entry_name = Entry(window)
        self.entry_name.place(x=x+60, y=y+20)
# =======================================================================================


# =======================================================================================
# 클래스: 도서를 추가하거나 수정할 때, 도서 정보 및 이미지를 입력하는 위젯을 모아놓은 패널
# =======================================================================================
class Panel_Edit_Book():

    # 생성자
    def __init__(self, window, x, y):

        self.label_isbn = Label(window, text="ISBN")
        self.label_isbn.place(x=x, y=y)

        self.label_title = Label(window, text="도서명")
        self.label_title.place(x=x, y=y+20)

        self.entry_isbn = Entry(window)
        self.entry_isbn.place(x=x+60, y=y)

        self.entry_title = Entry(window)
        self.entry_title.place(x=x+60, y=y+20)
# =======================================================================================