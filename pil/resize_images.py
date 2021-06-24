from PIL import Image


def quarter(filename):
    """

    :param filename: the filename
    :return: redefined image
    """
    image = Image.open(filename)
    width, height = image.size
    quarter_sized = image.resize((int(width/2), int(height/2)))
    quarter_sized.save('quarter_sized_%s.png' % filename.strip('.png'))
    svelte_image = image.resize((width, height+300))
    svelte_image.save('svelte_%s.png' % filename.strip('.png'))


#quarter('zophie.png')


def rotate(filename):
    """

    :param filename:
    :return:
    """
    image = Image.open(filename)
    image.rotate(90).save('rotated90.png')
    image.rotate(180).save('rotate180.png')
    image.rotate(270).save('rotate270.png')


#rotate('zophie.png')
image = Image.open('zophie.png')
image.rotate(6, expand=True).save('rotate_expanded.png')


def mirror_flip(filename):
    """

    :param filename:
    :return:
    """
    image = Image.open(filename)
    image.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
    image.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')


mirror_flip('zophie.png')

