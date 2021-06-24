from PIL import Image

image_file = Image.open('zophie.png')
cropped_image = image_file.crop((335, 345, 565, 560)) # Pass the lef top and the right bottom point you want to crop
cropped_image.save('cropped.png')