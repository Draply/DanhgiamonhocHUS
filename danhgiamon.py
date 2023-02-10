from selenium import webdriver
import time
import csv

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService # Similar thing for firefox also!
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
from subprocess import CREATE_NO_WINDOW
import requests
MSV = '20001906'
Email = 'doanhduc_t65@hus.edu.vn'
def login_via(subList,stt):
    try:
        if stt<=8:
            stt = stt
        else:
            stt = stt%8
        if stt >=4 :
            b  = 500
        else:
            b=0
        if stt <=3 :
            a = stt*500
        else:
            a = (stt%4)*500
        NewlistVia = []
        with open('thongtin.txt', 'r') as f:
            reader = csv.reader(f, delimiter= '|', lineterminator ='\n')
            for i in reader:
                NewlistVia.append(i)
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-notifications')
        option.add_experimental_option("detach", True)
        chrome_service = ChromeService('chromedriver')
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(service=chrome_service,options=option)

        driver.set_window_rect(a,b,400,500)
        Tenmonhoc = subList[0]
        Mahocphan = subList[1]
        Tengiangvien = subList[2]

        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfYwgiE2AR4sC0DtOW_Y4X8BsUn0hnczYzxDBsBajsqKKle8A/viewform')
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")))
        time.sleep(10)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(MSV)
        time.sleep(1)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Email)
        time.sleep(1)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Mahocphan)
        time.sleep(1)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Tenmonhoc)
        time.sleep(1)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(Tengiangvien)
        time.sleep(1)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        ### Đánh giá môn học
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")))
        time.sleep(10)
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        ###
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        ####
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[10]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        ###
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]/div').click()
        time.sleep(1)
        ##
        driver.find_element('xpath','/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
        time.sleep(1)




    except Exception as e:
        print(e)
if __name__ == '__main__':
    list_via = []
    with open('thongtin.txt', 'r') as f:
        reader = csv.reader(f, delimiter= '|', lineterminator ='\n')
        for i in reader:
            list_via.append(i)
    Newlist_via = [ele for ele in list_via if ele != []]
    soluong = 10
    List_stt = []
    for stt in range(len(Newlist_via)):
        List_stt.append(stt)
    with ThreadPoolExecutor(max_workers=soluong) as executor:
        executor.map(login_via, Newlist_via,List_stt)
        executor.shutdown(wait=True)



