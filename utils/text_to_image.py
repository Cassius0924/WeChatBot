from PIL import Image, ImageDraw, ImageFont
from utils.time import get_current_date
import unicodedata


def text_to_image(data: str) -> str:
    d_str = get_current_date()
    output_image_path = f"../data/text_image/{d_str}.png"
    chinese_font_path = "SimHei.ttf"  # 替换为支持中文字符的字体文件路径

    # 创建图像
    image_size = (800, 800)
    font_size = 40
    image = Image.new("RGB", image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # 选择字体和字体大小
    font = ImageFont.load_default()
    chinese_font = ImageFont.truetype(chinese_font_path, font_size)

    # 分割文本内容中的中文和其他字符
    chinese_text = "".join([char for char in data if isinstance(char, str) and "CJK" in unicodedata.name(char)])
    other_text = "".join([char for char in data if not (0x4e00 <= ord(char) <= 0x9fff)])



    # 获取文本的矩形框大小
    # chinese_width, chinese_height = draw.textbbox((0, 0), chinese_text, font=chinese_font)[2:]
    # other_width, other_height = draw.textbbox((0, 0), other_text, font=font)[2:]

    chinese_width, chinese_height = draw.textsize(chinese_text, font=chinese_font)
    other_width, other_height = draw.textsize(other_text, font=font)


    # 计算文本在图像中的位置
    chinese_x = (image_size[0] - chinese_width) / 2
    chinese_y = (image_size[1] - chinese_height - other_height) / 2

    other_x = (image_size[0] - other_width) / 2
    other_y = (image_size[1] + chinese_height - other_height) / 2

    # 在图像上绘制文本
    draw.text((chinese_x, chinese_y), chinese_text, fill=(0, 0, 0), font=chinese_font)
    draw.text((other_x, other_y), other_text, fill=(0, 0, 0), font=font)

    # 保存图像
    image.save(output_image_path)
    return output_image_path


# # 调用函数并传入要转换的文本内容
# text = "你好吼吼吼，Hello, 123!@#"
# resulting_output_image_path = text_to_image(text)
# print(f"图片已保存至 {resulting_output_image_path}")
