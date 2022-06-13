import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

BACKGROUND_COLOR = "#B1DDC6"
WIDTH = 600
HEIGHT = 451
STD_MARGIN = 5
IMAGE_SIZE = (WIDTH, HEIGHT)


def upload_image():
    new_win = tk.Toplevel(window)
    new_win.title('Upload Image')
    new_win.config(padx=10, pady=10)
    filename = tk.filedialog.askopenfilename()
    raw_image = Image.open(filename)
    raw_image.thumbnail(IMAGE_SIZE)
    prep_image = ImageTk.PhotoImage(raw_image)
    canvas = tk.Canvas(new_win, width=WIDTH + STD_MARGIN * 2, height=HEIGHT + STD_MARGIN * 2)
    image_display = canvas.create_image(STD_MARGIN, STD_MARGIN, anchor='nw', image=prep_image)
    canvas.grid(columnspan=2, column=0, row=0)
    ttk.Button(new_win, text="Save").grid(column=1, row=1)

    new_win.mainloop()


window = tk.Tk()
window.title('Image Marker')

image = Image.open('./images/image_holder.jpg')
image.thumbnail(IMAGE_SIZE)
py_image = ImageTk.PhotoImage(image)

ttk.Button(window, text="Upload", command=upload_image).grid(column=0, row=1)
ttk.Button(window, text="Save").grid(column=1, row=1)

window.mainloop()


# watermark
