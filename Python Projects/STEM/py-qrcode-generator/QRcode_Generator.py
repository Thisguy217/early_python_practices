import qrcode
from tkinter import *

#Create Window
root=Tk()
root.title("QR Code Generator")
root.geometry("400x125")

#Function for generation of QR Code
def generator(data):
    if data=="":
        ting.config(text="No Input, please enter valid input.")
    else:
        #Verify acceptance
        ting.config(text="Data Accepted")
        #Generate QR Code
        img=qrcode.make(data)
        ting.config(text=type(img))
        ting.config(text="QR Code Generated")
        #Saves QR Code
        img.save("qrcode.jpg")
        ting.config(text="QR Code Saved")

#Window UI
link_label=Label(root,text="Enter Data:")
link_label.grid(row=0,column=0,pady=15,padx=10)
link_input=Entry(root,width=50)
link_input.grid(row=0,column=1,pady=15)
button_generator=Button(root,text="Generate",command=lambda:generator(link_input.get()))
button_generator.grid(column=0, columnspan=2, row=1)
ting=Label(root, text="")
ting.grid(column=0,columnspan=2, row=2,pady=15)

root.mainloop()