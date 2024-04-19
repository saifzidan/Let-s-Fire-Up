import os
from selenium import webdriver
from selenium.webdriver.common.by import By
search = input("search:")
link = "https://www.google.com/search?client=firefox-b-d&q=" + search
os.environ["PATH"] += r"C:\Users\saifl\Selenium drivers"
driver = webdriver.Firefox()
driver.get(link)
elements = driver.find_elements(By.CSS_SELECTOR, "a")
x = open ("Links.txt" , "w")
for element in elements:
    x.writelines(element.get_property("href")+'\n')
x.close()