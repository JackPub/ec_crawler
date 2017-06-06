# encoding: utf-8
#import requests
import time #for timer
import codecs #unicode file operation
from selenium import webdriver #web simulator

#==================================================================================================
def fetch_online():
    target_url = 'https://tw.buy.yahoo.com/'
    print 'Fetch online: ' + target_url
    
    file_out = codecs.open('c_fetch_result.txt','w', "utf-8")
    driver = webdriver.Chrome('chromedriver\chromedriver') #use chrome drive
    driver.get(target_url)
    driver.set_window_position(0,0) #set browser location
    driver.set_window_size(1024,800) #set browser size
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scoll down to trigger request of recmdHotNew 
    time.sleep(5) #set timer to wait for response
    pageSource = driver.page_source
    file_out.write(pageSource)
    file_out.close()
    driver.close()  #close browser
    
    return pageSource
    
#==================================================================================================    
def fetch_file(inputfile):
    print 'Fetch file: ' + inputfile
    
    file_in = codecs.open(inputfile,'r', "utf-8")
    pageSource = file_in.read()
    file_in.close()
    return pageSource

#==================================================================================================
#fetch_online()
#fetch_file('c_fetch_result.txt')    