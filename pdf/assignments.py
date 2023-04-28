from sys import argv 
from PyPDF2 import PdfReader, PdfWriter


def main(): 
    filename = argv[1]
    r1, r2, r3, r4 = PdfReader(filename), PdfReader(filename), PdfReader(filename), PdfReader(filename)
    writer = PdfWriter()

    for p1, p2, p3, p4 in zip(r1.pages, r2.pages, r3.pages, r4.pages): 
        p1, p2, p3, p4 = get_first(p1), get_second(p2), get_third(p3), get_forth(p4)

        writer.add_page(p1)
        writer.add_page(p2)
        writer.add_page(p3)
        writer.add_page(p4)
    

    with open(f'{filename}-cropped.pdf', 'wb') as fp: 
        writer.write(fp)
        
    return 0


def get_first(page): 
    page.mediabox.upper_right = (
        295, 
        785
    )
    page.mediabox.lower_left = (
        0, 
        400
    )

    return page


def get_second(page): 
    page.mediabox.upper_right = (
        600, 
        785
    )
    page.mediabox.lower_left = (
        300, 
        400
    )

    return page 


def get_third(page): 
    page.mediabox.upper_right = (
        295, 
        380
    )
    page.mediabox.lower_left = (
        0, 
        0
    )

    return page

def get_forth(page): 
    print(page.mediabox.width)
    print(page.mediabox.height)
    page.mediabox.upper_right = (
        600, 
        371
    )
    page.mediabox.lower_left = (
        300, 
        0
    )

    return page


if __name__ == '__main__': 
    main()
