from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import time
import getpass

chrome_path = r"C:\Chromedriver\chromedriver.exe"
user_name = getpass.getpass("Username: ")
password = getpass.getpass("Password: ")
first_name = input('Lead travelers first name: ')
first_last = input('Lead travelers last name: ')
driver = webdriver.Chrome(chrome_path)
action = ActionChains(driver)
driver.get('https://switchfly.com/adm/login.cfm')
#login
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[8]/div/form[1]/div[1]/input').click()
user_login = driver.find_element_by_id('username')
user_login.send_keys(user_name)
#password
driver.find_element_by_xpath('/html/body/div[8]/div/form[1]/div[2]/input').click()
user_login = driver.find_element_by_xpath('/html/body/div[8]/div/form[1]/div[2]/input')
user_login.send_keys(password)
driver.find_element_by_xpath('/html/body/div[8]/div/form[1]/button').click()
#FTC Creation
driver.find_element_by_xpath('/html/body/header/div[2]/nav/ul/li[1]/a').click()
driver.find_element_by_xpath('/html/body/div[8]/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td/a[3]').click()
#Quick add room
#adults
adults = driver.find_element_by_name('adults')
adults.click()
action.key_down(Keys.ARROW_DOWN).perform()
#CRS
crs = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[1]/tbody/tr[2]/td[2]/select')
crs.click()
crs = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[1]/tbody/tr[2]/td[2]/select/option[1]')
crs.click()
#Status
status = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[1]/tbody/tr[6]/td[2]/select')
status.click()
status = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[1]/tbody/tr[6]/td[2]/select/option[5]')
status.click()
#Check-in
checkin = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[2]/tbody/tr[2]/td[2]/select')
checkin.click()
checkin = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[2]/tbody/tr[2]/td[2]/select/option[5]')
checkin.click()
#Dates for check-in
month = driver.find_element_by_xpath('//*[@id="date1_month"]')
month.click()
month = driver.find_element_by_xpath('//*[@id="date1_month"]/option[12]')
month.click()
day = driver.find_element_by_xpath('//*[@id="date1_day"]')
day.click()
day = driver.find_element_by_xpath('//*[@id="date1_day"]/option[31]')
day.click()
dates = driver.find_element_by_xpath('//*[@id="date1_year"]')
dates.click()
dates = driver.find_element_by_xpath('//*[@id="date1_year"]/option[20]')
dates.click()
#Dates for check-out
month = driver.find_element_by_xpath('//*[@id="date2_month"]')
month.click()
month = driver.find_element_by_xpath('//*[@id="date2_month"]/option[12]')
month.click()
day = driver.find_element_by_xpath('//*[@id="date2_day"]')
day.click()
day = driver.find_element_by_xpath('//*[@id="date2_day"]/option[31]')
day.click()
dates = driver.find_element_by_xpath('//*[@id="date2_year"]')
dates.click()
dates = driver.find_element_by_xpath('//*[@id="date2_year"]/option[20]')
dates.click()
checkout = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[2]/tbody/tr[3]/td[3]/select')
checkout.click()
checkout = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table[2]/tbody/tr[3]/td[3]/select/option[21]')
checkout.click()
driver.find_element_by_xpath('//*[@id="pageContent"]/form/input').click()
driver.find_element_by_xpath('//*[@id="confirm"]/div[3]/div[4]/a/span').click()
#Traveler Information
first_name_field = driver.find_element_by_xpath('//*[@id="traveler_1_firstname"]')
first_name_field.click()
first_name_field.send_keys(first_name)
last_name_field = driver.find_element_by_xpath('//*[@id="traveler_1_lastname"]')
last_name_field.click()
last_name_field.send_keys(first_last)
dob = driver.find_element_by_xpath('//*[@id="traveler_1_dob_year"]')
dob.click()
dob = driver.find_element_by_xpath('//*[@id="traveler_1_dob_year"]/option[92]')
dob.click()
addy = driver.find_element_by_xpath('//*[@id="traveler_1_address"]')
addy.click()
addy.send_keys('123 Fake St')
addy = driver.find_element_by_xpath('//*[@id="traveler_1_city"]')
addy.click()
addy.send_keys('state')
addy = driver.find_element_by_xpath('//*[@id="traveler_1_state"]')
addy.click()
addy = driver.find_element_by_xpath('//*[@id="traveler_1_state"]/option[55]')
addy.click()
email = driver.find_element_by_xpath('//*[@id="traveler_1_email"]')
email.click()
email.send_keys('nobody@gmail.com')
phone_field = driver.find_element_by_xpath('//*[@id="traveler_1_phone"]')
phone_field.click()
phone_field.send_keys('800345678')

