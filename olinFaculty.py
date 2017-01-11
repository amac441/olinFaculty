#olin URL
url = "https://olin.wustl.edu/EN-US/Faculty-Research/Faculty/Pages/default.aspx"

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

browser2 = webdriver.Chrome(executable_path = path_to_chromedriver)


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

file = open("profout.csv",'w')
csvfile = csv.writer(file,delimiter=',')
csvfile.writerow(['name','title','url','email','ed','bio','cvlink',"interests","publications"])

for td in tds: #each row
    links = td.find_elements_by_tag_name("a")
    for link in links:
        prof=[]

        newu = link.get_attribute('href')
        name = link.text

        #get professor
        browser2.get(newu)      
        title = browser2.find_element_by_class_name("headinfo").find_element_by_tag_name("h2").text

        try:
            bio = browser2.find_element_by_id("bio").text
        except:
            bio='nobio'

        try:
            cvlink=browser2.find_element_by_id("lnkCV").get_attribute("href")
        except:
            cvlink="nocv"
        
        try:
            email = browser2.find_element_by_id("mail")
            email = email.find_element_by_tag_name("a").text
        except:
            email="noemail"

        try:
            ed=browser2.find_element_by_id("ed").text
        except:
            ed="noed"

        try:
            interst = browser2.find_element_by_id("pnlRsch")
            int = interst.find_element_by_id("rsch").text
        except:
            int="noint"

        prof=[name,title,newu,email,ed,bio,cvlink,int]

        #recent pubs
        try:
            pubs = browser2.find_element_by_id("pnlPubs")
            pubslist = pubs.find_elements_by_tag_name("li")
            for pub in pubslist:
                prof.append(pub.text)
        except:
            pass

        csvfile.writerow([unicode(s).encode("utf-8") for s in prof])

file.close()

#with open('eggs.csv', 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])

browser.close()
browser2.close()


#========== bio =============
#<div class="headinfo"><h1>Nicholas S. Argyres</h1><div class="biophoto"><img width="176px" alt="Nicholas S. Argyres" src="http://apps.olin.wustl.edu/images/photos/argyres.jpg">
    
#<p><span id="bio">Professor Argyres joined the Olin Business School faculty in 2008. He was previously Associate Professor at Boston University School of Management. Prior to that, he was Assistant Professor at the Marshall School of Business, University of Southern California. Professor Argyres' research is focused on topics in organizational strategy: organizational boundaries; contracting and inter-organizational relationships; internal organization structure; technology and organization; organizational dissent.</span></p>
#<p><span id="web"><a id="lnkCV" href="http://apps.olin.wustl.edu/faculty/argyres/CV.pdf" target="_blank" class="">Nicholas S. Argyres' Curriculum Vitae</a><br></span></p>
    
#<p><span id="mail"><b>Email:</b> <a href="mailto:argyres@wustl.edu" class="">argyres@wustl.edu</a></span></p>
    
#<p><span id="lblphone"><strong>Phone:</strong> (314) 935-6391</span></p>
        
#<p><span id="ed">PhD 1993, University of California Berkeley<br>
#</span></p>
#</div>
#<h2>Vernon W. &amp; Marion K. Piper Professor of Strategy</h2>
#<div id="pnlExp">

#======== publications ======
#<div id="pnlPubs">
#<h3>Selected Publications:</h3>
#<p>
#<span id="pubs" class="label">
#</span>
#</p>
#<ul>
#<li>"Knowledge Inheritance, Vertical Integration, and Entrant Survival in the Early U.S. Auto Industry"<i></i>, <i> Academy of Management Journal (forthcoming)</i>, Issue 59, 1-19, with R. Mostafa</li>
#<li>"Dominant Designs, Innovation Shocks and the Follower's Dilemma"<i></i>, <i> Strategic Management Journal</i>, Issue 36, 216-234, with L. Bigelow, J. Nickerson, 2015</li><li>"Capabilities, Transaction Costs and Firm Boundaries"<i></i>, <i> Organization Science</i>, Issue 23, 6, 1643-1657, with T. Zenger, 2012</li></ul><p></p>