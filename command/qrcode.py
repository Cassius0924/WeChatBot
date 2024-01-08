# URL转二维码命令
from utils.time import get_current_datetime

import qrcode


def generate_qrcode(data: str) -> str:
    """生成二维码，返回二维码的保存路径"""
    qr = qrcode.QRCode( # type: ignore
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, # type: ignore
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存到 data/qrcodes/ 目录下
    dt_str = get_current_datetime()
    path = f"data/qrcodes/{dt_str}.png"
    img.save(path)
    return path


# FIXME: 发送后，二维码后缀名不对，导致微信识别成普通文件
def get_qrcode_url(data: str) -> str:
    """获取二维码的url"""
    return f"https://api.qrserver.com/v1/create-qr-code/?data={data}"
