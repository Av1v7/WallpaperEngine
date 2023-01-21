import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import ctypes

def set_wallpaper(path_to_image):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_image, 0)

def save_image():
    with Image.open(filepath) as image_wallpaper:
        image_wallpaper.save(filepath)
        set_wallpaper(filepath)

def select_image():
    global filepath
    filepath = filedialog.askopenfilename()
    
    image_formats = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".svg", ".raw"]
    if any(filepath.endswith(ext) for ext in image_formats):
        global image

        root.iconbitmap(filepath)
        image_wallpaper = Image.open(filepath)
        image_wallpaper.save("HomeScreen.ico")
        root.iconbitmap("HomeScreen.ico")
        
        image = ImageTk.PhotoImage(image_wallpaper)
        image_label.config(image=image)
        image_label.image = image
    else:
        messagebox.showerror(title="Error !", message="File Needs To Be An Image.")

root = tk.Tk()
root.title("Set Wallpaper")
x = int(root.winfo_screenwidth()/2 - 250)
y = int(root.winfo_screenheight()/2 - 250)
root.geometry("500x500+{}+{}".format(x, y))
root.configure(bg='white')
root.resizable(width=False, height=False)

select_button = tk.Button(root, text="Select Image", command=select_image, bg='#242424', fg='white', font=('Arial', 12))
select_button.pack(side="top", fill="x")

save_button = tk.Button(root, text="Save", command=save_image, bg='#242424', fg='white', font=('Arial', 12))
save_button.pack(side="bottom", fill="x")

image_label = tk.Label(root, bg='white')
image_label.pack()

root.mainloop()