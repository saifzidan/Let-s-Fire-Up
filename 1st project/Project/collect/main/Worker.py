import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import Master
os.environ["PATH"] += r"C:\Users\saifl\Selenium drivers"
driver = webdriver.Firefox()
items = Master.elements
for item in items:
    print(str(item.get_property("href")))
    if (
        item.get_property("href") != ""
        and item.get_property("href")
        != "https://support.google.com/websearch/answer/181196?hl=ar"
        and item.get_property("href")
        != "https://accounts.google.com/ServiceLogin?hl=ar&passive=true&continue=https://www.google.com/search%3Fclient%3Dfirefox-b-d%26q%3Dnlp&ec=futura_asy_dt_so_72487300_e"
        and item.get_property("href")
        != "https://www.google.com/travel/flights?client=firefox-b-d&sca_esv=1680a5829504f13b&output=search&q=nlp&source=lnms&fbs=AEQNm0AVC_jJd_qrmjGRq-GYjl-c7k6o9NR1cGzHPFI7rH7xsKb3AILNs7OTPKzCR6_BywPq_V52stt7sLRn4u9t7kN1wPvrCvHY7lbxsj1Qzgh0qSsVAtrBYjrpXdBe5TFg6hNtnQ94FVSaMFYp8hFz2YfH7w0Nx8zI6Osk6it-P6qd_We9GSgIBDviAxlMjs0SPQmpdaipKKzJzBIzHVGXL4IqK7mupKFtMMhiO0--JQF6_UzqcATAS63bqRAIFGco5AbUg1V_&ved=1t:200715&ictx=111"
        and item.get_property("href")
        != "https://www.google.com/safesearch?prev=https://www.google.com/search?client%3Dfirefox-b-d%26q%3Dnlp&sa=X&ved=2ahUKEwj118_P9IGHAxUqWUEAHXoFB3YQ8JsIegQICRAM"
        and item.get_property("href")
        != "https://www.google.com/safesearch?prev=https://www.google.com/search?client%3Dfirefox-b-d%26q%3Dnlp&sa=X&ved=2ahUKEwiQ7v6b9oGHAxXIX0EAHUCgCigQ8JsIegQIBxAM"
        and item.get_property("href")
        != "https://www.google.com/safesearch?prev=https://www.google.com/search?client%3Dfirefox-b-d%26q%3Dnlp&sa=X&ved=2ahUKEwif__rX9oGHAxWgR0EAHZVwADYQ8JsIegQIDRAM"
        
    ):
        driver.get(str(item.get_property("href")))
        element = driver.find_element(By.CSS_SELECTOR, "body")
        txt = driver.title.replace("|" , "").replace('"' , "").replace("'" , "").replace("?" , "") + ".txt"
        print(str(driver.title) + "\n" + "\n" + "\n")
        print(str(element.get_attribute("outerHTML")) + "\n")
        x = open(txt, "w", encoding="utf-8")
        x.write(str(element.get_attribute("outerHTML")) + "\n")
        x.close()
