#https://www.code-learner.com/generate-graphic-verification-code-using-python-captcha-module/

import captcha.image as capt
import cv2
import os
import string as s
import random as r




obj=capt.ImageCaptcha(width=280,height=90)



alphanume=s.ascii_letters+s.digits
text=""

for i in range(6):
    index=r.randint(0,61)
    text=text+alphanume[index]
    

    
image=obj.generate_image(text)

#print(text)

os.chdir('C:/Users/ACER_USER/Desktop')


image.save('test.jpg')
read=cv2.imread('test.jpg')

cv2.imshow("test",read)
cv2.waitKey(1)


inp=input("Please enter the alphanumeric text : \n")

while inp!=text:
    print("Wrong")
    inp=input("Please enter again\n")


print("Correct")


    


