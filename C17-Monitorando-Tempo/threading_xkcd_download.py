import bs4
import requests
import threading
import os

os.makedirs('xkcd', exist_ok=True)


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Downloading the page
        print('Downloading the page')
        res = requests.get('http://xkcd.com%s' % url_number)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='html.parser')

        # Find the url of the comic image

        comic_element = soup.select('#comic img')
        if comic_element == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_element[0].get('src')
        # Download the image
        print('Downloading the %s' % comic_url)

        res = requests.get('https:' + comic_url)
        # Save the image to xkcd file
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()


# Create and start the thread objects
download_threads = []
for i in range(0, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so we set it to 1
        download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()
for download_thread in download_threads:
    download_thread.join()

print('Done.')
