import tkinter as tk
from tkinter import ttk
import webbrowser

def open_paper():
    subject = subject_var.get()
    year = year_entry.get()
    session = session_var.get()
    variant = variant_entry.get()
    typeof = type_var.get()

    if subject == "Maths":
        subjectcode = "9709"
    elif subject == "Chemistry":
        subjectcode = "9701"
    elif subject == "Physics":
        subjectcode = "9702"

    if session == "May/June":
      sessionchar = "s"
    elif subject == "October/November":
      sessionchar = "w"
    elif session == "March":
      sessionchar = "m"

    if typeof == "Question Paper":
      typechar = "qp"
    if typeof == "Mark Scheme":
      typechar = "ms"

    yearlast = year[-2:]

    url = f"https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{subjectcode}_{sessionchar}{yearlast}_{typechar}_{variant}.pdf"
    webbrowser.open(url)

# Initialize the main window
root = tk.Tk()
root.title("CIE.py")
root.geometry("900x600")

# Title
type_label = tk.Label(root, text="CIEpy: Past Paper Link Generator")

# Subject code entry
subject_label = tk.Label(root, text="Choose Your Subject")
subject_label.pack()
subject_var = tk.StringVar(value="Maths")
subject_options = ["Maths", "Chemistry", "Physics"]
subject_menu = tk.OptionMenu(root, subject_var, *subject_options)
subject_menu.pack()


# Year entry
year_label = tk.Label(root, text="Choose The Year")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Session selection
session_label = tk.Label(root, text="Choose The Session")
session_label.pack()
session_var = tk.StringVar(value="May/June")
session_options = {"May/June","March","October/November"}
session_menu = tk.OptionMenu(root, session_var, *session_options)
session_menu.pack()

# Variant entry
variant_label = tk.Label(root, text="Choose The Variant and Paper")
variant_label.pack()
variant_entry = tk.Entry(root)
variant_entry.pack()

# Type selection
type_label = tk.Label(root, text="Choose The Type")
type_label.pack()
type_var = tk.StringVar(value="Question Paper")
type_options = ["Question Paper", "Mark Scheme"]
type_menu = tk.OptionMenu(root, type_var, *type_options)
type_menu.pack()

# Submit button
submit_button = tk.Button(root, text="Generate Link", command=open_paper)
submit_button.pack()

# Run the main loop
root.mainloop()
