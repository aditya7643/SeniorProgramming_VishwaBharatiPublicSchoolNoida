#Importing nesecarry libraries
import cv2
import urllib.request
import numpy as np

#Link of avatar
#this is just sample link, you can change this to generate new images
avatar = "https://user-images.githubusercontent.com/99065656/199068721-d5d4faf1-6263-4206-b1cf-6c57381e0d9c.png"

# Meme generation functions
def wanted(avatar):   
    img=cv2.imread('want.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)
    img2=cv2.resize(img2, (400,451))
    for i in range (139,590):
        for j in range(50,450):
            img[i][j]=img2[i-139][j-50]
            
    status = cv2.imwrite('result1.png',img)     

def stage(avatar):
    img=cv2.imread('stage.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (490,280))
    for i in range (54,330):
        for j in range(89,579):
            if 190<img[i,j][0]<230 or 90<img[i,j][0]<150:
                img[i][j]=img2[i-54][j-89]
                
    status = cv2.imwrite('result2.png',img)       


def foot(avatar):
    img=cv2.imread('foot.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (340,350))
    for i in range (690,1020):
        for j in range(190,530):
            if img[i,j][0]==204:
                img[i][j]=img2[i-690][j-190]
                
    status = cv2.imwrite('result3.png',img)       


def worthless(avatar):
    
    img=cv2.imread('worthless.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (1111,601))
    for i in range (160,760):
        for j in range(160,1260):
            if 230<img[i,j][0]<=255:
                img[i][j]=img2[i-160][j-160]
                
    status = cv2.imwrite('result4.png',img)       


def supreme(avatar):
    img=cv2.imread('supreme.jpg',1)
    img=cv2.resize(img,(500,500))
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (100,100))
    for i in range (200,300):
        for j in range(50,150): 
            if img[i,j][0]>80:
                img[i][j]=img2[i-200][j-50]
                
    status = cv2.imwrite('result5.png',img)       


def miss(avatar):
    img=cv2.imread('miss.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (230,200))
    for i in range (170,370):
        for j in range(140,370): 
            
            img[i][j]=img2[i-170][j-140]
                    
    status = cv2.imwrite('result6.png',img)       


def cheat(avatar):
    img=cv2.imread('hh.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (260,195))
    for i in range (420,610):
        for j in range(350,615):
            if img[i][j][0]>240:
                img[i][j]=img2[i-420][j-350]
                    
    status = cv2.imwrite('result7.png',img)       


def scare(avatar):
    img=cv2.imread('scare.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (164,164))
    for i in range (331,493):
        for j in range(166,330): 
            
            img[i][j]=img2[i-331][j-166]
                    
    status = cv2.imwrite('result8.png',img)       


def button(avatar):
    img=cv2.imread('button.jpg',1)
    req = urllib.request.urlopen(avatar)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img2 = cv2.imdecode(arr, 1)

    img2=cv2.resize(img2, (265,250))
    for i in range (150,400):
        for j in range(35,300):
            if (i-300)**2+(j-166)**2<12000:
            
                img[i][j]=img2[i-150][j-35]
                    
    status = cv2.imwrite('result9.png',img)       


# Calls all the functions
wanted(avatar)
stage(avatar)
foot(avatar)
worthless(avatar)
supreme(avatar)
miss(avatar)
cheat(avatar)
scare(avatar)
button(avatar)