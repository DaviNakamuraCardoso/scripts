from selenium import webdriver
from selenium.webdriver.common.keys import Keys



options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/davi/.config/google-chrome/Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome('/home/davi/Downloads/chromedriver_linux64/chromedriver', options=options)
driver.get('https://gabrielecirulli.github.io/2048')
bt = driver.find_element_by_xpath('/html/body')
rt = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/a[2]')


def play(button, retry):
    """
    :return: Plays 2048
    """
    while not retry.is_displayed():
        button.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    retry.click()


while True:
    play(bt, rt)

