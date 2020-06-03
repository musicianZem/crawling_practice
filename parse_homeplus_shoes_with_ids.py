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
driver = webdriver.Chrome('./chromedriver83.exe') # download from google. same repository with this python file
driver.get('http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=61351')
list = []

# 마지막 페이지가 현 시점 jsPage('10', '4', 'martPage') 라서 2중 포문 저렇게 구성했습니다.
for i in range(4) :
    for j in range(10) :
        if(j == 9 and i >= 4) :
            break

        runScript = "jsPage('"+str(j+1)+"','"+str(i+1)+"', 'martPage');";
        print(runScript) # just for running check
        driver.execute_script(runScript); # 1 ~ 44 페이지 중 한 리스트를 load

        e = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fix-ty2")))

        shop_list = driver.find_elements_by_class_name('fix-ty2') # item-list 각 한 줄

        for elem in shop_list :
            shoes_link_list = elem.find_elements_by_css_selector('li')

            for slink in shoes_link_list :
                shoes_image = slink.find_elements_by_css_selector('img') # image onclick has itemGoodsId
                for img in shoes_image :
                    onclick_function = img.get_attribute('onclick')
                    if(onclick_function) : # 작은 아이콘조차 img태그로 감싸져있어서 onclick 있는것만 걸러냈습니다.
                        jsGoodDetail = onclick_function.split('\'')[1] # onclick="jsGoodsDetail('여기따올거임', ''); return false"
                        list.append(jsGoodDetail)

for e in list :
    print(e) # 임시로 출력만 해보고, 아직 파일로 저장하고 있진 않는 상태.
