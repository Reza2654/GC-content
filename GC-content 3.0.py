import tkinter as tk
from tkinter import messagebox
from tkinter.colorchooser import askcolor

def calculate_sequence():
    dna_sequence = dna_entry.get().upper()
    
    if not dna_sequence:
        messagebox.showerror("Error", "Please enter a DNA sequence.")
        return
    
    valid_bases = set("ACGT")
    if not all(base in valid_bases for base in dna_sequence):
        messagebox.showerror("Error", "Invalid characters in DNA sequence.")

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

def show_about_info():
    about_info = """
    This software was created by Reza.
    Version: 3.0
    Date: 2023-10-06
    """
    messagebox.showinfo("About", about_info)

def open_settings():
    color = askcolor()[1]
    window.configure(bg=color)

def open_regulators():
    regulators_window = tk.Toplevel()
    regulators_window.title("Regulators")
    
    def set_background_color():
        color = askcolor()[1]
        window.configure(bg=color)
    
    def set_button_color():
        color = askcolor()[1]
        calculate_button.config(bg=color)
        calculate_length_button.config(bg=color)
        about_button.config(bg=color)
        settings_button.config(bg=color)
        background_color_button.config(bg=color)
        button_color_button.config(bg=color)
    
    def set_text_color():
        color = askcolor()[1]
        calculate_button.config(fg=color)  # تغییر رنگ متن دکمه "Calculate"
        calculate_length_button.config(fg=color)  # تغییر رنگ متن دکمه "Calculate Length"
        about_button.config(fg=color)  # تغییر رنگ متن دکمه "About"
        settings_button.config(fg=color)  # تغییر رنگ متن دکمه "Settings"
        background_color_button.config(fg=color)  # تغییر رنگ متن دکمه "Background Color"
        button_color_button.config(fg=color)  # تغییر رنگ متن دکمه "Button Color"
    
    background_color_button = tk.Button(regulators_window, text="Background Color", command=set_background_color)
    background_color_button.pack(padx=10, pady=5)
    
    button_color_button = tk.Button(regulators_window, text="Button Color", command=set_button_color)
    button_color_button.pack(padx=10, pady=5)

    text_color_button = tk.Button(regulators_window, text="Text Color", command=set_text_color)
    text_color_button.pack(padx=10, pady=5)

window = tk.Tk()
window.title("DNA and RNA Sequence Calculator")
window.geometry("330x330")
window.resizable(False, False)

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

settings_button = tk.Button(window, text="Settings", command=open_regulators)
settings_button.pack(side="bottom", anchor="se", padx=10, pady=10)

about_button = tk.Button(window, text="About", command=show_about_info, bg="Gray")
about_button.pack(side="bottom", anchor="se", padx=10, pady=10)

window.mainloop()
