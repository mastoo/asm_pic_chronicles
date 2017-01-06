import os
import subprocess as subp
from shutil import copyfile


VERSION = "v1.0"
RELEASE_FOLDER  = "release"
DOCS_FOLDER     = RELEASE_FOLDER+"/docs"
TOOLS_FOLDER    = RELEASE_FOLDER+"/tools"

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        print("CREATING: "+folder_name)
        os.makedirs(folder_name)


def create_release_folder():
    make_folder(RELEASE_FOLDER)
    make_folder(DOCS_FOLDER)
    make_folder(TOOLS_FOLDER)

def copy_arduino_programmer_files():
    copyfile("./src/arduino_pic_prog/docs/pic_programmer_howto.md",DOCS_FOLDER+"/pic_programmer_howto.md")
    copyfile("./src/arduino_pic_prog/schematic/Connections.png",DOCS_FOLDER+"/Connections.png")
    copyfile("./src/arduino_pic_prog/sketch/PIC18f_auto/PIC18f_auto.ino",TOOLS_FOLDER+"/PIC18f_auto.ino")
    print("PRECOMPILED BINARY OF Arduino_Pic18F2550_programmer.exe WILL BE USED")
    copyfile("./src/arduino_pic_prog/burner/bin/Arduino_Pic18F2550_programmer.exe",TOOLS_FOLDER+"/Arduino_Pic18F2550_programmer.exe")

if __name__ == "__main__":
    print("ASM PIC CHRONICLES BUILDER: "+VERSION)
    try:
        create_release_folder()
        copy_arduino_programmer_files()
        
    except Exception as e:
        print("Error: "+str(e))