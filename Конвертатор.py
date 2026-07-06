import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from docx import Document

# Функция для конвертации DOCX в CSV
def convert_docx_to_csv(filepath, output_folder):
    doc = Document(filepath)
    data = []
    
    for para in doc.paragraphs:
        data.append([para.text])
    
    df = pd.DataFrame(data, columns=['Text'])
    output_path = os.path.join(output_folder, os.path.basename(filepath).replace('.docx', '.csv'))
    df.to_csv(output_path, index=False)
    return output_path

# Функция для конвертации TXT в CSV
def convert_txt_to_csv(filepath, output_folder):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    df = pd.DataFrame(data, columns=['Text'])
    output_path = os.path.join(output_folder, os.path.basename(filepath).replace('.txt', '.csv'))
    df.to_csv(output_path, index=False)
    return output_path

# Функция для конвертации PDF в CSV
def convert_pdf_to_csv(filepath, output_folder, PdfReader=None):
    from PyPDF2 import PdfReader
    reader = PdfReader(filepath)
    data = []
    
    for page in reader.pages:
        data.append([page.extract_text()])
    
    df = pd.DataFrame(data, columns=['Text'])
    output_path = os.path.join(output_folder, os.path.basename(filepath).replace('.pdf', '.csv'))
    df.to_csv(output_path, index=False)
    return output_path

class FileConverterApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Converter")
        self.geometry("400x300")
        
        # Выбор файла
        self.selected_file = None
        
        # Кнопка "Загрузить"
        self.load_button = ttk.Button(self, text="Загрузить", command=self.load_file)
        self.load_button.pack(pady=10)
        
        # Кнопка "Поменять"
        self.convert_button = ttk.Button(self, text="Поменять", command=self.convert_file)
        self.convert_button.pack(pady=10)
        
        # Кнопка "Загрузить в папку"
        self.save_button = ttk.Button(self, text="Загрузить файл в папку", command=self.save_to_folder)
        self.save_button.pack(pady=10)
        
        self.output_folder = None
        
    def load_file(self):
        self.selected_file = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ("Word Files", "*.docx"), ("Text Files", "*.txt"), ("PDF Files", "*.pdf")))
        if self.selected_file:
            messagebox.showinfo("File Selected", f"Выбран файл: {self.selected_file}")
    
    def convert_file(self):
        if self.selected_file:
            if self.selected_file.endswith('.docx'):
                output_path = convert_docx_to_csv(self.selected_file, self.output_folder or os.getcwd())
            elif self.selected_file.endswith('.txt'):
                output_path = convert_txt_to_csv(self.selected_file, self.output_folder or os.getcwd())
            elif self.selected_file.endswith('.pdf'):
                output_path = convert_pdf_to_csv(self.selected_file, self.output_folder or os.getcwd())
            else:
                messagebox.showerror("Error", "Неподдерживаемый формат файла!")
                return
            
            messagebox.showinfo("Conversion Complete", f"Файл был успешно конвертирован:\n{output_path}")
        else:
            messagebox.showerror("Error", "Сначала загрузите файл!")
    
    def save_to_folder(self):
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            messagebox.showinfo("Directory Selected", f"Файлы будут сохранены в: {self.output_folder}")


if __name__ == "__main__":
    app = FileConverterApplication()
    app.mainloop()

