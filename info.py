import requests
from bs4 import BeautifulSoup

# url 설정
announce_url = "https://www.dju.ac.kr/dju/na/ntt/selectNttList.do?mi=1188&bbsId=1040"
scholarship_url = "https://www.dju.ac.kr/dju/na/ntt/selectNttList.do?mi=3957&bbsId=1853"
schedule_url = "https://www.dju.ac.kr/dju/sv/schdulView/schdulCalendarView.do?mi=1166"

# 공지사항 [제목, 유형, 게시일, 링크, 조회수]
announce_res = requests.get(announce_url)
announce_res.raise_for_status()
announce_html = BeautifulSoup(announce_res.text, "lxml")
announce_contents = announce_html.find("div", attrs={"class":"BD_list"}).find("tbody").find_all("tr")
def get_announce():
    announce_list = []
    for content in announce_contents:
        content_title = content.find("a").get_text().strip()
        content_date = content.find_all("td")[3].get_text()
        content_id = content.find("a").attrs['data-id']
        content_view = int(content.find_all("td")[4].get_text())
        content_url = f"https://www.dju.ac.kr/dju/na/ntt/selectNttInfo.do?nttSn={content_id}&bbsId=1040&mi=1188"
        if content.find("td", attrs={"class":"bbs_01"}):
            content_type = "공지"
        else:
            content_type = "일반"
        announce_list.append([content_title, content_type, content_date, content_url, content_view])
    return announce_list

# 장학 [제목, 유형, 게시일, 링크, 조회수]
scholarship_res = requests.get(scholarship_url)
scholarship_res.raise_for_status()
scholarship_html = BeautifulSoup(scholarship_res.text, "lxml")
scholarship_contents = scholarship_html.find("div", attrs={"class":"BD_list"}).find("tbody").find_all("tr")
def get_scholarship():
    scholarship_list = []
    for content in scholarship_contents:
        content_title = content.find("a").get_text().strip()
        content_date = content.find_all("td")[3].get_text()
        content_id = content.find("a").attrs['data-id']
        content_view = int(content.find_all("td")[4].get_text())
        content_url = f"https://www.dju.ac.kr/dju/na/ntt/selectNttInfo.do?nttSn={content_id}&bbsId=1040&mi=1188"
        if content.find("td", attrs={"class":"bbs_01"}):
            content_type = "공지"
        else:
            content_type = "일반"
        scholarship_list.append([content_title, content_type, content_date, content_url, content_view])
    return scholarship_list

# 학사일정 [] = 연, [] = 월, [순서, 날짜정보, 일정]
schedule_res = requests.get(schedule_url)
schedule_res.raise_for_status()
schedule_html = BeautifulSoup(schedule_res.text, "lxml")
schedule_contents = schedule_html.find("ul", attrs={"id":"schedule_month"}).find_all("div", attrs={"class":"schedule_calendar"})
schedule_year = []
def get_schedule():
    for schedule in schedule_contents:
        schedule_info = schedule.find_all("tbody")[1].find_all("tr")
        for schedule_detail in schedule_info:
            schedule_date = schedule_detail.find("td", attrs={"class":"ac first"}).get_text()
            schedule_label = schedule_detail.find("ul", attrs={"class":"list_st3"}).get_text()
        schedule_year.append([schedule_date, schedule_label])
    return schedule_year

# 정렬
def sort_by_view(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j][4] < arr[j+1][4]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sort_by_date(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            bymd = arr[j][2].split('.')
            aymd = arr[j+1][2].split('.')
            if int(bymd[2]) < int(aymd[2]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if int(bymd[1]) < int(aymd[1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if int(bymd[0]) < int(aymd[0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else: continue
    return arr

# 선착순 확인
def check_limited(arr):
    url = arr[3]
    res = requests.get(url)
    res.raise_for_status()
    html = BeautifulSoup(res.text, "lxml")
    if "선착순" in html.get_text(): return "limited"

def collect_limited(arr):
    result = []
    for content in arr:
        if check_limited(content) == "limited":
            result.append(content)
    return result