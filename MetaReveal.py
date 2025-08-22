import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ExifTags

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.tiff *.bmp")]
    )
    if not file_path:
        return
    
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()

        output_text.delete("1.0", tk.END)  
        output_text.insert(tk.END, f"File: {file_path}\n\n")

        if exif_data:
            for tag_id, value in exif_data.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                output_text.insert(tk.END, f"{tag:25}: {value}\n")
        else:
            output_text.insert(tk.END, "No EXIF metadata found.\n")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read metadata: {e}")


root = tk.Tk()
root.title("Image Metadata Viewer (EXIF Tool)")
root.geometry("600x400")

btn_open = tk.Button(root, text="Open Image", command=open_image, font=("Arial", 12))
btn_open.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10))
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
