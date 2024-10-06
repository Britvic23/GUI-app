from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# -----------------uploading image------------------
def upload():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    if file_path:
        img = Image.open(file_path)
        add_watermark(img, file_path)

# -----------------adding watermark-----------------
def add_watermark(img, file_path):
    watermark_text = website_entry.get()

    draw = ImageDraw.Draw(img)  # Fix 1: Correct use of ImageDraw
    font = ImageFont.truetype("arial.ttf", 36)

    # Using textbbox() to get text width and height
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Position the watermark at the bottom-right corner
    width, height = img.size
    position = (width - text_width - 10, height - text_height - 10)

    # Add watermark text
    draw.text(position, watermark_text, (255, 255, 255), font=font)

    # Save the image with a new name
    watermarked_file_path = file_path.replace(".", "_watermarked.")
    img.save(watermarked_file_path)

    # Notify the user
    success_label.config(text=f"Watermark added! Saved as: {watermarked_file_path}")

# -------------------window setup-------------------
window = Tk()
window.title("Watermark Adder")
window.config(padx=50, pady=50)

title = Label(text="Upload the image")
title.grid(row=1, column=2)

upload_button = Button(text="Upload", command=upload)
upload_button.grid(row=2, column=2)

website_label = Label(text="Enter the watermark")
website_label.grid(row=3, column=1)

website_entry = Entry(width=30)
website_entry.grid(row=3, column=3)

success_label = Label(text="")
success_label.grid(row=4, column=2)

window.mainloop()