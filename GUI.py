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
    global current_view
    global current_content
    current_view = contents
    current_content = "announce"

def scholarship_list():
    contents = info.get_scholarship()
    list_result.delete(0, END)
    for content in contents:
        list_result.insert(END, content[0])
    global current_view
    global current_content
    current_view = contents
    current_content = "scholarship"

def schedule_list():
    list_result.delete(0, END)
    global current_content
    current_content = "schedule"

# 무시 기능
def ignore():
    title = list_result.get(list_result.curselection())
    info.ignore([title])
    if current_content == "announce":
        announce_list()
    elif current_content == "scholarship":
        scholarship_list()
    else:
        pass

# 선착순 추리기
def limited():
    if current_content == "schedule":
        return
    global current_view
    limited_contents = info.collect_limited(current_view)
    list_result.delete(0, END)
    for content in limited_contents:
        list_result.insert(END, content[0])
    current_view = limited_contents

# 조회수 정렬
def sort_view():
    if current_content == "schedule":
        return
    global current_view
    sorted_list = info.sort_by_view(current_view)
    list_result.delete(0, END)
    for content in sorted_list:
        list_result.insert(END, content[0])
    current_view = sorted_list

# 링크 열기
def open_url():
    if current_content == "schedule":
        return
    global current_view
    title = list_result.get(list_result.curselection())
    for i in current_view:
        if title in i:
            webbrowser.open(i[2])
        
# 학사일정 확인
def schedule_list():
    schedule_overall = info.get_schedule()
    list_result.delete(0, END)
    checked_schedule = []
    for schedule in schedule_overall:
        if schedule in checked_schedule:
            continue
        list_result.insert(END, f"{schedule[0]} / {schedule[1]}")
        checked_schedule.append(schedule)
    global current_content
    current_content = "schedule"

# 기본형
root = Tk()
root.title("LMS-mini")
root.geometry("600x750")
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
btn_view = Button(frame_option, text="조회수", width=25, command=sort_view)
btn_limited = Button(frame_option, text="선착순", width=25, command=limited)
btn_ignore = Button(frame_option, text="무시", width=25, command=ignore)
btn_view.pack(side="left",padx=6)
btn_limited.pack(side="left", padx=6)
btn_ignore.pack(side="left", padx=6)

# 링크 영역
frame_link = Frame(root)
frame_link.pack(fill="both", padx=10, pady=10, ipady=3, ipadx=3)
btn_open = Button(frame_link, text="바로가기", command=open_url)
btn_open.pack(fill="both")

root.mainloop()