# 命令调用器
from command.bili_hot import get_bili_hot_str
from command.douyin_hot import get_douyin_hot_str
from command.github_trending import get_github_trending_str
from command.gpt_reply import reply_by_gpt35, reply_by_gpt4
from command.help import get_help_msg
from command.pai_post import get_pai_post_str
from command.today_in_history import get_today_in_history_str
from command.todo import add_todo_task, view_todos, load_todos, save_todos
from command.transalte import (
    get_reverso_context_tran_str,
    detect_lang,
    check_lang_support,
)
from command.weibo_hot import get_weibo_hot_str
from command.zhihu_hot import get_zhihu_hot_str
from send_msg import SendTo, Sender


class CommandInvoker:
    def __init__(self) -> None:
        pass

    # 命令：/help
    @staticmethod
    def cmd_help(to: SendTo) -> None:
        Sender.send_text_msg(to, get_help_msg())

    # 命令：/gpt
    @staticmethod
    def cmd_gpt35(to: SendTo, message: str) -> None:
        # 获取 gpt3.5 回复
        Sender.send_text_msg(to, reply_by_gpt35(message))

    # 命令：/gpt4
    @staticmethod
    def cmd_gpt4(to: SendTo, message: str) -> None:
        Sender.send_text_msg(to, reply_by_gpt4(message))

    # 命令：/bili-hot
    @staticmethod
    def cmd_bili_hot(to: SendTo) -> None:
        Sender.send_text_msg(to, get_bili_hot_str())

    # 命令：/zhihu-hot
    @staticmethod
    def cmd_zhihu_hot(to: SendTo) -> None:
        Sender.send_text_msg(to, get_zhihu_hot_str())

    # 命令：/weibo-hot
    @staticmethod
    def cmd_weibo_hot(to: SendTo) -> None:
        Sender.send_text_msg(to, get_weibo_hot_str())

    # 命令：/word
    # TODO: 改成解释单词，不翻译
    @staticmethod
    def cmd_word(to: SendTo, message: str) -> None:
        # 检测文本语言
        from_lang = detect_lang(message)
        to_lang = "chinese"
        # en -> zh
        # zh -> en
        # other -> zh -> en
        if from_lang == "":
            Sender.send_text_msg(to, "无法检测文本语言")
            return
        if from_lang == "chinese":
            to_lang = "english"
        elif from_lang != "english" and not check_lang_support(from_lang, "chinese"):
            to_lang = "english"
        # 获取翻译
        result = get_reverso_context_tran_str(message, from_lang, to_lang)
        Sender.send_text_msg(to, result)

    # 命令：/tran
    @staticmethod
    def cmd_tran(to: SendTo, message: str) -> None:
        # 获取翻译
        Sender.send_text_msg(to, "翻译功能暂未开放")

    # 命令：/people-daily
    @staticmethod
    def cmd_people_daily(to: SendTo) -> None:
        # 获取人民日报
        Sender.send_text_msg(to, "人民日报功能暂未开放")

    # 命令：/today-in-history
    @staticmethod
    def cmd_today_in_history(to: SendTo) -> None:
        # 获取历史上的今天
        Sender.send_text_msg(to, get_today_in_history_str())

    # 命令：/github-trending
    @staticmethod
    def cmd_github_trending(to: SendTo) -> None:
        Sender.send_text_msg(to, get_github_trending_str())

    # 命令：/douyin-hot
    @staticmethod
    def cmd_douyin_hot(to: SendTo) -> None:
        Sender.send_text_msg(to, get_douyin_hot_str())

    # 命令：/pai-post
    @staticmethod
    def cmd_pai_post(to: SendTo) -> None:
        Sender.send_text_msg(to, get_pai_post_str())

    # 命令：/todo
    @staticmethod
    def cmd_todo(to: SendTo, message: str, personid: str, personname: str) -> None:
        # 获取用户id
        person_id = personid
        # 获取用户名
        person_name = personname
        # 判断是查询还是添加
        if message == "":
            # 获取待办事项
            result = view_todos(person_id, person_name)
            Sender.send_text_msg(to, result)
        else:
            # 添加待办事项
            add_success = add_todo_task(person_id, message)
            if add_success:
                Sender.send_text_msg(to, "添加成功")
                result = view_todos(person_id, person_name)
                Sender.send_text_msg(to, result)
            else:
                Sender.send_text_msg(to, "添加失败")

    # 命令：/rmtd
    @staticmethod
    def cmd_remove_todo(
            to: SendTo, message: str, personid: str, personname: str
    ) -> None:
        # 获取用户id
        person_id = personid
        # 获取用户名
        person_name = personname
        if not message.isdigit():
            Sender.send_text_msg(to, "请输入有效数字来删除待办事项")
            return

        task_index = int(message) - 1  # 用户输入的数字转换为任务索引
        todos = load_todos(person_id)

        if 0 <= task_index < len(todos):
            removed_task = todos.pop(task_index)  # 删除对应索引的任务
            save_todos(person_id, todos)
            Sender.send_text_msg(to, f"成功删除任务: {removed_task}")
            result = view_todos(person_id, person_name)
            Sender.send_text_msg(to, result)
        else:
            Sender.send_text_msg(to, "请输入有效数字来删除待办事项")

