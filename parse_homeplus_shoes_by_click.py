import time
import pyperclip
import getpass
from selenium import webdriver # pip install selenium
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.webdriver.common.keys import Keys

# chrome 드라이버
driver = webdriver.Chrome('./chromedriver83.exe')
driver.get('http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=61351')

shop_list = driver.find_elements_by_class_name('fix-ty2')

for elem in shop_list :
    shoes_link_list = elem.find_elements_by_css_selector('li')

    for slink in shoes_link_list :
        slink.find_element_by_css_selector('div').click()
