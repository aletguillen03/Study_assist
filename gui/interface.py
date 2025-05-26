import tkinter as tk
from tkinter import filedialog, scrolledtext
from core import pdf_parser

def launch_app():
    def open_pdf():
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            content = pdf_parser.extract_text_from_pdf(path)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

        with open("data/texto_extraido.txt", "w", encoding="utf-8") as f:
            f.write(content)

    root = tk.Tk()
    root.title("Asistente de Estudio IA")
    root.geometry("800x600")

    btn_open = tk.Button(root, text="Cargar PDF", command=open_pdf)
    btn_open.pack(pady=10)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    root.mainloop()