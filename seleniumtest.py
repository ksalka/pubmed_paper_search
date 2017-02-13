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

SearchTerm = "Breast Cancer Proteomics treatment"

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

for x in range(20):
    for title in soup.find_all('p', class_="title")[x:x+1]:
        print str(x+1)+'.',title.text

    for authors in soup.find_all('p', class_="desc")[x:x+1]:
        print '  ',authors.text

    for details in soup.find_all('p', class_="details")[x:x+1]:
        print '  ',details.text
    
    for PMID in soup.find_all('dl', class_="rprtid")[x:x+1]:
        print '  ',PMID.text
        print
