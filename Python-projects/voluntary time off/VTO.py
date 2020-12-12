from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import time
chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://aspectwfm.com/WFO/")
time.sleep(3)
driver.find_element_by_xpath('//*[@class="login-footer"]').click()
element = driver.find_element_by_id('userID')
element.send_keys("")
element = driver.find_element_by_id('password')
element.send_keys("")
driver.find_element_by_id('login').click()
driver.get("https://aspectwfm.com/WFO/default/WFM/IntraDayStaffingBalances")
time.sleep(7)
dropdown = driver.find_element_by_xpath('//*[@id="dialog-instance-WFM_ModuleDialog"]/div/div[2]/div/div/fieldset/ul/li[2]/div[2]/span/span/span')
action = ActionChains(driver)
action.move_to_element(dropdown).perform()
element = driver.find_element_by_xpath('//*[@id="dialog-instance-WFM_ModuleDialog"]/div/div[2]/div/div/fieldset/ul/li[2]/div[2]/span/span/span/input')
element.send_keys("MY DEPARTMENT")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dialog-instance-WFM_ModuleDialog"]/div/div[3]/div/button').click()
time.sleep(7)
