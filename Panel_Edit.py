from tkinter import *


# =======================================================================================
# 클래스: 회원을 추가하거나 수정할 때, 회원 정보 및 이미지를 입력하는 위젯을 모아놓은 패널
# =======================================================================================
class Panel_Edit_User():

    # 생성자
    def __init__(self, window, x, y):
        self.label_phone = Label(window, text="전화번호 : ")        
        self.label_phone.place(x=x, y=y)

        self.label_name = Label(window, text="이름 : ")
        self.label_name.place(x=x, y=y+25)

        self.label_birthday = Label(window, text = "생년월일 : ")
        self.label_birthday.place(x=x,y=y+50)
        
        self.label_gender = Label(window, text = "성별 : ")
        self.label_gender.place(x=x,y=y+75)

        self.label_email = Label(window,text="이메일 : ")
        self.label_email.place(x=x,y=y+100)

        self.label_registration = Label(window,text="상태 : ")
        self.label_registration.place(x=x,y=y+125)

        self.photo = PhotoImage(file="2.gif")
        self.label_image = Label(window,width=50,height=100,image=self.photo)
        self.label_image.place(x=x-150,y=y)

        self.entry_phone = Entry(window)
        self.entry_phone.place(x=x+60, y=y)

        self.entry_name = Entry(window)
        self.entry_name.place(x=x+60, y=y+25)

        self.entry_birthday = Entry(window)
        self.entry_birthday.place(x=x+60,y=y+50)

        self.RadioButton_gender = IntVar()
        self.gender_rb1 = Radiobutton(window, text="남",variable=self.RadioButton_gender,value=1)
        self.gender_rb2 = Radiobutton(window, text="여",variable=self.RadioButton_gender,value=2)
        self.gender_rb1.place(x=x+60,y=y+75)
        self.gender_rb2.place(x=x+140,y=y+75)

        self.entry_email = Entry(window)
        self.entry_email.place(x=x+60,y=y+100)

        self.RadioButton_registration = IntVar()
        self.registration_rb1= Radiobutton(window, text="등록",variable=self.RadioButton_registration,value=1)
        self.registration_rb2= Radiobutton(window, text="탈퇴(정보 유지)",variable=self.RadioButton_registration,value=2)
        self.registration_rb1.place(x=x+60,y=y+125)
        self.registration_rb2.place(x=x+140,y=y+125)


        
        
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