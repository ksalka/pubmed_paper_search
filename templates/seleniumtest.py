from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import bs4 as bs
import urllib2

chrome_path = "/usr/local/Cellar/chromedriver/2.27/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)

#Website search
driver.get("https://www.ncbi.nlm.nih.gov/pubmed")

#Search entry and button
SearchFieldId = "term"
SearchButtonId = "search"


SearchFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(SearchFieldId))
SearchButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(SearchButtonId))

SearchTerm = "Cystic Fibrosis MUC5AC MUC5B Proteomics"

#Creating URL Term for BeautifulSoup
words = SearchTerm.split()
SearchString = ''

for x in range(SearchTerm.count(' ')+1):
    if x < SearchTerm.count(' '):
        SearchString = SearchString+words[x]+'+'
    else:
        SearchString = SearchString+words[x]

#Selenium Search
SearchFieldElement.clear()
SearchFieldElement.send_keys(SearchTerm)

SearchButtonElement.click()

#Getting papers in search

sauce = urllib2.urlopen('https://www.ncbi.nlm.nih.gov/pubmed/?term='+SearchString).read()
soup = bs.BeautifulSoup(sauce,'lxml')

papers = []
authors = []
info = []
PubMedID = []

for x in range(20):
    for title in soup.find_all('p', class_="title")[x:x+1]:
        #print str(x+1)+'.',title.text
        papers.append(title.text)

    for names in soup.find_all('p', class_="desc")[x:x+1]:
        #print '  ',names.text
        authors.append(names.text)

    for details in soup.find_all('p', class_="details")[x:x+1]:
        #print '  ',details.text
        info.append(details.text)
    
    for PMID in soup.find_all('dl', class_="rprtid")[x:x+1]:
        #print '  ',PMID.text
        PubMedID.append(PMID.text)
        print

driver.close()

#Reading and writing to HTML file
readMe = open('profile.html','r').readlines()
newfile = open('profile.html','w')

#checking for duplicate papers
for line in readMe:
    for index,y in enumerate(papers):
        if line == '\t\t<p class="title">'+y+'</p>\n':
            del papers[index]
            del authors[index]
            del info[index]
            del PubMedID[index]


#Adding papers to html file
count = 0

for line in readMe:
    if line == '\t<div>\n':    
        if count == 0:
            for z in range(len(papers)):
                newfile.write('\t<div>\n\t\t<p class="title">'+papers[z]+'</p>\n\t\t<p class="authors">'+authors[z]+'</p>\n\t\t<p class="journal">'+info[z]+'</p>\n\t\t<p class="PMID">'+PubMedID[z]+'</p>\n\t</div>\n')
                count += 1
    newfile.write(line)

newfile.close()
