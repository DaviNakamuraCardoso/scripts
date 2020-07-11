from PIL import Image

# The Image.copy() method will return the same image that was copied.
cat_image = Image.open('zophie.png')
copy_cat = cat_image.copy()
face_image = cat_image.crop((335, 345, 565, 560))
print(face_image.size)
copy_cat.paste(face_image, (0, 0))
copy_cat.paste(face_image, (400, 500))
copy_cat.save('pasted.png')


def make_faces(filename):
    """

    :param image: image filename
    :return: a new image with lots of faces
    """
    image = Image.open(filename)
    width, height = image.size
    crop = image.crop((335, 345, 565, 560))
    crop_w, crop_h = crop.size
    copy = image.copy()
    for left in range(0, width, crop_w):
        for top in range(0, height, crop_h):
            print(left, top)
            copy.paste(crop, (left, top))
    name = filename.strip('.png')
    copy.save('%s_faces.png' % name)


make_faces('zophie.png')