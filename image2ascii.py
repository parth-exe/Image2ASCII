from PIL import Image
from pathlib import Path
import os
# FILE PATH
def get_filepath():
    file_name = input("Enter file name with extension: ")
    input_path = str(os.path.join(Path.home(), "Downloads", file_name))
    return input_path

def convert_to_ascii(input_path):
    img = Image.open(input_path).convert('L')
    width, height = img.size
    aspect_ratio = height / width
    width = 80
    height = aspect_ratio * width * 0.55
    img = img.resize((width, int(height)))
    pixels = img.getdata()
    chars = ["o", "x", "!", "&", "$", "$", "!", ",", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)
    pixels_count = len(new_pixels)
    ascii_image = [
            new_pixels[index : index + width]
            for index in range(0, pixels_count, width)
        ]
    ascii_image = "\n".join(ascii_image)
    print(f"{ascii_image}")
# Opening Image
def main():
    try:
        convert_to_ascii(get_filepath())
    # Converting to ASCII
    except Exception as e:
        #\033[1;31m for Red Color
        #\033[1;32m for Green Color
        print(f"\033[1;31m [!]Exception {e} encountered[!]")
        print("\033[1;32m Exiting program, run again")
        quit()
    

if __name__ == "__main__":
    main()