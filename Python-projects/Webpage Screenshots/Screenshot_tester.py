from selenium import webdriver
import time
from PIL import Image

items=[]

i = 0 
while 1:
    i += 1
    item = input('Enter links %d: '%i)
    if item=='':
        break
    items.append(item)

chrome_path = r"C:\Chromedriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.set_window_size(1920, 1080)
driver.get(items)

driver.save_screenshot('screenshot.png')


image = Image.open('screenshot.png')

image.show()

driver.quit()
