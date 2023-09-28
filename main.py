import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

list_of_names = []

def cleanup_data():
    with open("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def calculate_text_size(draw, text, font):
    # Calculate text size using the specified font
    text_width, text_height = draw.textsize(text, font=font)
    return text_width, text_height

def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("certificate_template.png")
        pil_template = Image.fromarray(template)
        draw = ImageDraw.Draw(pil_template)
        
        # Load your custom TTF font file and set the font size
        custom_font = ImageFont.truetype("AlexBrush-Regular.ttf", size=100)  # Adjust the size as needed
        
        # Calculate text size and position
        text = name
        text_width, text_height = custom_font.getsize(text)
        text_x = (template.shape[1] - text_width) // 2
        text_y = (template.shape[0] - text_height) // 2 + 50  # Adjust this value as needed
        
        # Set the font color (light black)
        font_color = (80, 80, 80)  # RGB values for dark gray
        
        # Add the text to the image
        draw.text((text_x, text_y), text, fill=font_color, font=custom_font)
        
        # Convert the image back to OpenCV format
        template = np.array(pil_template)
        
        # Save the generated certificate
        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template)

cleanup_data()
generate_certificates()
