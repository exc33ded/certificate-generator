import cv2

list_of_names = []

def cleanup_data():
    with open("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())

def calculate_font_size(template, name, max_width, max_height):
    font = cv2.FONT_HERSHEY_TRIPLEX 
    font_scale = 2.0 
    
    while True:
        text_size, _ = cv2.getTextSize(name, font, font_scale, 1)
        
        if text_size[0] <= max_width and text_size[1] <= max_height:
            break
        
        font_scale -= 0.1
    
    return font_scale

def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("certificate_template.png")
        
        max_text_width = template.shape[1] - 200  
        max_text_height = template.shape[0] - 200  

        font_scale = calculate_font_size(template, name, max_text_width, max_text_height)
        
        font_thickness = 2
        text_size, _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_TRIPLEX, font_scale, font_thickness)
        text_x = (template.shape[1] - text_size[0]) // 2
        text_y = (template.shape[0] - text_size[1]) // 2 + 50  
        
        font_color = (80, 80, 80) 
        cv2.putText(template, name, (text_x, text_y), cv2.FONT_HERSHEY_TRIPLEX, font_scale, font_color, font_thickness, cv2.LINE_AA)

        cv2.imwrite(f'generated-certificate-data/{name}.jpg', template)

cleanup_data()
generate_certificates()
