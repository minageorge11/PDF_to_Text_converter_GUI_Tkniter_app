#This app allows you to select a PDF file and the app extract the text content of the PDF file and show it to you. 
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.constants import END, RIGHT, VERTICAL, Y
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("PDF to text converter")

#Create Canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid()

#Create app logo
logo = ImageTk.PhotoImage(Image.open("app_logo.png"))
logo_label = tk.Label(image=logo)
logo_label.grid(row=0, column=0, padx=20, pady=15)

#Create a title in the center to explain the app use
center_title_label = tk.Label(root, text="Select the PDF file you want to retrieve its text", font="ubunto")
center_title_label.grid(row=1, column=0,  pady=30)

#Function that is called after clicking on "Select File button". It creates a select file window, then converts the PDF file into text and put it in a text box.
def open_file():
    select_file_btn_text.set("Loading...")
    pdffile = askopenfile(parent=root, mode="rb", title= "Select a PDF file", filetype=[("pdf file", "*.pdf")])
    if pdffile:
        #Create Text box.
        text_box = tk.Text(root, height=10, width= 50, padx=10, pady=10)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(row=3, column=0)
               
        #Create Scroll bar.
        my_scrollbar = tk.Scrollbar(root, orient=VERTICAL)  #1
        my_scrollbar.grid(row=3, column=1, sticky="NS")  #2
        text_box.config(yscrollcommand=my_scrollbar.set) #3
        my_scrollbar.config(command=text_box.yview)  #4

        #Extracting text from PDF file page by page and place it in the Text box
        read_pdf = PyPDF2.PdfFileReader(pdffile)
        page_count = read_pdf.getNumPages()
        for i in range(page_count):
            page = read_pdf.getPage(i)
            page_content =  page.extractText()
            text_box.insert(END, page_content)
        select_file_btn_text.set("Select File: ")

#String variable for the "select file" button because it changes to "Loading" at the time of selecting the file window appears.
select_file_btn_text = tk.StringVar()

#Creates "select file" button. It calls "Open_File" function when clicked.
select_file_btn = tk.Button(root, textvariable=select_file_btn_text, command=lambda:open_file(), font="ubunto", bg="#20be64", fg="white", height=1, width=14)
select_file_btn_text.set("Select File: ")
select_file_btn.grid(row=2, column=0, pady=30)

#Exit button to terminate the app at any time.
exit_button = tk.Button(root, text="Exit!", command=root.destroy, font="ubunto", bg="#be2020", fg="white", height=1, width=14)
exit_button.grid(row=4, column=0, pady=30)

root.mainloop()
