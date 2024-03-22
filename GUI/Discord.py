#https://www.tutorialspoint.com/python/python_gui_programming.htm
#linking to Matlab: https://www.mathworks.com/matlabcentral/answers/525545-calling-python-function-from-matlab-when-using-python-tkinter-results-in-tclerror-can-t-find-a-usa


import tkinter as tk
import tkinter.font as tkfont
import cv2 as cv
import random
import PIL.Image as I         #https://pillow.readthedocs.io/en/stable/
import PIL.ImageTk as Itk    


root=tk.Tk()
root.title("Discord")
root.iconbitmap("C:/Users/ACER_USER/Desktop/Python/Script/Summer Research Intern 2021/GUI/Discord Icon.ico")
frame0=tk.LabelFrame(root,text="",width=100,bg="#36393F")
frame1=tk.LabelFrame(root,text="",bg="#36393F")
frame2=tk.LabelFrame(frame1,text="",bg="#36393F")
frame3=tk.LabelFrame(frame1,text="",bg="#36393F")

'''
def passwordsignin():

    def signinsucc():
        signin.grid_forget()
        username.grid_forget()
        password.grid_forget()
        unenter.grid_forget()
        pwenter.grid_forget()
        signinbutton.grid_forget()
        mtl1.grid_forget()
        mtl2.grid_forget()


        succ=tk.Label(root,text="Signed in successfully")
        succ.grid(padx=180,pady=85)
        
    
    label.grid_forget()
    pwmethod.grid_forget()
    qrmethod.grid_forget()

    signin=tk.Label(root,text="Enter your username and password")

    username=tk.Label(root,text="Username")
    password=tk.Label(root,text="Password")
    
    unenter=tk.Entry(root,width=30)
    pwenter=tk.Entry(root,width=30)

    
    signinbutton=tk.Button(root,text="Sign in",command=signinsucc,width=20)

    
    #indentation purpose, "mt"="emtpy" mtl=>empty label
    mtl1=tk.Label(root,text="")
    mtl2=tk.Label(root,text="")

    signin.grid(row=0,column=0,padx=10,pady=20)
    
    username.grid(row=1,column=0,pady=10)
    password.grid(row=2,column=0,pady=10)
    unenter.grid(row=1,column=1,padx=20,sticky="w")
    pwenter.grid(row=2,column=1,padx=20,sticky="w")

    signinbutton.grid(row=3,column=1)

    mtl1.grid(row=4,column=0)
    mtl2.grid(row=1,column=4,padx=20)





def qrsignin():

    def displayqr():
        
        names=["...","abc","asd","daga kotowaru","good afternoon",
               "good morning","good night","hello world","I love you",
               "login","musedash","nani","nice","nicenicenice","no",
               "omaewa mou shindeiru","wait a minute","wasd","yes","za warudo"]
        name=names[random.randint(0,len(names)-1)]
        jpg=name+".jpg"
        filename="C:/Users/ACER_USER/Desktop/Matlab/Summer Research Intern 2021/QR code/Python generated hash/"+jpg
        img=cv.imread(filename)
        cv.imshow(jpg,img)
        cv.waitKey(1)
        
        


    def scanqr():
        #https://learnopencv.com/opencv-qr-code-scanner-c-and-python/
        
        vid=cv.VideoCapture(0)
        for i in range(500):
            frame=vid.read()[1]
            cv.imshow("Show the QR code",frame)
            cv.waitKey(1)
        vid.release()
        cv.destroyAllWindows()
        


    
    label.grid_forget()
    pwmethod.grid_forget()
    qrmethod.grid_forget()

    qroption=tk.Label(root,text="Please choose an option")

    scanwphone=tk.Button(root,text="Scan with phone",command=displayqr)
    scanwcom=tk.Button(root,text="Scan with computer",command=scanqr)

    qroption.grid(row=0,column=0,padx=10,pady=20)
    scanwphone.grid(row=1,column=0,padx=30,pady=30)
    scanwcom.grid(row=1,column=2,padx=30,pady=30)
'''


size=800,800
img=I.open("C:/Users/ACER_USER/Desktop/Python/Script/Summer Research Intern 2021/GUI/Discord Logo 2.jpg")
img.thumbnail(size)

