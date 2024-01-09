import requests
from utils.time import get_current_year_month, get_current_day, get_current_ymd
from utils.path import get_abs_path

def is_url_valid(url: str) -> bool:
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def get_paper_people_todaypdf() -> str:
    """获取今日人民日报pdf"""
    yearmonthday = get_current_ymd()
    year_month = get_current_year_month()
    day = get_current_day()
    #TODO: 版本号需要根据实际情况修改
    version = "01"
    save_path = get_abs_path(f"data/paper_people_pdf/{yearmonthday}.pdf")
    url = f"http://paper.people.com.cn/rmrb/images/{year_month}/{day}/{version}/rmrb{yearmonthday}{version}.pdf"
  # url = f"http://paper.people.com.cn/rmrb/images/2024-01/09/01/rmrb2024010901.pdf"

    if not is_url_valid(url):
        print(f"下载失败，{url}无效")
        return ""

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open("save_path", "wb") as file:
                file.write(response.content)
            print(f"下载成功，保存路径为{save_path}")
        else:
            print(f"下载失败，状态码为{response.status_code}")
    except Exception as e:
        print(f"下载失败，错误为{e}")
    return save_path

def get_paper_people_datepdf() -> str:
    pass

def get_paper_people_pdfurl() -> str:
    pass
