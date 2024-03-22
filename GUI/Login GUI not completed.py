#linking to Matlab: https://www.mathworks.com/matlabcentral/answers/525545-calling-python-function-from-matlab-when-using-python-tkinter-results-in-tclerror-can-t-find-a-usa

import tkinter as tk
import cv2 as cv
import random


root=tk.Tk()
root.title("Sign in to your account")


def passwordsignin():


    def backtomethod():

        
        f2.grid_forget()
        f3.grid_forget()
        signin.grid_forget()
        un.grid_forget()
        pw.grid_forget()
        unenter.grid_forget()
        pwenter.grid_forget()
        signinbutton.grid_forget()
        back.grid_forget()

        notexist.grid_forget()
        incorrect.grid_forget()
        plsenterun.grid_forget()
        plsenterpw.grid_forget()

    

        label.grid(row=0,column=0,padx=10,pady=20)
        pwmethod.grid(row=1,column=0,padx=50,pady=30)
        qrmethod.grid(row=1,column=1,padx=50,pady=30)

        

    def check():


        def success():


            def logout():
                empty5.grid_forget()
                empty6.grid_forget()
                succ.grid_forget()
                empty.grid_forget()
                name.grid_forget()
                idd.grid_forget()
                empty2.grid_forget()
                balance.grid_forget()
                rm.grid_forget()
                empty3.grid_forget()
                logoutb.grid_forget()
                empty4.grid_forget()

                label.grid(row=0,column=0,padx=10,pady=20)
                pwmethod.grid(row=1,column=0,padx=50,pady=30)
                qrmethod.grid(row=1,column=1,padx=50,pady=30)



            f2.grid_forget()
            f3.grid_forget()
            signin.grid_forget()
            un.grid_forget()
            pw.grid_forget()
            unenter.grid_forget()
            pwenter.grid_forget()
            signinbutton.grid_forget()
            back.grid_forget()

            notexist.grid_forget()
            incorrect.grid_forget()
            plsenterun.grid_forget()
            plsenterpw.grid_forget()


            succ=tk.Label(root,text='Login successful')
            name=tk.Label(root,text='Lee Yu Chen',font='bold 12')
            idd=tk.Label(root,text='20204082')
            balance=tk.Label(root,text='Balance',font='bold 16')
            rm=tk.Label(root,text='RM 89.30')
    
            logoutb=tk.Button(root,text='Logout',width=8,command=logout)


            empty=tk.Label(root,text='')
            empty2=tk.Label(root,text='')
            empty3=tk.Label(root,text='')
            empty4=tk.Label(root,text='')
            empty5=tk.Label(root,text='        ')
            empty6=tk.Label(root,text='        ')

        

            empty5.grid(row=0,column=0,padx=30)
            empty6.grid(row=0,column=2,padx=30)

            succ.grid(row=0,column=1)
            empty.grid(row=1,column=1)
        
            name.grid(row=2,column=1)
            idd.grid(row=3,column=1)
            empty2.grid(row=4,column=1)
        
            balance.grid(row=5,column=1)
            rm.grid(row=6,column=1)
            empty3.grid(row=7,column=1)
        
            logoutb.grid(row=8,column=1)
            empty4.grid(row=9,column=1)
            




        
        username=unenter.get()
        password=pwenter.get()


        database=open("C:/Users/ACER_USER/Desktop/Python/Script/Summer Research Intern 2021/GUI/database.txt","r")

        data=database.read()
        database.close()
        datalist=data.split('\n')
        datalist=datalist[:len(datalist)-1]

        
        userlist=[]
        passlist=[]
        for i in datalist:
            user,pas=i.split(' ')
            
            userlist = userlist + [user]
            passlist = passlist + [pas]



        notexist.grid_forget()
        incorrect.grid_forget()
        plsenterun.grid_forget()
        plsenterpw.grid_forget()
        
        if username=='' and password=='':
            user=user       

        elif username=='' and password!='':
            plsenterun.grid(row=2,column=1,padx=20,sticky='w')

        elif username!='':
            
            if '@)!('+username not in userlist:
                notexist.grid(row=2,column=1,padx=20,sticky='w')

            else:
                ind=userlist.index('@)!('+username)

                if password=='':
                    plsenterpw.grid(row=4,column=1,padx=20,sticky='w')

                else:
                    
                    if '#]?['+password == passlist[ind]:
                        success()

                    else:
                        incorrect.grid(row=4,column=1,padx=20,sticky='w')
             
            
            
        '''
        notexist.grid(row=2,column=1,padx=20,sticky='w')
        plsenterun.grid(row=2,column=1,padx=20,sticky='w')

        incorrect.grid(row=4,column=1,padx=20,sticky='w')
        plsenterpw.grid(row=4,column=1,padx=20,sticky='w')
        '''


        
    
        
        
            
            
        
        
        
        
    
    label.grid_forget()
    pwmethod.grid_forget()
    qrmethod.grid_forget()
    
    



    f2=tk.Frame(root,borderwidth=0,highlightthickness=0)
    f3=tk.Frame(root,borderwidth=0,highlightthickness=0)
    
    signin=tk.Label(f2,text="Enter your username and password")

    un=tk.Label(f2,text="Username")
    pw=tk.Label(f2,text="Password")
    
    unenter=tk.Entry(f2,width=30)
    pwenter=tk.Entry(f2,width=30)

    notexist=tk.Label(f2,text="Username does not exist",fg='red')
    incorrect=tk.Label(f2,text='Incorrect password',fg='red')
    plsenterun=tk.Label(f2,text='Please enter your username',fg='red')
    plsenterpw=tk.Label(f2,text='Please enter your password',fg='red')

    
    signinbutton=tk.Button(f3,text="Sign in",command=check,width=20)
    back=tk.Button(f3,text='Back',command=backtomethod,width=8)



    f2.grid(row=0,column=0)
    f3.grid(row=1,column=0)

    signin.grid(row=0,column=0,padx=10,pady=20)
    
    un.grid(row=1,column=0,pady=10)
    pw.grid(row=3,column=0,pady=10)
    unenter.grid(row=1,column=1,padx=20,sticky="w")
    pwenter.grid(row=3,column=1,padx=20,sticky="w")

    

    
    

    

    signinbutton.grid(row=0,column=0,padx=30,pady=15)
    back.grid(row=0,column=1,padx=30,pady=15)

    








