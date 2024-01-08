from PIL import Image, ImageDraw, ImageFont


def text_to_image(data: str) -> str:
    image_width = 500  # Width of the image
    line_height = 31  # Height of each line
    background_color = (255, 255, 255)  # White

    # Split the text into lines based on newline character (\n)
    lines = data.split("\n")
    num_lines = len(lines)

    # Calculate image height based on the number of lines and line height
    image_height = num_lines * line_height
    image = Image.new('RGB', (image_width, image_height), background_color)

    # Choose a font and font size
    font_path = "SimHei.ttf"  # Replace with your font file path
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define text color
    text_color = (0, 0, 0)  # Black

    # Define initial text position (top-left corner)
    x_position = 50
    y_position = 50

    # Draw each line of text on the image
    try:
        for line in lines:
            draw.text((x_position, y_position), line, fill=text_color, font=font)
            y_position += line_height  # Move to the next line

        # Save the image
        output_image_path = f"data/text_image/help.png"
        image.save(output_image_path)
        return output_image_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

