import tkinter as tk
from tkinter import filedialog, messagebox

def filter_lines(filename, keywords):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if all(keyword.lower() in line.lower() for keyword in keywords)]

def browse_file():
    filename = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    file_label.config(text=filename)

def apply_filter():
    filename = file_label.cget("text")
    keywords = entry.get().split(',')
    keywords = [keyword.strip() for keyword in keywords]  # Remove spaces

    try:
        global filtered_lines
        filtered_lines = filter_lines(filename, keywords)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, '\n'.join(filtered_lines))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def export_results():
    if filtered_lines:
        export_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if not export_file:
            return
        with open(export_file, 'w') as f:
            f.write('\n'.join(filtered_lines))
    else:
        messagebox.showerror("Error", "No data to export. Please filter the data first.")

root = tk.Tk()
root.title("TxtFilterGUI")
root.geometry("1280x720")

frame = tk.Frame(root)
frame.pack(pady=10)

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.pack(side="left")

file_label = tk.Label(frame, text="")
file_label.pack(side="left")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

filter_button = tk.Button(root, text="Apply Filter", command=apply_filter)
filter_button.pack(pady=10)

export_button = tk.Button(root, text="Export Results", command=export_results)
export_button.pack(pady=10)

result_text = tk.Text(root)
result_text.pack(fill='both', expand=True)

filtered_lines = []

root.mainloop()
