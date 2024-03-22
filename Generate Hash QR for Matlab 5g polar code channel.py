import cv2 as cv
import qrcode
import os
import hashlib as h


text=input("Please enter the content : \n")


encoded=text.encode()

hashobject=h.sha256(encoded)

hashvalue=hashobject.hexdigest()


print(hashvalue)
print("len : ",len(hashvalue),'\n')


qr = qrcode.QRCode(version=3,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=2)


qr.add_data(hashvalue)
qr.make(fit=True)

im=qr.make_image(fill_color='black',back_color='white')


#cv.imshow('test',im)

os.chdir('C:/Users/ACER_USER/Desktop/Matlab/Summer Research Intern 2021/QR code/Python generated hash')


filename=text+'.jpg'

im.save(filename)
read=cv.imread(filename)
cv.imshow('test',read)


pixel = read.shape[0]   # get the pixel size of the image. Since QR code generated is a square image, length=width

nsquare = int(pixel/qr.box_size)

dimen = int(nsquare-(qr.border*2))

version = int(((dimen - 21)/4) + 1)

print("\nQR code version : ",version)
print("\nDimension : ",dimen)
print("\nPixel size : ",pixel)


