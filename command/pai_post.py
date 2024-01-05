import requests

def get_pai_post_str() -> str:
    pai_post_list = get_pai_post_list()
    if pai_post_list == []:
        return "获取少数派早报失败"
    pai_post_str = "✨=====派早报=====✨\n"
    for i, pai_post in enumerate(pai_post_list):
        pai_post_str += f"{i + 1}. {pai_post}\n"
    return pai_post_str


def get_pai_post_list() -> list:
    response: requests.Response
    try:
        # url = "https://sspai.com/api/v1/articles"
        url = "https://sspai.com/api/v1/articles/85581"
        response = requests.get(url, timeout=10)
    except Exception:
        print("请求少数派早报失败")
        return []

    if response.status_code != 200:
        print("获取少数派早报失败")
        return []

    pai_post_list = response.json()
    return pai_post_list.get("morning_paper_title", [])
