from tkinter import *
from tkinter import messagebox

from datetime import datetime, timedelta

import pandas as pd

from Window_Add import Window_Add_User
from Window_Add import Window_Add_Book
from Panel_Show import Panel_Show_Book
from Panel_Show import Panel_Show_User

BOOK_INFO_X = 475
BOOK_INFO_Y = 20
BTN_WIDTH = 75

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

# ===========================================================================================
# 클래스: 메인 윈도우
# ===========================================================================================
class Window_Main():

    # 생성자
    def __init__(self):
        self.window = Tk()
        self.window.title("도서 대여 프로그램")
        self.window.geometry('900x575')

        self.userinfo = Panel_Show_User(self.window, x=10, y=20)    # 회원 정보 패널 붙이기
        self.bookinfo = Panel_Show_Book(self.window, x=BOOK_INFO_X, y=BOOK_INFO_Y)   # 도서 정보 패널 붙이기

        # 대여 버튼
        self.btn_save_book = Button(self.window, text="대여", command=self.event_book_rent)
        self.btn_save_book.place(x=BOOK_INFO_X+240, y=BOOK_INFO_Y+500, width=BTN_WIDTH)

        # 반납 버튼
        self.btn_save_book = Button(self.window, text="반납", command=self.event_book_return)
        self.btn_save_book.place(x=BOOK_INFO_X+330, y=BOOK_INFO_Y+500, width=BTN_WIDTH)

        self.load_menu()    # 메뉴바 붙이기

        self.window.mainloop()

    # 멤버 메소드: 윈도우 상단에 메뉴 붙이기
    def load_menu(self):
        # 메뉴바 추가
        self.menubar = Menu(self.window, tearoff=0)
        self.window.config(menu = self.menubar)

        # [파일] 메뉴 추가
        self.menu_1 = Menu(self.menubar)
        self.menubar.add_cascade(label="파일", menu=self.menu_1)

        # [파일] 메뉴의 하위 항목 추가
        self.menu_1.add_command(label="프로그램 종료", command=quit)

        # [신규 데이터 추가] 메뉴 추가
        self.menu_2 = Menu(self.menubar)
        self.menubar.add_cascade(label="신규 데이터 추가", menu=self.menu_2)

        # [신규 데이터 추가] 메뉴의 하위 항목 추가
        self.menu_2.add_command(label="신규 회원 추가", command=self.load_window_add_user)
        self.menu_2.add_separator()
        self.menu_2.add_command(label="신규 도서 추가", command=self.load_window_add_book)

    # 멤버 메소드: (이벤트) 신규 회원 추가 윈도우 띄우기
    def load_window_add_user(self):
        Window_Add_User()

    # 멤버 메소드: (이벤트) 신규 도서 추가 윈도우 띄우기
    def load_window_add_book(self):
        Window_Add_Book()

    # 멤버 메소드: [대여] 버튼 이벤트
    def event_book_rent(self):

        # 데이터프레임 불러오기
        df_user, df_book, df_rent = load_dataframes()

        # 대여자의 이름과 전화번호 구하기
        try:
            user_phone = self.userinfo.get_phone()
            user_name = df_user["USER_NAME"].loc[user_phone]
        except KeyError:
            if user_phone.strip('') == '':
                messagebox.showinfo("도서 대여", f"회원 전화번호가 입력되지 않았습니다.")
                return -1
            else:
                messagebox.showinfo("도서 대여", f"전화번호 {user_phone} 회원을 찾을 수 없습니다.")
                return -2

        # 대여 도서의 ISBN과 도서명 구하기
        try:
            book_isbn = self.bookinfo.get_isbn()
            book_title = df_book["BOOK_TITLE"].loc[book_isbn]
        except ValueError:
            messagebox.showinfo("도서 대여", f"도서 ISBN이 입력되지 않았습니다.")
            return -3
        except KeyError:
            messagebox.showinfo("도서 대여", f"ISBN {book_isbn} 도서를 찾을 수 없습니다.")
            return -4

        # 대여일(오늘 날짜) 가져오기
        today = datetime.now()
        today_format = today.strftime("%Y%m%d")
        
        # 반납예정일(2주 뒤 날짜) 가져오기
        due = today + timedelta(weeks=2)
        due_format = due.strftime("%Y%m%d")
        
        # 해당 도서의 대여 이력 중 '대여 중'에 해당하는 이력만 추출
        df_rent_rented = df_rent[["BOOK_ISBN"]][df_rent["RENT_RETURN_DATE"] == -1]
        
        # 대여가 불가능한 경우의 이벤트 처리
        if not df_rent_rented.empty:
            messagebox.showinfo("도서 대여", "이미 대여중인 도서입니다.")
            return 1
        elif df_user["USER_REG"].loc[user_phone] == False:
            messagebox.showinfo("도서 대여", "탈퇴한 회원은 도서를 대여할 수 없습니다.")
            return 2

        # 대여 이력 추가
        new_rent = { "BOOK_ISBN": book_isbn,\
                    "USER_PHONE": user_phone,\
                    "RENT_DATE": today_format,\
                    "RENT_DUE_DATE": due_format,\
                    "RENT_RETURN_DATE": -1 }
        df_rent = df_rent.append(new_rent, ignore_index=True)

        # 대여자의 대여 카운트 증가
        df_user["USER_RENT_CNT"].loc[user_phone] += 1

        # 데이터프레임을 csv 파일에 저장
        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
        df_rent.to_csv(DIR_CSV_RENT, index=True, encoding='CP949')

        # 테이블 새로고침
        self.userinfo.update_table()
        self.bookinfo.update_table()

        msg = "도서 대여 완료\n"
        msg += f"- {book_title}({book_isbn})\n"
        msg += f"- 대여자: {user_name}({user_phone})"
        messagebox.showinfo("도서 대여", msg)

        return 0


    # 멤버 메소드: [반납] 버튼 이벤트
    def event_book_return(self):

        # 데이터프레임 불러오기
        df_user, df_book, df_rent = load_dataframes()


        # 선택한 도서에 대한 ISBN과 도서명, 대여번호, 대여자 전화번호 불러오기
        try:
            book_isbn = self.bookinfo.get_isbn()
            book_title = df_book["BOOK_TITLE"].loc[book_isbn]
            rent_seq = max(df_rent[df_rent["BOOK_ISBN"] == book_isbn].index)
            rent_phone = df_rent["USER_PHONE"].loc[rent_seq]
        except ValueError:
            messagebox.showinfo("도서 반납", f"도서 ISBN이 입력되지 않았습니다.")
            return -3
        except KeyError:
            messagebox.showinfo("도서 반납", f"ISBN {book_isbn} 도서를 찾을 수 없습니다.")
            return -4         

        # 이미 반납한 경우의 이벤트 처리
        if df_rent["RENT_RETURN_DATE"].loc[rent_seq] != -1:
            messagebox.showinfo("도서 반납", "이미 반납한 도서입니다.")
            return 1

        # 반납일(오늘 날짜) 가져오기
        today = datetime.now()
        today_format = today.strftime("%Y%m%d")

        # 반납 실행
        df_rent["RENT_RETURN_DATE"].loc[rent_seq] = today_format
        df_user["USER_RENT_CNT"].loc[rent_phone] -= 1

        df_user.to_csv(DIR_CSV_USER, index=False, encoding='CP949')
        df_rent.to_csv(DIR_CSV_RENT, index=True, encoding='CP949')

        # 테이블 새로고침
        self.userinfo.update_table()
        self.bookinfo.update_table()

        # 회원 정보 패널에 대여자(반납자) 정보 출력
        self.userinfo.event_show_return_user(rent_phone)
        
        msg = "도서 반납 완료\n"
        msg += f"- {book_title}({book_isbn})\n"
        messagebox.showinfo("도서 반납", msg)

        return 0

# ===========================================================================================