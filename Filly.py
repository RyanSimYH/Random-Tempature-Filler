#Declaring Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import random

#importing time
import time

#Options for Chrome
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_argument("--no-sandbox")


#List of Users
userList = ("")
pwdList = ("")

#Loop till all users done
loopCounter = 0
while loopCounter <= len(userList):

    #Creating Chrome Instance
    browser = webdriver.Chrome(executable_path='', chrome_options=option)
    browser.get("")


    #Select Person
    time.sleep(3)
    memberSelect = Select(browser.find_element_by_id("member-select"))
    memberSelect.select_by_value(userList[loopCounter])

    #Split Pin to individual Number
    pwdKey = [int(p) for p in str(pwdList[loopCounter])]

    #Enter Pin
    time.sleep(3)
    browser.find_element_by_id("ep1").send_keys(pwdKey[0])
    time.sleep(1)
    browser.find_element_by_id("ep2").send_keys(pwdKey[1])
    time.sleep(1)
    browser.find_element_by_id("ep3").send_keys(pwdKey[2])
    time.sleep(1)
    browser.find_element_by_id("ep4").send_keys(pwdKey[3])

    #Randomize Temp
    random.seed()
    randTemp=random.randrange(58,72)
    Temp = [int(x) for x in str(randTemp)]

    #Enter Temp
    browser.find_element_by_id("td1").send_keys('3')
    browser.find_element_by_id("td2").send_keys(Temp[0])
    browser.find_element_by_id("td3").send_keys(Temp[1])

    #Submit
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/button").click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="submit-temp-btn"]').click()

    #Close
    time.sleep(5)
    browser.quit()
    loopCounter+=1
quit()