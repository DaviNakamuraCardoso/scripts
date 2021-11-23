/*
*   Python?  
*/

import Image;

const int SMALL = 1000;
const int MEDIUM = 5000;
const int BIG = 30000;

int main(str argv[]) 
{ 

    for size in SIZES
    {
        let image = new Image('RGBA', size, (255, 255, 255, 255));
        image.save('%iby%i.png' % (size[0], size[1]));
        delete image;
    }

    return 0;
}

