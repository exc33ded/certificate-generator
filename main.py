import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

list_of_names = []

def cleanup_data():
    with open("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("certificate_template.png")
        template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)  # Convert to RGB color space

        max_text_width = template.shape[1] - 200
        max_text_height = template.shape[0] - 200

        font_path = "AlexBrush-Regular.ttf"
        font_size = 1
        font = ImageFont.truetype(font_path, font_size)

        temp_img = Image.new('RGB', (max_text_width, max_text_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(temp_img)
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        while text_width <= max_text_width and text_height <= max_text_height and font_size < 100:
            font_size += 1
            font = ImageFont.truetype(font_path, font_size)
            text_bbox = draw.textbbox((0, 0), name, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        text_x = (template.shape[1] - text_width) // 2
        text_y = (template.shape[0] - text_height) // 2 - 30

        font_color = (100, 100, 100)  # Light black color in RGB format
        img_pil = Image.fromarray(template)
        draw = ImageDraw.Draw(img_pil)
        draw.text((text_x, text_y), name, font=font, fill=font_color)

        template_with_text = np.array(img_pil)
        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template_with_text)

cleanup_data()
generate_certificates()

