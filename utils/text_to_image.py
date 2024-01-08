from PIL import Image, ImageDraw, ImageFont
from utils.time import get_current_date


def text_to_image(data: str) -> str:
    image_width = 600
    image_height = 200
    background_color = (255, 255, 255)  # White
    image = Image.new('RGB', (image_width, image_height), background_color)

    # Choose a font and font size
    font_path = "SimHei.ttf"  # Replace with your font file path
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define text color
    text_color = (0, 0, 0)  # Black

    # Define text position (you can adjust this according to your requirement)
    text_position = (50, 50)  # (x, y) coordinates

    # Draw text on the image
    draw.text(text_position, data, fill=text_color, font=font)

    # Save the image
    d_str = get_current_date()
    output_image_path = f"../data/text_image/{d_str}.png"
    image.save(output_image_path)

    return output_image_path

# text = "你好，Hello, World! This is a sample text."
# image_path = text_to_image(text)
# print(f"Image saved at: {image_path}")

    # d_str = get_current_date()
    # output_image_path = f"../data/text_image/{d_str}.png"
    # chinese_font_path = "SimHei.ttf"  # 替换为支持中文字符的字体文件路径
    #
    # # 保存图像
    # image.save(output_image_path)
    # return output_image_path

