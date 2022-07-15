from selenium import webdriver
import time

import yagmail
import os

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blank-features = AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def get_value(elem):
  value=float(elem.split(" ")[0])
  return value

def send_mails(value):
  sender='josuegallardolara1@gmail.com'
  receiver='jyelxjiqd@emlpro.com'
  subject='Stock Update'
  content=f'Your current stock of {value} has dropped prices.'
  
  yag=yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver, subject=subject, contents=content)
  print('Email Send')
  time.sleep(5)

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                    value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    value = str(get_value(element.text))
    
    if float(value) < -0.10:
      send_mails(value)
    print(value)

main()