def qrsignin():

    

    def opencam():

        def success():


            def logout():
                empty5.grid_forget()
                empty6.grid_forget()
                succ.grid_forget()
                empty.grid_forget()
                name.grid_forget()
                idd.grid_forget()
                empty2.grid_forget()
                balance.grid_forget()
                rm.grid_forget()
                empty3.grid_forget()
                logoutb.grid_forget()
                empty4.grid_forget()

                label.grid(row=0,column=0,padx=10,pady=20)
                pwmethod.grid(row=1,column=0,padx=50,pady=30)
                qrmethod.grid(row=1,column=1,padx=50,pady=30)




            prepare.grid_forget()
            opencame.grid_forget()
            back.grid_forget()
            empty0.grid_forget()
            empty1.grid_forget()
            f1.grid_forget()
            qrnotfound.grid_forget()


            succ=tk.Label(root,text='Login successful')
            name=tk.Label(root,text='Lee Yu Chen',font='bold 12')
            idd=tk.Label(root,text='20204082')
            balance=tk.Label(root,text='Balance',font='bold 16')
            rm=tk.Label(root,text='RM 89.30')
    
            logoutb=tk.Button(root,text='Logout',width=8,command=logout)


            empty=tk.Label(root,text='')
            empty2=tk.Label(root,text='')
            empty3=tk.Label(root,text='')
            empty4=tk.Label(root,text='')
            empty5=tk.Label(root,text='        ')
            empty6=tk.Label(root,text='        ')

        

            empty5.grid(row=0,column=0,padx=30)
            empty6.grid(row=0,column=2,padx=30)

            succ.grid(row=0,column=1)
            empty.grid(row=1,column=1)
        
            name.grid(row=2,column=1)
            idd.grid(row=3,column=1)
            empty2.grid(row=4,column=1)
        
            balance.grid(row=5,column=1)
            rm.grid(row=6,column=1)
            empty3.grid(row=7,column=1)
        
            logoutb.grid(row=8,column=1)
            empty4.grid(row=9,column=1)
            




        #https://learnopencv.com/opencv-qr-code-scanner-c-and-python/

        qr=cv.QRCodeDetector()
        
        vid=cv.VideoCapture(0)
        msg=''
        i=0
        while len(msg)==0 and i<=500:

            frame=vid.read()[1]

            msg,box,rectI=qr.detectAndDecode(frame)

            if len(msg)==0 :
                #print('QR Code not found')
                msg=msg

            else:
                print(msg)
                start=(int(box[0][0][0])-10,int(box[0][0][1])-10)
                end=(int(box[0][2][0])+10,int(box[0][2][1])+10)
            
                cv.rectangle(frame,start,end,(255,0,0),5)

            
            cv.imshow("Show the QR code",frame)
            cv.waitKey(1)

            i=i+1

            
        vid.release()
        cv.destroyAllWindows()

        if len(msg)==0:
            prepare.grid_forget()
            qrnotfound.grid(row=0,column=1,padx=10,pady=20)
        else:
            success()

            
            


        




        
        

    def backtomethod():

        prepare.grid_forget()
        opencame.grid_forget()
        back.grid_forget()
        empty0.grid_forget()
        empty1.grid_forget()
        f1.grid_forget()
        qrnotfound.grid_forget()

        label.grid(row=0,column=0,padx=10,pady=20)
        pwmethod.grid(row=1,column=0,padx=50,pady=30)
        qrmethod.grid(row=1,column=1,padx=50,pady=30)
        
    
    
    label.grid_forget()
    pwmethod.grid_forget()
    qrmethod.grid_forget()

    

    prepare=tk.Label(root,text="Prepare your QR code")
    qrnotfound=tk.Label(root,text="QR Code not found, please scan again")


    f1=tk.Frame(root,borderwidth=0,highlightthickness=0)

    opencame=tk.Button(f1,text="Open camera",command=opencam)
    back=tk.Button(f1,text='Back',command=backtomethod,width=8)

    
    empty0=tk.Label(root,text='            ')
    empty1=tk.Label(root,text='            ')

    
    
    prepare.grid(row=0,column=1,padx=10,pady=20)

    f1.grid(row=1,column=1)
    
    opencame.grid(row=0,column=0,padx=30,pady=30)
    back.grid(row=0,column=1,padx=30,pady=30)
    
    empty0.grid(row=0,column=0)
    empty1.grid(row=0,column=2)








label = tk.Label(root,text="Please choose your sign in method")
pwmethod = tk.Button(root,text="Sign in with password", command=passwordsignin)
qrmethod = tk.Button(root,text="Sign in with QR code",command=qrsignin)

label.grid(row=0,column=0,padx=10,pady=20)
pwmethod.grid(row=1,column=0,padx=50,pady=30)
qrmethod.grid(row=1,column=1,padx=50,pady=30)







root.mainloop()
