import info
from tkinter import *
import tkinter.messagebox as msgbox
import webbrowser

# 현재 표시된 정보
current_content = ""
current_view = []

# 공지사항 게시글 정보 수집 후 표시
def announce_list():
    contents = info.get_announce()
    list_result.delete(0, END)
    for content in contents:
        list_result.insert(END, content[0])
    global current_view
    global current_content
    current_view = contents
    current_content = "announce"

# 장학 게시글 정보 수집 후 표시
def scholarship_list():
    contents = info.get_scholarship()
    list_result.delete(0, END)
    for content in contents:
        list_result.insert(END, content[0])
    global current_view
    global current_content
    current_view = contents
    current_content = "scholarship"

# 학사일정 정보 수집 후 표시
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

# 선택된 게시물 무시하기
def ignore():
    global current_content
    if current_content == "schedule":
        msgbox.showinfo("알림", "학사일정에서는 제공되지 않는 기능입니다.")
        return
    try:
        global current_view
        title = list_result.get(list_result.curselection())
        info.ignore([title])
        for content in current_view:
            if title in content[0]:
                current_view.remove(content)
        list_result.delete(0, END)
        for content in current_view:
            list_result.insert(END, content[0])
    except:
        msgbox.showinfo("알림", "무시할 게시물을 선택하세요.")

# 선착순 게시물만 추리기
def limited():
    if current_content == "schedule":
        msgbox.showinfo("알림", "학사일정에서는 제공되지 않는 기능입니다.")
        return
    global current_view
    limited_contents = info.collect_limited(current_view)
    list_result.delete(0, END)
    for content in limited_contents:
        list_result.insert(END, content[0])
    current_view = limited_contents

# 조회수 높은 순서대로 정렬
def sort_view():
    if current_content == "schedule":
        msgbox.showinfo("알림", "학사일정에서는 제공되지 않는 기능입니다.")
        return
    global current_view
    sorted_list = info.sort_by_view(current_view)
    list_result.delete(0, END)
    for content in sorted_list:
        list_result.insert(END, content[0])
    current_view = sorted_list

# 링크 열기
def open_url():
    global current_view
    if current_content == "schedule":
        msgbox.showinfo("알림", "학사일정에서는 제공되지 않는 기능입니다.")
        return
    try:
        title = list_result.get(list_result.curselection())
        for i in current_view:
            if title in i:
                webbrowser.open(i[2])
    except:
        msgbox.showinfo("알림","열람할 게시물을 선택하세요.")

# GUI 기본 틀
root = Tk()
root.title("LMS-mini")
root.geometry("600x750")
root.resizable(False, False)
root.iconbitmap("DJU-logo.ico")

# 게시판 영역
frame_board = LabelFrame(root, relief="solid", bd=1, text="정보")
frame_board.pack(side="top", fill="x", padx=10, pady=10, ipady=3, ipadx=3)
# 게시판-버튼
btn_announce = Button(frame_board, text="공지사항", width=25, command=announce_list)
btn_scholarship = Button(frame_board, text="장학", width=25, command=scholarship_list)
btn_schedule = Button(frame_board, text="학사일정", width=25, command=schedule_list)
btn_announce.pack(side="left",padx=6)
btn_scholarship.pack(side="left", padx=6)
btn_schedule.pack(side="left", padx=6)

# 게시물 표시 영역
frame_result = Frame(root)
frame_result.pack(fill="both", padx=10)
# 게시물 표시-세로스크롤
scrollbar = Scrollbar(frame_result)
scrollbar.pack(side="right", fill="y")
# 게시물 표시-리스트박스
list_result = Listbox(frame_result, selectmode="single", height=35, yscrollcommand=scrollbar.set)
list_result.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_result.yview)

# 옵션 영역
frame_option = LabelFrame(root, relief="solid", bd=1, text="옵션")
frame_option.pack(side="top", fill="x", padx=10, pady=10, ipady=3, ipadx=3)
# 옵션-버튼
btn_view = Button(frame_option, text="조회수", width=25, command=sort_view)
btn_limited = Button(frame_option, text="선착순", width=25, command=limited)
btn_ignore = Button(frame_option, text="무시", width=25, command=ignore)
btn_view.pack(side="left",padx=6)
btn_limited.pack(side="left", padx=6)
btn_ignore.pack(side="left", padx=6)

# 링크-버튼
frame_link = Frame(root)
frame_link.pack(fill="both", padx=10, pady=10, ipady=3, ipadx=3)
btn_open = Button(frame_link, text="바로가기", command=open_url)
btn_open.pack(fill="both")

# 종료 방지 루프
root.mainloop()