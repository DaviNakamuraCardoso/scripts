from PIL import Image

cat_image = Image.open('zophie.png') # To open a image, use the Image.open function

print(cat_image.size)
width, height = cat_image.size
print(width)
print(height)
print(cat_image.filename)
print(cat_image.format)
print(cat_image.format_description)
cat_image.save('zophie.png')
image = Image.new('RGBA', (100, 200), 'purple') # The Image.new() function creates a new image. First we set the RGBA,
# then the (width, height) tuple
image.save('purple_image.png')
image2 = Image.new('RGBA', (20, 20))
image2.save('transparent_image.png')

