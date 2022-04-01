from doctest import master
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image,ImageTk

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
        
        self.label_image = Label(window)
        self.label_image.place(x=x-135,y=y-5) 

        self.entry_phone = Entry(window)
        self.entry_phone.place(x=x+60, y=y)

        self.entry_name = Entry(window)
        self.entry_name.place(x=x+60, y=y+25)

        self.entry_birthday = Entry(window)
        self.entry_birthday.place(x=x+60,y=y+50)

        self.entry_email = Entry(window)
        self.entry_email.place(x=x+60,y=y+100)

        self.RadioButton_gender = IntVar()
        self.gender_rb1 = Radiobutton(window, text="남",variable=self.RadioButton_gender,value=1)
        self.gender_rb2 = Radiobutton(window, text="여",variable=self.RadioButton_gender,value=2)
        self.gender_rb1.place(x=x+60,y=y+75)
        self.gender_rb2.place(x=x+140,y=y+75)

        self.RadioButton_registration = IntVar()
        self.registration_rb1= Radiobutton(window, text="등록",variable=self.RadioButton_registration,value=1)
        self.registration_rb2= Radiobutton(window, text="탈퇴(정보 유지)",variable=self.RadioButton_registration,value=2)
        self.registration_rb1.place(x=x+60,y=y+125)
        self.registration_rb2.place(x=x+140,y=y+125)

        def open_dialog():
            filename = askopenfilename(parent=window,filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
            photo = Image.open(filename)
            resize_photo = photo.resize((150,150))
            photo_tk = ImageTk.PhotoImage(resize_photo,master=window)
            self.label_image.configure(image=photo_tk,width=120,height=150)
            self.label_image.image = photo_tk

        self.Button_image = Button(window,text="이미지 추가",width=15,command=open_dialog)
        self.Button_image.place(x=x-130,y=y+160)
# =======================================================================================


# =======================================================================================
# 클래스: 도서를 추가하거나 수정할 때, 도서 정보 및 이미지를 입력하는 위젯을 모아놓은 패널
# =======================================================================================
class Panel_Edit_Book():

    # 생성자
    def __init__(self, window, x, y):

        self.label_isbn = Label(window, text="ISBN : ")
        self.label_isbn.place(x=x, y=y)

        self.label_title = Label(window, text="도서명 : ")
        self.label_title.place(x=x, y=y+25)

        self.label_author = Label(window, text="저자 : ")
        self.label_author.place(x=x, y=y+50)

        self.label_publisher = Label(window, text="출판사 : ")
        self.label_publisher.place(x=x, y=y+75)

        self.label_price = Label(window, text="가격(₩) : ")
        self.label_price.place(x=x, y=y+100)

        self.label_link = Label(window, text="관련링크 : ")
        self.label_link.place(x=x, y=y+125)

        self.label_book_explain = Label(window, text="도서설명 : ")
        self.label_book_explain.place(x=x, y=y+150)

        self.label_image = Label(window)
        self.label_image.place(x=x-135,y=y-5) 

        self.entry_isbn = Entry(window)
        self.entry_isbn.place(x=x+60, y=y)

        self.entry_title = Entry(window)
        self.entry_title.place(x=x+60, y=y+25)

        self.entry_author = Entry(window)
        self.entry_author.place(x=x+60, y=y+50)

        self.entry_publisher = Entry(window)
        self.entry_publisher.place(x=x+60, y=y+75)

        self.entry_price = Entry(window)
        self.entry_price.place(x=x+60, y=y+100)

        self.entry_link = Entry(window)
        self.entry_link.place(x=x+60, y=y+125)

        self.entry_book_explain = Entry(window)
        self.entry_book_explain.place(x=x+60, y=y+150)

        def open_dialog():
            filename = askopenfilename(parent=window,filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
            photo = Image.open(filename)
            resize_photo = photo.resize((150,150))
            photo_tk = ImageTk.PhotoImage(resize_photo,master=window)
            self.label_image.configure(image=photo_tk,width=120,height=150)
            self.label_image.image = photo_tk

        self.Button_image = Button(window,text="이미지 추가",width=15,command=open_dialog)
        self.Button_image.place(x=x-130,y=y+160)
# =======================================================================================