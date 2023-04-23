import pywhatkit
from PIL import Image
from FILEPATH import input_path
# FILE PATH
file_name = input("Enter file name with extension: ")
final_path = input_path + file_name
# Opening Image
try:
    inp = Image.open(final_path)
# Converting to ASCII
    pywhatkit.image_to_ascii_art(final_path,'Image2Ascii/final') 
except Exception as e:
    #\033[1;31m for Red Color
    #\033[1;32m for Green Color
    print(f"\033[1;31m [!]Exception {e} encountered[!]")
    print("\033[1;32m Exiting program, run again")
    quit()

read_file = open("Image2Ascii/final.txt","r")
# Reading File
print(read_file.read())
read_file.close()


