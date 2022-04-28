import info
from tkinter import *

# 기본형
root = Tk()
root.title("LMS-mini")
root.geometry("400x700")
root.resizable(False, False)

# 게시판 영역
frame_board = LabelFrame(root, relief="solid", bd=1, text="정보")
frame_board.pack(side="top", fill="x", padx=10, pady=10, ipady=3, ipadx=3)
# 게시판-버튼 영역
btn_announce = Button(frame_board, text="공지사항", width=15)
btn_scholarship = Button(frame_board, text="장학", width=15)
btn_schedule = Button(frame_board, text="학사일정", width=15)
btn_announce.pack(side="left",padx=6)
btn_scholarship.pack(side="left", padx=6)
btn_schedule.pack(side="left", padx=6)

# 결과 영역

# 옵션 영역

# 링크 영역

root.mainloop()