import pywhatkit
from PIL import Image
from FILEPATH import input_path
# FILE PATH
def get_filepath():
    file_name = input("Enter file name with extension: ")
    final_path = input_path + file_name
    return final_path
# Opening Image
def open_image(final_path):
    try:
        inp = Image.open(final_path)
    # Converting to ASCII
        pywhatkit.image_to_ascii_art(final_path,'Image2ASCII/final') 
    except Exception as e:
        #\033[1;31m for Red Color
        #\033[1;32m for Green Color
        print(f"\033[1;31m [!]Exception {e} encountered[!]")
        print("\033[1;32m Exiting program, run again")
        quit()
    read_file = open("Image2ASCII/final.txt","r")
    # Reading File
    print(read_file.read())
    read_file.close()

def main():
    open_image(get_filepath())

if __name__ == "__main__":
    main()