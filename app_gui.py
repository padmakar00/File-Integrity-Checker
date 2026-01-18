import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from backend_integrity import integrity_check

def browse_folder():
    folder = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder)

def run_scan():
    folder = entry_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder")
        return

    btn_scan.config(state=tk.DISABLED)
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Scanning files, please wait...\n")

    # Run backend in separate thread
    threading.Thread(target=scan_task, args=(folder,), daemon=True).start()

def scan_task(folder):
    result = integrity_check(folder)

    # Update GUI safely
    app.after(0, update_output, result)

def update_output(result):
    output.delete(1.0, tk.END)

    for key, files in result.items():
        output.insert(tk.END, f"\n[{key}]\n")
        if files:
            for file in files:
                output.insert(tk.END, f"{file}\n")
        else:
            output.insert(tk.END, "None\n")

    btn_scan.config(state=tk.NORMAL)
    messagebox.showinfo("Completed", "Integrity check finished successfully")
#       GUI SETUP 
app = tk.Tk()
app.title("File Integrity Checker")
app.geometry("600x450")

tk.Label(app, text="Select Directory to Monitor").pack(pady=5)

entry_path = tk.Entry(app, width=60)
entry_path.pack(pady=5)

tk.Button(app, text="Browse", command=browse_folder).pack(pady=5)

btn_scan = tk.Button(app, text="Start Integrity Check", command=run_scan)
btn_scan.pack(pady=10)

output = tk.Text(app, height=18, width=70)
output.pack(pady=5)

app.mainloop()
