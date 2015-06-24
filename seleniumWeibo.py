# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ID = '00821043197019'
PW = 'wn9889zn1'
# cj 家庭購物
Keyword = 'cj%2520%25E5%25AE%25B6%25E5%25BA%25AD%25E8%25B3%25BC%25E7%2589%25A9'
PageNo = 10

driver = webdriver.Firefox()

# login first
driver.get('http://login.sina.com.cn/')
uid = driver.find_element_by_id('username')
upw = driver.find_element_by_id('password')
loginBtn = driver.find_element_by_class_name('smb_btn')

time.sleep(2)
uid.send_keys(ID)
upw.send_keys(PW)
loginBtn.click()

for page in range(PageNo):
    # sleep on a while
    time.sleep(3)
    # search on sina
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.COMMAND + 't')
    driver.get('http://s.weibo.com/weibo/' + Keyword + '&page=' + str(page))
    htmlRawText = str(page) + '_r.txt'
    htmlSplitted = str(page) + '_s.txt'

    """
        Save HTML Raw data
    """
    fraw = open(htmlRawText, "w")
    html_source = driver.page_source
    html_source = str(html_source)
    temp = html_source.splitlines()
    fraw.write(str(temp[15:]))
    fraw.close()

    """
        Save splitted data
    """
    fspd = open(htmlSplitted, "w")
    contents = driver.find_elements_by_class_name("WB_feed_detail")
    comments = driver.find_elements_by_class_name("feed_action")
    date = driver.find_elements_by_class_name("feed_from")

    for count in range(len(contents)):
        fspd.write(contents[count].text)
        # print(contents[count].text)
        try:
            fspd.write(comments[count].text)
            # print(comments[count].text)
        except:
            fspd.write("No comments")
            # print("No comments")
        try:
            fspd.write(date[count].text)
            # print(date[count].text)
        except:
            fspd.write("No date")
            # print("No date")
    fspd.close()
driver.close()
