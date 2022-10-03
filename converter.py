import my_gui
from PIL import Image
from tkinter import filedialog
import shutil, os, sys

#(appends image path to image_paths list), copies image to script directory, and displays it in the gui listbox
def openFile():
    #global image_paths
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


#function using the save() method of the Pillow library which determins the desired file format via string
#image = internal image name used for convertion  e.g. image0
#format = user specified image format to convert into
#imageKey = original(user) image name e.g. birthday picture.jpg
#savePath = directory to save the image into
def convertIm(image, format, imageKey, savePath):
    a, b = os.path.splitext(imageKey)
    newImageKey = a + format
    f, e = os.path.splitext(image)
    outfile = f + format     #.jpg, .pdf   ;  save() converts file into specified format
    if image != outfile:
        try:
            with Image.open(image) as im:
                im.save(outfile)           #save() automaticly detects the image type which, e.g. outfile = picture.pdf  ->  save() will convert the image into a pdf
                image_key_value.update({newImageKey:outfile})
                my_gui.insert_listbox(newImageKey)
                savePath = savePath + "/" + newImageKey
                print(savePath)
                shutil.copy2(outfile, savePath)
        except OSError:
            print("cannot convert", image, format, imageKey)

#deletes all internal images in the script directory 
def deleteImagesOnStart():   
    my_gui.image_listbox.delete(0, 'end')
    directory = os.fsencode(sys.path[0])   #sys.path[0] returns script directory
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

#deletes single file, currently not used
def deleteImage(fileClone):
    try:
        os.remove(fileClone)
    except FileNotFoundError:
        print("That file was not found")
    except PermissionError:
        print("You do not have permission to delete that")

#image_paths = []
image_counter = 0      #counter to help name the file clones

image_key_value = {}   #dictionary to connect the original filenames with the program-internal filenames
