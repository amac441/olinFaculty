#olin URL
url = "https://olin.wustl.edu/EN-US/Faculty-Research/Faculty/Pages/default.aspx"

#=====================
#SQL
#=====================
#import sqlite3
#sqlite_file = 'olin.sqlite3'
#conn = sqlite3.connect(sqlite_file)
#c = conn.cursor()
#log=open("log.txt",'a')

#=====================
#SELENIUM
#=====================
from selenium import webdriver
import time
import string, sys
import csv
from datetime import datetime
#wr=open('output.csv','w')
timestamp=datetime.now()
path_to_chromedriver = r"chromedriver.exe"

browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get(url)
time.sleep(4)         
daterow=False
skiplast=True

#=========================================
#<tbody><tr>
#    <td width="250" nowrap="nowrap">
                        
#    <a id="dlFac_ctl00_facName" href="FacultyDetail.aspx?username=argyres">Nicholas Argyres</a>
#    </td><td></td><td width="250" nowrap="nowrap">
                        
#    <a id="dlFac_ctl74_facName" href="FacultyDetail.aspx?username=tghani">Tarek Ghani</a>
#    </td><td></td><td width="250" nowrap="nowrap">
                        
#    <a id="dlFac_ctl148_facName" href="FacultyDetail.aspx?username=dmeyer24">David Meyer</a>
#    </td><td></td>
#    </tr><tr>
#    <td width="250" nowrap="nowrap">
                        
#    <a id="dlFac_ctl02_facName" href="FacultyDetail.aspx?username=daydin">Deniz Aydin</a>
#    </td><td></td><td width="250" nowrap="nowrap">
#=================================================


try:
    table = browser.find_element_by_tag_name("tbody")
    tds = table.find_elements_by_tag_name("td")
except:
    print "\nCant Access Site\n"
    log.write("Cant Access Site - "+str(datetime.now()))
    browser.close()
    raise

for td in tds: #each row
    links = td.find_elements_by_tag_name("a")
    for link in links:
        link.get_attribute('href')