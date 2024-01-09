import requests
from utils.time import get_current_year_month, get_current_day, get_current_ymd
from utils.path import get_abs_path

def get_paper_people_pdf_path(date_version: str) -> str:#2024010901
    """获取人民日报pdf到本地并返回路径"""
    #判断字符串是否为数字并且长度为10
    if date_version.isdigit() and len(date_version) == 10:
        yearmonthday = date_version[:8]#20240109
        year = date_version[:4]#2024
        month = date_version[4:6]#01
        day = date_version[6:8]#09
        year_month = f"{year}-{month}"#2024-01
        version = date_version[8:]#01
        save_path = get_abs_path(f"data/paper_people_pdf/{yearmonthday}.pdf")
        # url = "http://paper.people.com.cn/rmrb/images/2024-01/09/01/rmrb2024010901.pdf"
        url = f"http://paper.people.com.cn/rmrb/images/{year_month}/{day}/{version}/rmrb{yearmonthday}{version}.pdf"

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                print(f"下载成功，保存路径为{save_path}")
            else:
                print(f"下载失败，状态码为{response.status_code}")
        except Exception as e:
            print(f"下载失败，错误为{e}")
        return save_path
    else:
        print("输入的日期版本号不符合要求，请重新输入")
        return None

def get_paper_people_todaypdf() -> str:#2024010901
    """获取今日人民日报pdf"""
    yearmonthday = get_current_ymd()
    version = "01"
    today_version = f"{yearmonthday}{version}"
    save_path = get_paper_people_pdf_path(today_version)
    return save_path


# def get_paper_people_savepath(date_version:int) -> str:
#     """获取本地的今日人民日报pdf路径"""
#
#     save_path = get_paper_people_todaypdf()
#     return save_path
#
# def get_paper_people_url() -> str:
#     """获取今日人民日报pdf的url"""
#     url =get_paper_people_todaypdf()
#     return url
