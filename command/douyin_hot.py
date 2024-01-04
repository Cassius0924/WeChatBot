import requests


def get_douyin_hot_str() -> str:
    hot_list = get_douyin_hot_list()
    if not hot_list:
        return "获取抖音热搜失败"
    hot_str = "✨=====抖音热搜=====✨\n"
    for i, hot in enumerate(
        hot_list["word_list"][:20]
    ):
        hot_str += f"{i + 1}.  {hot['word']}\n"
    return hot_str


def get_douyin_hot_list() -> list:
    url = "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/?reflow_source=reflow_page&web_id=7320147385195562523&device_id=7320147385195562523&msToken=FmBVSfj564dcrkJbxohUGZiGSE6fw62Q65ZPE__0DJgSc2fC72tLeVPNnDJQNue0jLa1PwmpgrNGL4KclXaTdGgnpPHXDXYNLWpK-YDRL9-oSsA1weeUhhClzuoq-g%3D%3D&a_bogus=YyUDXchBMsm1qDfeawkz9yvm-1E0YW5IgZEF2UUzGULg"
    response = requests.get(url)

    if response.status_code == 200:
        hot_list = response.json()
        return hot_list

    print("获取抖音热搜失败")
    return []
