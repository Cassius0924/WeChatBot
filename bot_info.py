# 机器人信息类
import json


class BotInfo:
    id: str = ""
    name: str = ""

    @staticmethod
    def update_from_source(source: str) -> None:
        source_dict = {}
        try:
            source_dict = json.loads(source)
        except Exception:
            print("更新机器人信息时，消息来源JSON解析失败")
            return
        to = source_dict.get("to", {})
        if to == "":
            return
        payload = to.get("payload", {})
        BotInfo.id = payload.get("id", "")
        BotInfo.name = payload.get("name", "")

    @staticmethod
    def update_id(id: str) -> None:
        BotInfo.id = id

    @staticmethod
    def update_name(name: str) -> None:
        BotInfo.name = name
