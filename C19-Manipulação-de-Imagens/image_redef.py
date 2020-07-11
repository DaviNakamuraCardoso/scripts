from PIL import Image
import os
import send2trash


def size(directory):
    """

    :param directory: The directory
    :return:
    """
    os.chdir(directory)
    logo_image = Image.open('catlogo.png')
    logo = logo_image.resize((40, 35))
    for filename in os.listdir():
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(filename)
            width, height = image.size
            dimensions = [int(width), int(height)]
            if int(width) > 300 or int(height) > 300:
                dimensions.sort(reverse=True)
                greater = int(dimensions[0])
                lower = int(dimensions[1])
                new_low = int(lower * 300 / greater)
                if greater == 'width':
                    new_img = image.resize((300, new_low))
                    new_img.paste(logo, (260, new_low-35), logo) # We pass the third argument to ensure the image's
                    # pixels will be transparent
                else:
                    new_img = image.resize((new_low, 300))
                    new_img.paste(logo, (new_low-40, 260), logo)
            else:
                new_img = image.copy()
                new_img.paste(logo, (width-40, height-35), logo)
            if filename.endswith('.png'):
                new_img.save('resized_%s.png' % filename.strip('.png'))
            else:
                new_img.save('resized_%s.jpg' % filename.strip('.jpg'))


def delete_resized(directory):
    """

    :param directory:
    :return:
    """
    for filename in os.listdir():
        if filename.startswith('resized') and filename.endswith('.png'):
            send2trash.send2trash(os.path.join(directory, filename))


delete_resized('./')
size('./')
