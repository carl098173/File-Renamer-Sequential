import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext


class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")

        self.input_dir = ""
        self.output_dir = ""
        self.file_extension = ""

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, pady=5)

        self.input_button = tk.Button(self.input_frame, text="Select Input Directory",
                                      command=self.select_input_directory)
        self.input_button.pack(side=tk.LEFT, padx=5)

        self.input_label = tk.Label(self.input_frame, text="", width=50, anchor="w")
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill=tk.X, pady=5)

        self.output_button = tk.Button(self.output_frame, text="Select Output Directory",
                                       command=self.select_output_directory)
        self.output_button.pack(side=tk.LEFT, padx=5)

        self.output_label = tk.Label(self.output_frame, text="", width=50, anchor="w")
        self.output_label.pack(side=tk.LEFT, padx=5)

        self.extension_frame = tk.Frame(self.root)
        self.extension_frame.pack(fill=tk.X, pady=5)

        self.extension_label = tk.Label(self.extension_frame, text="File Extension:")
        self.extension_label.pack(side=tk.LEFT, padx=5)

        self.extension_entry = tk.Entry(self.extension_frame, width=10)
        self.extension_entry.pack(side=tk.LEFT, padx=5)

        self.process_button = tk.Button(self.root, text="Process Files", command=self.process_files)
        self.process_button.pack(pady=5)

        self.log_frame = tk.Frame(self.root)
        self.log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, height=20, width=50)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.line_count = 0

    def log(self, message):
        self.line_count += 1
        self.log_text.insert(tk.END, f"{self.line_count}: {message}\n")
        self.log_text.see(tk.END)

    def select_input_directory(self):
        self.input_dir = filedialog.askdirectory(title="Select Input Directory")
        self.input_label.config(text=self.input_dir)
        self.log(f"Selected Input Directory: {self.input_dir}")

    def select_output_directory(self):
        self.output_dir = filedialog.askdirectory(title="Select Output Directory")
        self.output_label.config(text=self.output_dir)
        self.log(f"Selected Output Directory: {self.output_dir}")

    def process_files(self):
        self.file_extension = self.extension_entry.get().strip()

        if not self.input_dir or not self.output_dir:
            messagebox.showerror("Error", "Please select both input and output directories.")
            return

        if not self.file_extension:
            messagebox.showerror("Error", "Please enter a file extension.")
            return

        next_file_number = self.get_next_file_number()
        file_count = 0

        for filename in os.listdir(self.input_dir):
            src_path = os.path.join(self.input_dir, filename)
            if os.path.isfile(src_path) and filename.endswith(self.file_extension):
                new_filename = f"{next_file_number:010}{os.path.splitext(filename)[1]}"
                dst_path = os.path.join(self.output_dir, new_filename)
                shutil.copy2(src_path, dst_path)
                self.log(f"Copied and renamed {filename} to {new_filename}")
                next_file_number += 1
                file_count += 1

        self.log(f"Processing complete. {file_count} files processed.")

    def get_next_file_number(self):
        existing_files = [f for f in os.listdir(self.output_dir) if
                          f.endswith(self.file_extension) and f[:10].isdigit()]
        existing_numbers = [int(f[:10]) for f in existing_files]
        return max(existing_numbers, default=-1) + 1


if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()
