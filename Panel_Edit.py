from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

ENTRY_WIDTH = 200

IMG_WIDTH = 120
IMG_HEIGHT = 160
IMG_FILE_TYPE = ["*.gif", "*.png", "*.jpg", "*.jpeg", "*.bmp"]

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
        self.label_image.place(x=x-135, y=y-5, width=IMG_WIDTH, height=IMG_HEIGHT) 

        self.entry_phone = Entry(window)
        self.entry_phone.place(x=x+60, y=y, width=ENTRY_WIDTH)

        self.entry_name = Entry(window)
        self.entry_name.place(x=x+60, y=y+25, width=ENTRY_WIDTH)

        self.entry_birthday = Entry(window)
        self.entry_birthday.place(x=x+60,y=y+50, width=ENTRY_WIDTH)

        self.entry_email = Entry(window)
        self.entry_email.place(x=x+60,y=y+100, width=ENTRY_WIDTH)

        self.RadioButton_gender = StringVar(window)
        self.gender_rb1 = Radiobutton(window, text="남",variable=self.RadioButton_gender,value="남")
        self.gender_rb2 = Radiobutton(window, text="여",variable=self.RadioButton_gender,value="여")
        self.gender_rb1.place(x=x+60,y=y+75)
        self.gender_rb2.place(x=x+140,y=y+75)
        self.RadioButton_registration = IntVar(window)
        self.registration_rb1= Radiobutton(window, text="등록",variable=self.RadioButton_registration,value=True)
        self.registration_rb2= Radiobutton(window, text="탈퇴(정보 유지)",variable=self.RadioButton_registration,value=False)
        self.registration_rb1.place(x=x+60,y=y+125)
        self.registration_rb2.place(x=x+140,y=y+125)
        

        def open_dialog():
            filename = askopenfilename(parent=window,filetypes=(("이미지 파일", IMG_FILE_TYPE),("모든 파일","*.*")))
            self.photo = Image.open(filename)
            resize_photo = self.photo.resize((IMG_WIDTH, IMG_HEIGHT))
            photo_tk = ImageTk.PhotoImage(resize_photo,master=window)
            self.label_image.configure(image=photo_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
            self.label_image.image = photo_tk


        self.Button_image = Button(window,text="이미지 추가",width=15,command=open_dialog)
        self.Button_image.place(x=x-130,y=y+160)

    # 멤버 메소드: 전화번호 등 회원의 속성 리턴
    def get_phone(self):
        return self.entry_phone.get()
    def get_name(self):
        return self.entry_name.get()
    def get_birthday(self):
        number = self.entry_birthday.get()
        number = number.replace("-","")
        return number
    def get_email(self):
        return self.entry_email.get()
    def get_gender(self):
        gender_text = self.RadioButton_gender.get()
        return gender_text
    def get_REG(self):
        reg_boolean = bool(self.RadioButton_registration.get())
        return reg_boolean
    def forget_regis(self):
        self.label_registration.place_forget()
        self.registration_rb1.place_forget()
        self.registration_rb2.place_forget()
    def self_return(self):
        return self
    def get_birthday2(self):
        return self.entry_birthday.get()


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
        self.label_image.place(x=x-135,y=y-5, width=IMG_WIDTH, height=IMG_HEIGHT) 

        self.entry_isbn = Entry(window)
        self.entry_isbn.place(x=x+60, y=y, width=ENTRY_WIDTH)

        self.entry_title = Entry(window)
        self.entry_title.place(x=x+60, y=y+25, width=ENTRY_WIDTH)

        self.entry_author = Entry(window)
        self.entry_author.place(x=x+60, y=y+50, width=ENTRY_WIDTH)

        self.entry_publisher = Entry(window)
        self.entry_publisher.place(x=x+60, y=y+75, width=ENTRY_WIDTH)

        self.entry_price = Entry(window)
        self.entry_price.place(x=x+60, y=y+100, width=ENTRY_WIDTH)

        self.entry_link = Entry(window)
        self.entry_link.place(x=x+60, y=y+125, width=ENTRY_WIDTH)

        self.entry_book_explain = Entry(window)
        self.entry_book_explain.place(x=x+60, y=y+150, width=ENTRY_WIDTH)

        def open_dialog():
            filename = askopenfilename(parent=window,filetypes=(("이미지 파일", IMG_FILE_TYPE),("모든 파일","*.*")))
            # 원본 이미지 데이터 반환
            
            # 이미지 저장 중 취소 버튼 선택시 오류 발생 수정
            try:
                self.image = Image.open(filename)
            except:
                return 0

            resize_image = self.image.resize((IMG_WIDTH, IMG_HEIGHT))
            image_tk = ImageTk.PhotoImage(resize_image,master=window)
            self.label_image.configure(image=image_tk, width=IMG_WIDTH, height=IMG_HEIGHT)
            self.label_image.image = image_tk

        self.Button_image = Button(window,text="이미지 추가",width=15,command=open_dialog)
        self.Button_image.place(x=x-130,y=y+160)

    # 멤버 메소드: ISBN 등 도서의 속성 리턴
    def get_isbn(self):
        return self.entry_isbn.get().rstrip()
        # ISBN 형식 검사 int형으로 입력받게 되면 문자열 입력시 예외처리와 무관하게 바로 오류가 뜸.
    def get_title(self):
        return self.entry_title.get().rstrip()
    def get_author(self):
        return self.entry_author.get().rstrip()
    def get_publisher(self):
        return self.entry_publisher.get().rstrip()
    def get_price(self):
        return self.entry_price.get().rstrip()
        # 가격 형식 검사 위와 동일
    def get_link(self):
        return self.entry_link.get().rstrip()
    def get_book_explain(self):
        return self.entry_book_explain.get().rstrip()

# =======================================================================================