# 获取命令帮助消息
from command.command_set import cmd_dict
from utils.text_to_image import text_to_image


def get_help_msg() -> str:
    help_msg = "=====帮助信息=====\n"
    for value in cmd_dict.values():
        if value["value"] == 0:
            continue
        cmd_msg = ""
        for key in value["keys"]:
            cmd_msg += "/" + key + "\n"
        help_msg += cmd_msg + "➡️「" + value["desc"] + "」\n"
    return help_msg

# def get_help_image() -> str:
#     help_msg = "=====帮助信息=====\n"
#     for value in cmd_dict.values():
#         if value["value"] == 0:
#             continue
#         cmd_msg = ""
#         for key in value["keys"]:
#             cmd_msg += "/" + key + "\n"
#         help_msg += cmd_msg + "「" + value["desc"] + "」\n"
#     image_path = text_to_image(help_msg)
#     if image_path:
#         return image_path
#     else:
#         return "获取帮助信息失败。"
