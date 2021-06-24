from sys import argv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import DictWriter


info = {}
output = open("info2.csv", "w")
writer = DictWriter(output, ["name", "email", "phone", "role", "company"])
writer.writeheader()

def main(argc, argv):

    driver = open_browser(None)
    driver.get("https://rmvaleti.wellbiz.app/#/networking")

    sleep(3)

    for i in range(9, 115):
        get_people(driver, i)

    driver.quit()

    return 0

def get_people(driver, page):

    get_page(driver, page)
    elements = driver.find_elements_by_class_name("person-name")
    roles = driver.find_elements_by_class_name("person-role")
    companies = driver.find_elements_by_class_name("person-company")
    for i in range(len(elements)):
        try:
            get_person(driver, elements[i], roles[i].text, companies[i].text)
        except IndexError:
            return
        get_page(driver, page)
        sleep(4)
        elements = driver.find_elements_by_class_name("person-name")
        roles = driver.find_elements_by_class_name("person-role")
        companies = driver.find_elements_by_class_name("person-company")

    return


def get_page(driver, page):

    driver.get("https://rmvaleti.wellbiz.app/#/networking")

    sleep(3)
    for i in range(1, page):
       sleep(3)
       next = driver.find_element_by_id("click-next-page")
       next.click()

    page = driver.find_element_by_id(f"click-page-{page}")
    page.click()
    sleep(4)

    return

def get_person(driver, element, role, company):
    global info, writer

    name =  (element.text).title()


    print("Getting %s..." % name)

    element.click()
    sleep(4)
    spans = driver.find_elements_by_tag_name("span")

    info[name] = {"name": name, "email": spans[2].text, "phone": spans[1].text, "role": role, "company": company}

    writer.writerow(info[name])

    print("\n")
    talk(driver, name)

    sleep(4)
    return


def talk(driver, name):
    btn = driver.find_element_by_class_name("btn-send-message")
    btn.click()
    sleep(3)

    input = driver.find_element_by_tag_name("input")
    input.send_keys(f"Olá, {name}! ")
    input.send_keys("Meu nome é Davi estou procurando um emprego na área da programação. Tenho experiência com as linguagens C, Python e JavaScript, com frameworks Django e React, e tecnologias Git e AWS. Email: davinakamuracardoso@gmail.com")
    button = driver.find_element_by_class_name("btn-send-message")
    button.click()
    sleep(2)
    driver.back()
    return


def open_browser(void):
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=/home/davi/.config/google-chrome/Default")
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    return driver


if __name__ == '__main__':

    main(len(argv), argv)
