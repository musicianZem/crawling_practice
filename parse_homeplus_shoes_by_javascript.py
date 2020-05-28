import time
import pyperclip
import getpass
from selenium import webdriver # pip install selenium
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

input_id = 'qufaudwpak'
input_pw = 'dlwpdjs3#'
#input_id = input          ("E-mail   : ")
#input_pw = getpass.getpass("Password : ")

# chrome 드라이버
driver = webdriver.Chrome('./chromedriver83.exe')
driver.get('http://www.homeplus.co.kr/app.exhibition.category.Category.ghs?comm=category.list&cid=61351')

driver.execute_script("")
pager = driver.find_element_by_id('martPaging')
print(pager)

nextLinks = pager.find_elements_by_tag_name('a')
print(nextLinks)

cnt = 0
for nextPage in nextLinks :
    if(nextPage.get_attribute('class') == '') :
        print(cnt)

    cnt = cnt + 1


'''next_tabs = [ i.get_attribute('class') for i in nextLinks ]
for i in range(nextLinks.length) :
    print(i)'''
















'''
login_btn = driver.find_element_by_class_name('link_login')
login_btn.click()

tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('pw')
tag_id.clear()
tag_id.click()
pyperclip.copy(input_id)
tag_id.send_keys(Keys.CONTROL, 'v')

# pw 입력
tag_pw.click()
pyperclip.copy(input_pw)
tag_pw.send_keys(Keys.CONTROL, 'v')

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('log.login')
login_btn.click()
time.sleep(0.1)
## 2차 인증 있으면 여기서 멈춰야함 input()

base_url = 'https://cafe.naver.com/sequencediary?iframe_url=/ArticleList.nhn%3Fsearch.clubid=29802635%26search.boardtype=L%26search.totalCount=151%26search.page='

result_list = [];

for page in range(3) :
    driver.get(base_url + str(page+1))
    driver.switch_to.frame('cafe_main')
    quest_list = driver.find_elements_by_css_selector('div.inner_list > a.article')
    quest_urls = [ i.get_attribute('href') for i in quest_list ]

    for quest in quest_urls :
        try :
            OBJ_ONE = {};

            driver.get(quest)
            driver.switch_to.frame('cafe_main')
            soup = bs(driver.page_source, 'html.parser')

            #제목
            title = soup.select('div.tit-box span.b')[0].get_text()
            #print(title)

            #글쓴이
            person = soup.select('div.etc-box a.m-tcol-c')[0].get_text()
            #print(person)

            #내용
            contents_tags = soup.select('#tbody')[0]#.select('p')
            #print(contents_tags)
            #content = ' '.join([ tags.get_text() for tags in contents_tags ])
            content = str(contents_tags)
            while True :
                l = content.find('<')
                r = content.find('>')
                if l < 0 or r < 0 :
                    break
                if l >= r :
                    break
                content = content[0:l] + content[r+1:]
            #print(content)

            #댓글 작성자
            commenter = soup.select('div.comm_cont a.m-tcol-c')
            commentxt = soup.select('div.comm_body')
            for i in commenter :
                print(i.get_text())
            OBJ_ONE['title'] = title
            OBJ_ONE['person'] = person
            OBJ_ONE['content'] = content
            result_list.append(OBJ_ONE)


        except :
            print("ERROR", quest)
            continue

text_file = open("./diary.txt", "w", -1, 'utf-8')
text_file.write('[\n')
isFirst = 1
for oneFeed in result_list :
    if isFirst == 1 :
        isFirst = 0
        text_file.write('  {\n')
    else :
        text_file.write(',\n  {\n')

    for key in oneFeed :
        text_file.write('    \"'+key + '\":\"' + oneFeed[key]);
        if key == 'content' :
            text_file.write('\"\n')
        else :
            text_file.write('\",\n')

    text_file.write('  }')
text_file.write('\n]')
text_file.close()
'''
