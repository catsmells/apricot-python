import tkinter as tk
from tkinter import filedialog
from tkhtmlview import HTMLLabel

class viewsystem:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Viewer")
        self.root.geometry("1024x720")

        self.open_button = tk.Button(self.root, text="Open HTML File", command=self.open_file)
        self.open_button.pack()

        self.html_label = HTMLLabel(self.root, html="", width=1024, height=720, background="gray")
        self.html_label.pack(pady=20, padx=20, fill="both", expand=True)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.html_label.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    viewer = viewsystem(root)
    root.mainloop()
