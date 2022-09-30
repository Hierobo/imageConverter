from tkinter import*
from tkinter import filedialog
import os, sys
import converter

selection = []

def insert_listbox(imageName):
    global image_listbox
    image_listbox.insert(image_listbox.size(), imageName)

def listbox_delete():
    for index in reversed(image_listbox.curselection()):
        converter.deleteImage(converter.image_key_value.get(image_listbox.get(index)))
        converter.image_key_value.pop(image_listbox.get(index))
        image_listbox.delete(index)

def get_path():
    input = path_entry.get()
    print(input)

def delete():
    path_entry.delete(0, END)                #deletes all characters in entry box

def display():
    pass

def add_image():
    converter.openFile()

def deleteImagesOnStart():
    converter.deleteImagesOnStart()

def convert_and_save():
    global selection
    for index in image_listbox.curselection():
        selection.append(image_listbox.get(index))

    image_listbox.place_forget()
    format_listbox.place(x=42, y=110)

    add_image_button.place_forget()
    delete_all_button.place_forget()
    delete_selected_button.place_forget()
    convert_and_save_button.place_forget()

    choose_format_button.place(x=350,y=110)


def get_format():
    format = format_listbox.get(format_listbox.curselection())
    save_path = filedialog.askdirectory()
    for image in selection:
        converter.convertIm(converter.image_key_value.get(image), format, image, save_path)

    choose_format_button.place_forget()
    add_image_button.place(x=350,y=110)
    delete_all_button.place(x=350,y=180)
    delete_selected_button.place(x=350,y=250)
    convert_and_save_button.place(x=350,y=320)

    format_listbox.place_forget()
    image_listbox.place(x=42, y=110)


def run_gui():                              #start the GUI and waits for inputs, deletes all internal images on start
    global window
    window.mainloop()

fog = "#171510"            #standard foreground color
bag ='#ebc167'             #standard background color


window = Tk()
window.geometry("720x720")
window.title("EZ File Format")
icon = PhotoImage(file="Logo.png")      #converts the logo file into a PhotoImage
window.iconphoto(True, icon)            #sets the PhotoImage as the logo in the top left
window.config(background="#a7b8ad")     #sets background color

photo = PhotoImage(file="Logo.png")

path_entry = Entry(window,
                   font=('Arial', 20, 'bold') )
path_submit = Button(window, text='submit path', command=get_path, font=('Arial', 20, 'bold'))
path_entry_delete = Button(window, text='delete', command=delete, font=('Arial', 20, 'bold'))
#path_entry.pack(side=LEFT)
#path_submit.pack(side=RIGHT)
#path_entry_delete.pack(side=RIGHT)

label = Label(window,
              text="File Formater",
              font=('Arial', 20, 'bold'),
              fg=fog,                   #text color
              bg=bag,                   #widget background color
              relief=RAISED,                  #relief defines the boarder type  SUNKEN
              bd=5,                           #defines boarder width, default is 1
              padx=20,                        #20 pixels of space between text and boarder on x-axis
              pady=10,                        #10 pixels of space between text and boarder in y-axis
              #image=photo                   #puts photo in widget, replaces text
              #compound="bottom"
              state=ACTIVE                    #if DISABLED disables button
              )
x = IntVar()
check_button = Checkbutton(window,
                           text="I agree that the creator of this program is not responsible \nfor potential damage done to my files",
                           variable=x,
                           onvalue=1,         #default = 1
                           offvalue=0,        #default = 0
                           command=display,
                           font=("Arial",20),
                           fg=fog,
                           bg=bag,
                           padx=20,                        #20 pixels of space between text and boarder on x-axis
                           pady=10,                        #10 pixels of space between text and boarder in y-axis
                           #image=...
                           #compund="left"
    )

add_image_button = Button(window, text="add image", command=add_image,  #function name without parantheses! callback
             font=("Arial", 20),
             #fg=fog,
             #bg=bag,
             #activeforeground='green',
             #activebackground='black')
             #state=ACTIVE,   #if DISABLED disables button
             #relief=RAISED,  # relief defines the boarder type  SUNKEN
             #bd=5,            # defines boarder width, default is 1
             #padx=20,           # 20 pixels of space between text and boarder on x-axis
             #pady=10,
             )
add_image_button.place(x=350,y=110)

delete_all_button = Button(window, text="delete all images", command=deleteImagesOnStart, font=("Arial", 20))
delete_all_button.place(x=350, y=180)   #gives option to clear program of all input images

image_listbox = Listbox(window,font=("Arial", 20), selectmode=MULTIPLE)
image_listbox.place(x=42, y=110)

delete_selected_button = Button(window, text="delete selected images",font=("Arial", 20), command=listbox_delete)
delete_selected_button.place(x=350, y=250)

convert_and_save_button = Button(window, text="convert and save", font=("Arial", 20), command=convert_and_save)
convert_and_save_button.place(x=350, y=320)

format_listbox = Listbox(window, font=("Arial", 20))     #creates a listbox to choose the format the user wants the image to convert to

format_listbox.insert(format_listbox.size(),".jpg")
format_listbox.insert(format_listbox.size(),".pdf")
format_listbox.insert(format_listbox.size(),".jpeg")
format_listbox.insert(format_listbox.size(),".png")
format_listbox.insert(format_listbox.size(),".pdf")

choose_format_button = Button(window, text='choose format and choose directory to save in', command=get_format, font=('Arial', 20, 'bold'))

label.place(x=42, y=42)

