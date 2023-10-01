import tkinter as tk
from tkinter import messagebox

def calculate_sequence():
    dna_sequence = dna_entry.get()
    
    if not dna_sequence:
        messagebox.showerror("Error", "Please enter a DNA sequence.")
        return
    
    rna_sequence = dna_sequence.replace('T', 'U')
    a_count = dna_sequence.count('A')
    c_count = dna_sequence.count('C')
    g_count = dna_sequence.count('G')
    t_count = dna_sequence.count('T')
    gc_content = (g_count + c_count) / len(dna_sequence) * 100
    
    result_text = f'DNA Sequence: {dna_sequence}\nRNA Sequence: {rna_sequence}\nA Count: {a_count}\nC Count: {c_count}\nG Count: {g_count}\nT Count: {t_count}\nGC Content (%): {gc_content:.2f}%'
    result_label.config(text=result_text)

# ایجاد پنجره
window = tk.Tk()
window.title("DNA and RNA Sequence Calculator")

# ایجاد ویجت‌ها و تنظیمات
label = tk.Label(window, text="Enter DNA Sequence:")
label.pack(pady=10)

dna_entry = tk.Entry(window, width=50)
dna_entry.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_sequence)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

# شروع حلقه اصلی
window.mainloop()
