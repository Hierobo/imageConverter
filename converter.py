import my_gui
from PIL import Image
from tkinter import filedialog
import shutil, os, sys

#appends image path to image_paths list, copies image to script directory
def openFile():
    global image_paths
    global image_counter
    filepath = filedialog.askopenfilename() #opens file explorer to choose image
    a, b = os.path.split(filepath)
    f, e = os.path.splitext(b)
    fileclone = "image" + str(image_counter) + e
    image_counter = image_counter + 1
    image_key_value.update({b:fileclone})   #connects the original image name with the name script name, e.g. dog_picture:image2
    print(image_key_value.items())
    shutil.copy2(filepath, fileclone)       #destination is program folder
    my_gui.insert_listbox(b)                #inserts the image name into the listbox
    #image_paths.append(fileclone)



def convertIm(image, format, imageKey, savePath):
    a, b = os.path.splitext(imageKey)
    newImageKey = a + format
    f, e = os.path.splitext(image)
    outfile = f + format     #.jpg, .pdf   ;  save() converts file into specified format
    if image != outfile:
        try:
            with Image.open(image) as im:
                im.save(outfile)
                image_key_value.update({newImageKey:outfile})
                my_gui.insert_listbox(newImageKey)
                savePath = savePath + "/" + newImageKey
                print(savePath)
                shutil.copy2(outfile, savePath)
        except OSError:
            print("cannot convert", image, format, imageKey)

def convert_and_save(image, format, imageKey):
    a, b = os.path.splitext(imageKey)
    newImageKey = a + format
    f, e = os.path.splitext(image)
    outfile = f + format  # .jpg, .pdf   ;  save() converts file into specified format
    if image != outfile:
        try:
            with Image.open(image) as im:
                im.save(outfile)
                savePath = filedialog.askdirectory   #ask the user for directory to save image in
                print("test")
                print(savePath)
                savePath = savePath + outfile
                print(savePath)
                #shutil.copy2(outfile, savePath)

        except OSError:
            print("cannot convert", image)

def deleteImagesOnStart():   #deletes all internal images on start
    my_gui.image_listbox.delete(0, 'end')
    directory = os.fsencode(sys.path[0])
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("image"):
            try:
                os.remove(filename)
            except FileNotFoundError:
                print("That file was not found")
            except PermissionError:
                print("You do not have permission to delete that")
            continue
        else:
            continue

def deleteImage(fileClone):
    try:
        os.remove(fileClone)
    except FileNotFoundError:
        print("That file was not found")
    except PermissionError:
        print("You do not have permission to delete that")

image_paths = []
image_counter = 0      #counter to help name the file clones

image_key_value = {}   #dictionary to connect the original filenames with the program-internal filenames
