import time
import pyperclip
import getpass
from selenium import webdriver # pip install selenium
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.webdriver.common.keys import Keys

input_id = 'qufaudwpak'
input_pw = 'dlwpdjs3#'
#input_id = input          ("E-mail   : ")
#input_pw = getpass.getpass("Password : ")

# chrome 드라이버
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=61351')
