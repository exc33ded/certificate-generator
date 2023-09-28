import cv2

list_of_names = []

def cleanup_data():
    with open("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def calculate_font_size(template, name, max_width, max_height):
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 2.0  # Initial font scale (increased)
    
    while True:
        # Calculate the text size with the current font scale
        text_size, _ = cv2.getTextSize(name, font, font_scale, 1)
        
        # Check if the text size fits within the specified region
        if text_size[0] <= max_width and text_size[1] <= max_height:
            break
        
        # Reduce the font size
        font_scale -= 0.1
    
    return font_scale

def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("certificate_template.png")
        
        # Specify the maximum width and height for text
        max_text_width = template.shape[1] - 200  # Adjust this value as needed
        max_text_height = template.shape[0] - 200  # Adjust this value as needed
        
        # Calculate the font size to fit within the specified region
        font_scale = calculate_font_size(template, name, max_text_width, max_text_height)
        
        # Calculate the text position in the center
        font_thickness = 2
        text_size, _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_COMPLEX, font_scale, font_thickness)
        text_x = (template.shape[1] - text_size[0]) // 2
        text_y = (template.shape[0] - text_size[1]) // 2
        
        # Add the text to the template image
        cv2.putText(template, name, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)
        
        # Save the generated certificate
        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template)

cleanup_data()
generate_certificates()
