# import cv2

# list_of_names = []

# def cleanup_data():
#     with open("names.txt") as file:
#         for line in file:
#             list_of_names.append(line.strip())

# def calculate_font_size(template, name, max_width, max_height):
#     font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
#     font_scale = 3.0 
    
#     while True:
#         text_size, _ = cv2.getTextSize(name, font, font_scale, 1)
        
#         if text_size[0] <= max_width and text_size[1] <= max_height:
#             break
        
#         font_scale -= 0.1
    
#     return font_scale

# def generate_certificates():
#     for name in list_of_names:
#         template = cv2.imread("certificate_template.png")
        
#         max_text_width = template.shape[1] - 200  
#         max_text_height = template.shape[0] - 200  

#         font_scale = calculate_font_size(template, name, max_text_width, max_text_height)
        
#         font_thickness = 2
#         text_size, _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, font_scale, font_thickness)
#         text_x = (template.shape[1] - text_size[0]) // 2
#         text_y = (template.shape[0] - text_size[1]) // 2 + 50  
        
#         font_color = (80, 80, 80) 
#         cv2.putText(template, name, (text_x, text_y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, font_scale, font_color, font_thickness, cv2.LINE_AA)

#         cv2.imwrite(f'generated-certificate-data/{name}.jpg', template)

# cleanup_data()
# generate_certificates()


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

        max_text_width = template.shape[1] - 200
        max_text_height = template.shape[0] - 200

        # Load the custom font
        font_path = "AlexBrush-Regular.ttf"
        font_size = 1
        font = ImageFont.truetype(font_path, font_size)

        # Create a temporary image and draw text on it to get text size
        temp_img = Image.new('RGB', (max_text_width, max_text_height), color = (255, 255, 255))
        draw = ImageDraw.Draw(temp_img)
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Calculate font size to fit within the specified width and height
        while text_width <= max_text_width and text_height <= max_text_height:
            font_size += 1
            font = ImageFont.truetype(font_path, font_size)
            text_bbox = draw.textbbox((0, 0), name, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Calculate text position
        text_x = (template.shape[1] - text_width) // 2
        text_y = (template.shape[0] - text_height) // 2 + 50

        # Render text on the template
        font_color = (80, 80, 80)
        img_pil = Image.fromarray(template)
        draw = ImageDraw.Draw(img_pil)
        draw.text((text_x, text_y), name, font=font, fill=font_color)

        # Convert back to OpenCV format and save the image
        template_with_text = np.array(img_pil)
        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template_with_text)

cleanup_data()
generate_certificates()
