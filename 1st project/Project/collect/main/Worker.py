import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import Master
os.environ["PATH"] += r"C:\Users\saifl\Selenium drivers"
driver = webdriver.Firefox()
items = Master.elements
x = open("Content.txt", "w", encoding="utf-8")
for item in items:
    print(str(item.get_property("href")))
    if (
        item.get_property("href") != ""
        and item.get_property("href")
        != "https://support.google.com/websearch/answer/181196?hl=ar"
        and item.get_property("href")
        != "https://accounts.google.com/ServiceLogin?hl=ar&passive=true&continue=https://www.google.com/search%3Fclient%3Dfirefox-b-d%26q%3Dnlp&ec=futura_asy_dt_so_72487300_e"
    ):
        driver.get(str(item.get_property("href")))
        driver.implicitly_wait(5)
        elements = driver.find_elements(By.CSS_SELECTOR, "p")
        for element in elements:
            x.writelines(element.text + "\n")
x.close()