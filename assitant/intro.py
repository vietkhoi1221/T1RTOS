import os
import re
from selenium import webdriver
import urllib.request
import urllib.parse
urlopen = urllib.request.urlopen
encode = urllib.parse.urlencode   

def playmusic(song):
    global driver
    query_string = encode({"search_query" : song})
    html_content = urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.youtube.com/watch?v=" +search_results[0])

def stopmusic():
    driver.close()