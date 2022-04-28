from threading import currentThread
import info
from tkinter import *
import webbrowser

current_content = ""
current_view = []
# 가져오기 후 추가
def announce_list():
    contents = info.get_announce()
    list_result.delete(0, END)
    for content in contents:
        list_result.insert(END, content[0])
    current_view = contents
    current_content = "announce"

def scholarship_list():
    contents = info.get_scholarship()
    list_result.delete(0, END)
    for content in contents:
        list_result.insert(END, content[0])
    current_view = contents
    current_content = "scholarship"

def schedule_list():
    list_result.delete(0, END)
    current_content = "schedule"
    pass

def open_url():
    pass

# 기본형
root = Tk()
root.title("LMS-mini")
root.geometry("600x800")
root.resizable(False, False)

# 게시판 영역
frame_board = LabelFrame(root, relief="solid", bd=1, text="정보")
frame_board.pack(side="top", fill="x", padx=10, pady=10, ipady=3, ipadx=3)
# 게시판-버튼 영역
btn_announce = Button(frame_board, text="공지사항", width=25, command=announce_list)
btn_scholarship = Button(frame_board, text="장학", width=25, command=scholarship_list)
btn_schedule = Button(frame_board, text="학사일정", width=25, command=schedule_list)
btn_announce.pack(side="left",padx=6)
btn_scholarship.pack(side="left", padx=6)
btn_schedule.pack(side="left", padx=6)

# 결과 영역
frame_result = Frame(root)
frame_result.pack(fill="both", padx=10)

scrollbar = Scrollbar(frame_result)
scrollbar.pack(side="right", fill="y")

list_result = Listbox(frame_result, selectmode="single", height=35, yscrollcommand=scrollbar.set)
list_result.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_result.yview)

# 옵션 영역
frame_option = LabelFrame(root, relief="solid", bd=1, text="옵션")
frame_option.pack(side="top", fill="x", padx=10, pady=10, ipady=3, ipadx=3)
# 옵션-버튼 영역
btn_view = Button(frame_option, text="조회수", width=25, command=announce_list)
btn_limited = Button(frame_option, text="선착순", width=25, command=scholarship_list)
btn_ignore = Button(frame_option, text="무시", width=25, command=schedule_list)
btn_view.pack(side="left",padx=6)
btn_limited.pack(side="left", padx=6)
btn_ignore.pack(side="left", padx=6)

# 링크 영역
frame_link = Frame(root)
btn_open = Button(frame_option)


root.mainloop()