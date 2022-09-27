from tkinter import *

from PIL import Image, ImageDraw, ImageFont


root = Tk()
root.title("Image Watermarking Desktop App")
root.minsize(width=700, height=700)
root.config(padx=100, pady=200, bg='#9FD996')


#Label
my_label = Label(text="Welcome in program of adding Watermarking sign to your image", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50, bg='#9FD996', fg="#DE8D6D")


def open_file():
    # "/Users/magdalenauchman/Desktop/picture.jpeg"

    image_label = Label(text="Please provide your absolute filepath: ")
    image_label.grid(column=0, row=3)
    new_window = Entry(width=70)
    new_window.grid(column=0, row=4)

    def button_click():
        image_path = new_window.get()
        with Image.open(image_path) as im:
            im.show()
        watermark = watermark_input.get()
        width, height = im.size

        draw = ImageDraw.Draw(im)
        text = watermark

        font = ImageFont.truetype("Arial", 35)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)
        im.show()

        im.save(image_path)



    watermark_input = Entry(width=70)
    watermark_input.grid(column=0, row=8)

    watermark_text = Label(text="What text would you like to add as watermark?")
    watermark_text.grid(column=0, row=7)

    add_watermark_button = Button(text="Add watermark", command=button_click)
    add_watermark_button.grid(column=0, row=9)


#Button
button = Button(text="Upload Image:", fg="#DE8D6D", command=open_file)
button.grid(column=0, row=1)



root.mainloop()