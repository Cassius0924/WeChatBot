# 命令集
# TODO: 添加参数功能，例如天气查询，可以添加城市参数（/天气 北京）
cmd_dict = {
    "None": {"keys": ["None"], "desc": "无效指令。", "value": 0},
    "help": {
        "keys": ["帮助", "help"],
        "desc": "获取帮助信息。",
        "value": 1,
    },
    "gpt4": {
        "keys": ["gpt4"],
        "desc": "调用GPT4进行回答。",
        "value": 2,
    },
    "gpt": {
        "keys": ["gpt"],
        "desc": "调用GPT3.5进行回答。",
        "value": 3,
    },
    "image-stitch": {
        "keys": ["图片拼接", "image-stitch"],
        "desc": "调用图像拼接。",
        "value": 4,
    },
    "github-trending": {
        "keys": ["github趋势", "github-trending"],
        "desc": "获取github趋势。",
        "value": 5,
    },
    "bili-hot": {
        "keys": ["b站热搜", "bili-hot"],
        "desc": "获取b站热搜。",
        "value": 6,
    },
    "zhihu-hot": {
        "keys": ["知乎热搜", "zhihu-hot"],
        "desc": "获取知乎热搜。",
        "value": 7,
    },
    "weibo-hot": {
        "keys": ["微博热搜", "weibo-hot"],
        "desc": "获取微博热搜。",
        "value": 8,
    },
    "weather": {
        "keys": ["天气", "weather"],
        "desc": "获取天气。",
        "value": 9,
    },
    "word": {
        "keys": ["word", "单词"],
        "desc": "解释单词(词、成语)。",
        "value": 10,
    },
    "tran": {
        "keys": ["tran", "翻译"],
        "desc": "翻译英文句子。",
        "value": 11,
    },
    "people": {
        "keys": ["people", "人民日报"],
        "desc": "发送今天人民日报的PDF。",
        "value": 12,
    },
    "today": {
        "keys": ["today-in-history", "历史上的今天"],
        "desc": "历史上的今天。",
        "value": 13,
    },
    "douyin-hot": {
        "keys": ["抖音热搜", "douyin-hot"],
        "desc": "获取抖音热搜。",
        "value": 14,
    },
    "pai-post": {
        "keys": ["派早报", "pai-post"],
        "desc": "获取少数派早报。",
        "value": 15,
    },
    "todo": {
        "keys": ["待办事项", "todo"],
        "desc": "待办事项。",
        "value": 16,
    },
    "rmtd": {
        "keys": ["删除待办事项", "rmtd"],
        "desc": "删除待办事项。",
        "value": 17,
    },
}