Dimg=Itk.PhotoImage(img)

                                  


Discord = tk.Label(frame0,image=Dimg,anchor="center")

#frame2
welcome=tk.Label(frame2,text="Welcome back!",font='Uni 20 bold',fg="white",bg="#36393F")    
were=tk.Label(frame2,text="We're so excited to see you again!",font='Uni 10',fg="#B9BBBE",bg="#36393F")
emailphone=tk.Label(frame2,text="EMAIL OR PHONE NUMBER",font='Uni 10 bold',fg="#B9BBBE",bg="#36393F")
emailentry=tk.Entry(frame2,width=60,fg="#B9BBBE",bg='#303338')
password=tk.Label(frame2,text="PASSWORD",font='Uni 10 bold',fg="#B9BBBE",bg="#36393F")
passwordentry=tk.Entry(frame2,width=60,fg="#B9BBBE",bg='#303338')
forgot=tk.Label(frame2,text="Forgot your password?",font='Uni 9 bold',fg='#12ABF4',bg="#36393F")              #should be a button
loginB=tk.Button(frame2,text="Login",width=50,height=2,fg='white',bg='#5865F2',font='Uni 9 bold')
needanacc=tk.Label(frame2,text="Need an account?",font='Uni 9',fg="#B9BBBE",bg="#36393F")
register=tk.Label(frame2,text="Register",font='Uni 9 bold',fg='#12ABF4',bg="#36393F")                        #should be a button



#frame3
names=["...","abc","asd","daga kotowaru","good afternoon",
               "good morning","good night","hello world","I love you",
               "login","musedash","nani","nice","nicenicenice","no",
               "omaewa mou shindeiru","wait a minute","wasd","yes","za warudo"]
name=names[random.randint(0,len(names)-1)]
jpg=name+".jpg"
filename="C:/Users/ACER_USER/Desktop/Matlab/Summer Research Intern 2021/QR code/Python generated hash/"+jpg
QRsize=150,150
QR=I.open(filename)
QR.thumbnail(QRsize)
QR=Itk.PhotoImage(QR)

QRcode=tk.Label(frame3,image=QR)


LoginwithQR=tk.Label(frame3,text="Log in with QR Code",font='Uni 20 bold',fg="white",bg="#36393F")
Scanthis=tk.Label(frame3,text="Scan this with the discord mobile app to log in instantly.",font='Uni 12 bold',fg="#B9BBBE",bg="#36393F")



'''
label = tk.Label(root,text="Please choose your sign in method")
pwmethod = tk.Button(root,text="Sign in with password", command=passwordsignin)
qrmethod = tk.Button(root,text="Sign in with QR code",command=qrsignin)
pwmethod.grid(row=1,column=0,padx=50,pady=30)
qrmethod.grid(row=1,column=1,padx=50,pady=30)
'''


#https://www.tutorialspoint.com/python/tk_grid.htm



frame0.grid(row=0,column=0,sticky="we")
frame1.grid(row=1,column=0)
frame2.grid(row=0,column=0,padx=0)
frame3.grid(row=0,column=1,padx=0,sticky="ns")
Discord.grid(row=0,column=0,padx=50,sticky="we")

#frame2
welcome.grid(row=0,column=0,padx=10,sticky="w")
were.grid(row=1,column=0,padx=10,sticky="w")
emailphone.grid(row=2,column=0,padx=10,pady=10,sticky="w")
emailentry.grid(row=3,column=0,padx=10,sticky="w")
password.grid(row=4,column=0,padx=10,pady=10,sticky="w")
passwordentry.grid(row=5,column=0,padx=10,sticky="w")
forgot.grid(row=6,column=0,padx=10,pady=3,sticky="w")
loginB.grid(row=7,column=0,padx=10,pady=5,sticky="w")
#needanacc.grid(row=8,column=0,sticky="w")
#register.grid(row=8,column=1,padx=0,sticky="w")


#frame3
QRcode.grid(row=0,column=0,padx=20)
LoginwithQR.grid(row=2,column=0)
Scanthis.grid(row=3,column=0)





root.mainloop()
