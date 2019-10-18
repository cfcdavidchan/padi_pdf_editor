import tkinter, os
from tkinter import messagebox
from tkinter import filedialog

root_path = os.getcwd()


top = tkinter.Tk()
top.geometry('640x300')
top.resizable(0, 0)

# pdf_base file area
#hearder
pdf_base_path_label = tkinter.Label(top, text= "pdf base path:", font= ("Courier", 12))
pdf_base_path_label.grid(row= 0, column= 0)
# pdf path_entry
pdf_base_entryText = tkinter.StringVar()
pdf_base_entry = tkinter.Entry(top, textvariable= pdf_base_entryText, width= 40, font= ("Courier", 12))
pdf_base_entryText.set("")
pdf_base_entry.grid(row=1, column= 1)
# pdf file browser
def browser_pdf():
    filename = filedialog.askopenfilename(initialdir= root_path, title= "Select file", filetypes= (("pdf files","*.pdf *.PDF"),("all files","*.*")))
    try:
        pdf_base_entryText.set(filename)
    except:
        pass
pdf_base_button = tkinter.Button(top, text= "Browser", command = browser_pdf)
pdf_base_button.grid(row=1, column= 5, padx= 15)


# blank label
blank_label = tkinter.Label(top, text= "", font= ("Courier", 14))
blank_label.grid(row=2, column= 0)


# student csv file area
#hearder
csv_path_label = tkinter.Label(top, text="Student csv path:", font= ("Courier", 12))
csv_path_label.grid(row= 3, column= 0)
# pdf path_entry
csv_entryText = tkinter.StringVar()
csv_entry = tkinter.Entry(top, textvariable= csv_entryText, width=40, font= ("Courier", 12))
csv_entryText.set("")
csv_entry.grid(row=4, column= 1)
# pdf file browser
def browser_csv():
    filename = filedialog.askopenfilename(initialdir = root_path, title = "Select file", filetypes = (("csv files","*.csv"),("all files","*.*")))
    try:
        csv_entryText.set(filename)
    except:
        pass
pdf_base_button = tkinter.Button(top, text ="Browser", command = browser_csv)
pdf_base_button.grid(row=4, column=5, padx=15)


# blank label
blank_label = tkinter.Label(top, text= "", font= ("Courier", 14))
blank_label.grid(row=5, column= 0)


# storage directory area
#hearder
storage_label = tkinter.Label(top, text="Storage Directory:", font= ("Courier", 12))
storage_label.grid(row= 6, column= 0)
# pdf path_entry
storage_entryText = tkinter.StringVar()
storage_entry = tkinter.Entry(top, textvariable= storage_entryText, width=40, font= ("Courier", 12))
storage_entryText.set("")
storage_entry.grid(row=7, column= 1)
# pdf file browser
def browser_storage():
    filename = filedialog.askdirectory(initialdir = root_path)
    try:
        storage_entryText.set(filename)
    except:
        pass
storage_button = tkinter.Button(top, text ="Browser", command = browser_storage)
storage_button.grid(row=7, column=5, padx=15)


# blank label
blank_label = tkinter.Label(top, text= "", font= ("Courier", 14))
blank_label.grid(row=8, column= 0, pady= 5)

# operating part
loading_entryText = tkinter.StringVar()
loading_label = tkinter.Label(top, textvariable=loading_entryText, font= ("Courier", 12))
loading_label.grid(row= 9, column= 1)
loading_entryText.set("")

def start_button():
    pdf_path = pdf_base_entryText.get()
    csv_path = csv_entryText.get()
    storage_dir_path = storage_entryText.get()
    student_info_list = pdf_editor.csv_to_list(csv_path)
    for student_info in student_info_list:
        pdf_editor.write_pdf(student_info, pdf_path, storage_dir_path)
    loading_entryText.set('Done!')

storage_button = tkinter.Button(top, text ="Start", command = start_button, font= ("Courier", 12), height = 6, width = 7)
storage_button.grid(row=9, column=5)

# version and creater label
version_label = tkinter.Label(top, text="\n\n\n\n\n\nVersion: 1.0\nDeveloper:cfcdavidchaan", font= ("Courier", 10), anchor='nw')
version_label.grid(row=9, column= 0, sticky='w')


top.mainloop()