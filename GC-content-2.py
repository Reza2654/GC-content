import tkinter as tk
from tkinter import messagebox

def calculate_sequence():
    dna_sequence = dna_entry.get().upper()  # توالی را به حروف بزرگ تبدیل می‌کنیم
    
    # اگر توالی وارد نشده باشد، پیام خطا نمایش داده می‌شود
    if not dna_sequence:
        messagebox.showerror("Error", "Please enter a DNA sequence.")
        return
    
    # بررسی صحت توالی وجود A، C، G، T و حروف دیگر
    valid_bases = set("ACGT")
    if not all(base in valid_bases for base in dna_sequence):
        messagebox.showerror("Error", "Invalid characters in DNA sequence.")

    
    # محاسبه توالی RNA و محتوای GC
    rna_sequence = dna_sequence.replace('T', 'U')
    gc_content = (dna_sequence.count('G') + dna_sequence.count('C')) / len(dna_sequence) * 100
    
    result_text = f'DNA Sequence: {dna_sequence}\nRNA Sequence: {rna_sequence}\nGC Content (%): {gc_content:.2f}%'
    result_label.config(text=result_text)

def calculate_length():
    dna_sequence = dna_entry.get().upper()
    a_count = dna_sequence.count('A')
    c_count = dna_sequence.count('C')
    g_count = dna_sequence.count('G')
    t_count = dna_sequence.count('T')

    length = len(dna_sequence)
    
    result_text = f'A Count: {a_count}\nC Count: {c_count}\nG Count: {g_count}\nT Count: {t_count}\nLength: {length} bases'
    result_label.config(text=result_text)

# ایجاد پنجره
window = tk.Tk()
window.title("DNA and RNA Sequence Calculator")

# ایجاد ویجت‌ها و تنظیمات
label = tk.Label(window, text="Enter DNA Sequence:")
label.pack(pady=10)

dna_entry = tk.Entry(window, width=50)
dna_entry.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_sequence)
calculate_button.pack(side="left", padx=5)

calculate_length_button = tk.Button(button_frame, text="Calculate Length", command=calculate_length)
calculate_length_button.pack(side="left", padx=5)

result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

# شروع حلقه اصلی
window.mainloop()
