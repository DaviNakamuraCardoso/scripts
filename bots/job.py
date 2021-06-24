from sys import argv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main(argc, argv):

    driver = open_browser(None)
    driver.get("https://rmvaleti.wellbiz.app/#/networking")

    sleep(3)
    elements = driver.find_elements_by_class_name("person-name")
    for i in range(len(elements)):
        get_person(e)
        driver.back()



    input()

    driver.quit()

    return 0

def get_person(element):
    print("Getting %s...\n" % element.text)
    element.click()

    return


def open_browser(void):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/home/davi/.config/google-chrome/Default")
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    return driver


if __name__ == '__main__':

    main(len(argv), argv)
