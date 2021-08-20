import os
import time
import account_info

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 변수
url_home = 'https://www.naver.com/'
url_vaccine = 'https://m.place.naver.com/rest/vaccine?vaccineFilter=used&x=127.0258739&y=37.5751279&bounds=126.9874217%3B37.5600927%3B127.064326%3B37.59016'
driver = webdriver.Chrome('./chromedriver')
vaccine = False

# 로그인
driver.get(url_home)
driver.find_element_by_class_name('link_login').click()

input_id = driver.find_element_by_id('id')
input_id.send_keys(account_info.NAVER_ID)
input_pw = driver.find_element_by_id('pw')
input_pw.send_keys(account_info.NAVER_PW)
input_pw.send_keys(Keys.RETURN)

os.system('say "추가 인증 및 보안문자 입력시간이 지금부터 15초 주어집니다."')
time.sleep(15)

# 페이지 로딩 및 목록보기 클릭
driver.get(url_vaccine)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._31ySW')))
driver.find_element_by_class_name('_31ySW').click()

# 현재 페이지 BS4 모듈에 저장
soup = BeautifulSoup(driver.page_source)

while vaccine is False:
    no = 0
    hospitals = soup.select('li._1mrr7')

    for hospital in hospitals:
        hospital_status = hospital.select_one('a._46SXN > strong').get_text()
        if (hospital_status != '대기중') and (hospital_status != '마감') and (hospital_status != '0'):
            vaccine = True
            break
        no += 1

    if no == 100:
        reset_button = driver.find_element_by_css_selector('a._1MCHh')
        reset_button.click()

apply_button = driver.find_element_by_css_selector("a[class='1wEWu _1dEyY'")
apply_button[no].click()
