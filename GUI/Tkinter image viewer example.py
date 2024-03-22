#https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5250s

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('codemy.com Image Viewer')


img1 = ImageTk.PhotoImage(Image.open('C:/Users/ACER_USER/Downloads/Pic/1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('C:/Users/ACER_USER/Downloads/Pic/Aqua.jpg'))
img3 = ImageTk.PhotoImage(Image.open('C:/Users/ACER_USER/Downloads/Pic/Dunno.jpg'))
img4 = ImageTk.PhotoImage(Image.open('C:/Users/ACER_USER/Downloads/Pic/Gura Fanart.jpg'))
img5 = ImageTk.PhotoImage(Image.open('C:/Users/ACER_USER/Downloads/Pic/Profile Pic.jpg'))

imglist = [img1,img2,img3,img4,img5]

label=Label(image=img1)
label.grid(row=0,column=0,columnspan=3)


def forward(num):

    global label
    global backb
    global forwardb
    
    label.grid_forget()
    label=Label(image=imglist[num-1])

    forwardb=Button(root,text='>>',command=lambda:forward(num+1))
    backb=Button(root,text='<<',command=lambda:back(num-1))

    if num==5:
        
        forwardb=Button(root,text='>>',state=DISABLED)

    if num==0:
         
        backb=Button(root,text='<<',state=DISABLED)
        

    label.grid(row=0,column=0,columnspan=3)
    backb.grid(row=1,column=0)
    forwardb.grid(row=1,column=2)


    



def back(num):
    global label
    global backb
    global forwardb
    
    label.grid_forget()
    label=Label(image=imglist[num-1])

    forwardb=Button(root,text='>>',command=lambda:forward(num+1))
    backb=Button(root,text='<<',command=lambda:back(num-1))

    if num==5:
        forwardb=Button(root,text='>>',state=DISABLED)

    if num==0:
        backb=Button(root,text='<<',state=DISABLED)
        

    label.grid(row=0,column=0,columnspan=3)
    backb.grid(row=1,column=0)
    forwardb.grid(row=1,column=2)





backb=Button(root,text='<<',command=lambda:back(5))
forwardb=Button(root,text='>>',command=lambda:forward(2))
exitb=Button(root,text="Exit",command=root.quit)

backb.grid(row=1,column=0)
forwardb.grid(row=1,column=2)
exitb.grid(row=1,column=1)


root.mainloop()
