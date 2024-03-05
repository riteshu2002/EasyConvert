import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
from docx2pdf import convert

def convert_file():
    file_path = file_path_entry.get() # taking file path as input
    convert_to = format_var.get() # asking for pdf pr docx which you like to convert

    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    if convert_to == "PDF": # IF you want pdf
        convert_to_pdf(file_path)
    elif convert_to == "DOCX": # if you want docx
        convert_to_docx(file_path)

def convert_to_pdf(file_path): # For converting into pdf file
    new_pdf_path = file_path.replace(".docx", "_converted.pdf")
    convert(file_path, new_pdf_path)
    messagebox.showinfo("Success", "Conversion to PDF successful.\nOutput file: " + new_pdf_path)

def convert_to_docx(file_path): # For converting into docx file
    old_pdf = file_path
    new_doc = file_path.replace(".pdf", "_converted.docx")
    obj = Converter(old_pdf)
    obj.convert(new_doc)
    obj.close()
    messagebox.showinfo("Success", "Conversion to DOCX successful.\nOutput file: " + new_doc)

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

# Creating main window
root = tk.Tk()
root.title("File Converter")

# File Path Entry
file_path_label = tk.Label(root, text="File Path:")
file_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=3, padx=5, pady=5)

# Format Selection
format_label = tk.Label(root, text="Convert to:")
format_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
formats = ["PDF", "DOCX"]
format_var = tk.StringVar(root)
format_var.set("PDF")
format_menu = tk.OptionMenu(root, format_var, *formats)
format_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_file)
convert_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
