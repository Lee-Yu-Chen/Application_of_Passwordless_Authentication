import cv2 as cv
import qrcode
import os 


string=input("Please enter the QR code content : \n")

qr = qrcode.QRCode(version=3,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=15,border=2)

'''
QR code versions
https://www.qrcode.com/en/about/version.html

error correction capability %
https://www.qrcode.com/en/about/error_correction.html


version = ((dimension - 21) / 4 ) + 1

maximum size of QR code :
for version 40 (dimension 177)
box size = 4

version 1 (dimension 21)
box size = 30~34 

:.
box size = 4-32


acceptable image size (unit = pixels)
(dimension + 2*border) * box_size < 820


maximum density (minimum box size) : 2
'''


qr.add_data(string)
qr.make(fit=True)

im=qr.make_image(fill_color='blue',back_color='white')


#cv.imshow('test',im) dunno why doesnt work, probably due to data type

os.chdir('C:/Users/ACER_USER/Desktop')
im.save('test.jpg')
read=cv.imread('test.jpg')
cv.imshow('test',read)


# calculate the version of the generated QR code,
# since the function will generate a QR code with bigger version if the length of the string is too long for the specified version

pixel = read.shape[0]   # get the pixel size of the image. Since QR code generated is a square image, length=width

nsquare = int(pixel/qr.box_size)

dimen = int(nsquare-(qr.border*2))

version = int(((dimen - 21)/4) + 1)

print("\nQR code version : ",version)
print("Dimension       : ",dimen)
print("Pixel size      : ",pixel)



