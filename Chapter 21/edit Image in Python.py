# installation of pillow library 
# change the image extension 
# resize image files
# resize multiple images using for loop  
# Sharpness 
# Brightess 
# Color
# Contrast 
# Image blur , GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os 
os.getcwd()
os.chdir("H:\\Python\\Chapter 21")
os.makedirs("Updated photo")

# change the image extension 
image1 = Image.open('Dog1.jpg')
image1.save('Updated photo\\Dog1.jpeg')
image1.save("Updated photo\\Dog1.pdf")
image1.show()

# resize image files
max_size =(250,250)
image1.thumbnail(max_size)
image1.save('Updated photo\\dog1small_size.jpg')


for item in os.listdir():
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        filename,extension = os.path.splitext(item)
        img1.save(f'Updated photo\\{filename}.png')

# Sharpness 
from PIL import ImageEnhance
image1 = Image.open('Dog1.jpg')
enhancer = ImageEnhance.Sharpness(image1)
enhancer.enhance(5).save('Updated photo\\dog1edited_Sharpness.jpg')
# 0 : blurry 
# 1: original image 
# 2 : image with increased sharpness and more than 2 increase shapness with number 


# -------color ---------
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(2).save('Updated photo\\dog1edited_color.jpg')
# 0 : black and white 
# 1: original image 
# 2 : image with increased colours and more than 2 increase shapness with number 


# --------brightness -----------
img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).save('Updated photo\\dog1edited_Brightness.jpg')
# 0 : black 
# 1: original image 
# 2 : image with increased brightness and more than 2 increase shapness with number 


img1 = Image.open('dog1.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).save('Updated photo\\dog1edited_contrast.jpg')

# image blur 
from PIL import ImageFilter
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('Updated photo\\dog1edited_blur.jpg')


'''
import shutil
shutil.rmtree("H:/Python/Chapter 21/Updated photo")
'''