import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from PIL import ImageTk, ImageDraw, ImageFont

BACKGROUND_COLOR = "#B1DDC6"
WIDTH = 600
HEIGHT = 451
STD_MARGIN = 5
IMAGE_SIZE = (WIDTH, HEIGHT)
images = {}


window = tk.Tk()
window.title('Image Marker')

image = Image.open('./images/image_holder.jpg')
image.thumbnail(IMAGE_SIZE)
py_image = ImageTk.PhotoImage(image)


def upload_image():
    new_win = tk.Toplevel(window)
    new_win.title('Upload Image')
    new_win.config(padx=10, pady=10)
    with Image.open(tk.filedialog.askopenfilename()) as raw_image:
        raw_image.thumbnail(IMAGE_SIZE)
        images['raw_image'] = raw_image
        prep_image = ImageTk.PhotoImage(raw_image)
    canvas = tk.Canvas(new_win, width=WIDTH + STD_MARGIN * 2, height=HEIGHT + STD_MARGIN * 2)
    image_display = canvas.create_image(STD_MARGIN, STD_MARGIN, anchor='nw', image=prep_image)
    canvas.grid(columnspan=2, column=0, row=0)
    watermark = ttk.Entry(new_win, width=40)
    watermark.grid(columnspan=2, column=0, row=1)
    ttk.Button(new_win, text="Save", command=lambda: save_img()).grid(column=1, row=2)
    ttk.Button(new_win, text="Paste Watermark", command=lambda: paste_watermark()).grid(column=0, row=2)

    def paste_watermark():
        im = images['raw_image'].convert("RGBA")
        wm_text = watermark.get()
        width, height = im.size
        txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        font = ImageFont.truetype('./Fonts/Roboto-Regular.ttf', 36)
        textwidth, textheight = draw.textsize(wm_text, font)
        margin = 20
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), wm_text, font=font, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(im, txt)
        images['marked_image'] = out.convert('RGB')
        images['update'] = ImageTk.PhotoImage(images['marked_image'])
        # out.show()
        canvas.itemconfig(image_display, image=images['update'])

    def save_img():
        save_path = './images/watermarked.jpg'
        images['marked_image'].save(save_path)

    new_win.mainloop()


ttk.Button(window, text="Upload", command=upload_image).grid(column=0, row=1)
ttk.Button(window, text="Save").grid(column=1, row=1)

window.mainloop()


# watermark
