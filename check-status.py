from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

with open('message.txt', 'r', encoding = 'utf-8') as message:
  message_list = list()
  text = message.read()
  message_list = text.split('\n')

def start():
  flag = False
  driver = webdriver.Chrome()
  driver.implicitly_wait(3)
  driver.get('https://web.whatsapp.com/')
  input('QR Kodu okut ve bir tusa bas')
  
  message_area = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p")

  while True:
    message_area.click()
    wp_source = driver.page_source
    soup = bs(wp_source, 'lxml')
    search = soup.find_all('div', {'class': ['p357zi0d', 'r15c9g6i', 'g4oj0cdv', 'ovllcyds', 'l0vqccxk', 'pm5hny62']})
    
    try:
      online = search[5].span.text
      print(online)

      if (online in ['çevrimiçi', 'online']) and flag == False:
        print('online')
        msgToSend = message_list[random.randint(0, len(message_list) -1 )]
        message_area.send_keys(msgToSend)
        message_area.send_keys(Keys.ENTER)
        flag = True

      elif online not in ['çevrimiçi', 'online']:
        print('Suanda cevrimdisi')
        flag = False
    except:
      print('Su an cevrimdisi')
      flag = False
      pass
    time.sleep(5)

start()