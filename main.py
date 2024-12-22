import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class Webdriver:
    def __init__(self):
        self.service = Service(executable_path='./chromedriver')

        # 設定 webdriver 的選項
        # 增加參數，讓 chrome 啟動之後，不會自動關閉
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=self.service)

    def get_iframe(self):
        WebDriverWait(self.driver, 5, 2).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="content-frame"]')))

load_dotenv()
chrome = Webdriver()

# go to website
url = "https://www.ris.gov.tw/app/portal/671"
chrome.driver.get(url)

# get iframe
chrome.get_iframe()

try:
    # click next button
    next_button = chrome.driver.find_element(By.XPATH, '//*[@id="nextButton"]').click()

    # select city and region
    # chrome.get_iframe()
    city = Select(chrome.driver.find_element(By.ID, "city_areaCode"))
    city.select_by_value(os.getenv("CITY_AREA_CODE"))

    time.sleep(1)

    site = Select(chrome.driver.find_element(By.ID, "site_areaCode"))
    site.select_by_value(os.getenv("SITE_AREA_CODE"))

    # select marry register checkbox
    marry_register_checkbox = WebDriverWait(chrome.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="general_typeIds00005"]')))
    marry_register_checkbox.click()

    first_confirm_button = WebDriverWait(chrome.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/form/div[3]/button')))
    first_confirm_button.click()

    second_confirm_button = WebDriverWait(chrome.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/form/div[6]/button[2]')))
    second_confirm_button.click()

    # fill out personal information
    person_id = WebDriverWait(chrome.driver, 30).until(EC.visibility_of_element_located((By.ID, 'personId')))
    person_id.send_keys(os.getenv("PERSON_ID"))

    # 戶籍
    location = Select(chrome.driver.find_element(By.ID, "city_censusRegister"))
    location.select_by_value(os.getenv("CITY_REGISTER"))
    time.sleep(1)

    # 鄉鎮市區
    location_site = Select(chrome.driver.find_element(By.ID, "site_censusRegister"))
    location_site.select_by_value(os.getenv("SITE_REGISTER"))

    # 申請人
    apply_username = chrome.driver.find_element(By.ID, "contactPerson")
    apply_username.send_keys(os.getenv("CONTACT_PERSON"))

    # 聯絡電話
    contact_number = chrome.driver.find_element(By.ID, "contactNumber")
    contact_number.send_keys(os.getenv("CONTACT_NUMBER"))

    # 選擇驗證方式
    verify = WebDriverWait(chrome.driver, 30).until(EC.visibility_of_element_located((By.ID, 'cardType3')))
    verify.click()

    # 出生年月日
    chrome.driver.find_element(By.ID, "year_birthday").send_keys(os.getenv("YEAR_BIRTHDAY"))
    month = Select(chrome.driver.find_element(By.ID, "mon_birthday"))
    month.select_by_value(os.getenv("MON_BIRTHDAY"))
    day = Select(chrome.driver.find_element(By.ID, "day_birthday"))
    day.select_by_value(os.getenv("DAY_BIRTHDAY"))

    # 預約日期
    try:
        date = Select(chrome.driver.find_element(By.ID, "reservationDate"))
        date.select_by_value(os.getenv("REGISTER_DATE"))
        time.sleep(1)
    except Exception as e:
        raise Exception("登記日期不存在")

    # 預約時段
    try:
        reservation_time = Select(chrome.driver.find_element(By.ID, "reservationTime"))
        reservation_time.select_by_value(os.getenv("RESERVATION_TIME"))
    except Exception as e:
        raise Exception("登記時間區間不存在")

except Exception as e:
    print(f"Error: {e}")
