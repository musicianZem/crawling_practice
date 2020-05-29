import time
import pyperclip
import getpass
from selenium import webdriver # pip install selenium
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# chrome 드라이버
driver = webdriver.Chrome('./chromedriver83.exe')
driver.get('http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=61351')

for i in range(11) :
    for j in range(10) :
        if(i == 8 and j == 3) :
            break

        #driver.execute_script("jsPage()") # wait.....
        shop_list = driver.find_elements_by_class_name('fix-ty2')

        for elem in shop_list :
            shoes_link_list = elem.find_elements_by_css_selector('li')

            for slink in shoes_link_list :
                shoes_image = slink.find_element_by_css_selector('img')
                onclick_function = shoes_image.get_attribute('onclick')
                if(onclick_function) :
                    print(onclick_function) ## result = goodsid
                #slink.find_element_by_css_selector('div').click()
                #e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p-info")))
                #driver.execute_script("window.history.go(-1)")
