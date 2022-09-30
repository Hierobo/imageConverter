import shutil
from PIL import Image
import PIL
import my_gui, os

def convertIm(image, format):
    f, e = os.path.splitext(image)
    outfile = f + format     #.jpg, .pdf   ;  save() converts file into specified format
    if image != outfile:
        try:
            with Image.open(image) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", image)

convertIm("Schadensort.jpg", ".pdf")