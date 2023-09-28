import cv2

list_of_names = []

def cleanup_date():
    with open("names.txt") as file:
        for line in file:
            print(line)
            
cleanup_date()

