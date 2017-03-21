import time
import urllib2
import requests
from selenium import webdriver

class Instagram():

    def __init__(self,ig_handle):

        self.ig_handle = ig_handle

        #INSTAGRAM FOLLOWERS

        instagram_url = 'https://www.instagram.com/'+ig_handle
        driver = webdriver.Chrome()
        driver.get(instagram_url)
        instagram_followers = driver.find_element_by_id('//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[2]/a/span')
        print instagram_followers
