import bs4 as bs
import urllib2

SearchTerm = "Cystic Fibrosis MUC5AC MUC5B Proteomics"

#Creating URL Term for BeautifulSoup
words = SearchTerm.split()
SearchString = ''

for x in range(SearchTerm.count(' ')+1):
    if x < SearchTerm.count(' '):
        SearchString = SearchString+words[x]+'+'
    else:
        SearchString = SearchString+words[x]

#Getting papers in search

sauce = urllib2.urlopen('https://www.ncbi.nlm.nih.gov/pubmed/?term='+SearchString).read()
soup = bs.BeautifulSoup(sauce,'lxml')

papers = []
authors = []
info = []
PubMedID = []

for x in range(20):
    for title in soup.find_all('p', class_="title")[x:x+1]:
        papers.append(title.text)

    for names in soup.find_all('p', class_="desc")[x:x+1]:
        authors.append(names.text)

    for details in soup.find_all('p', class_="details")[x:x+1]:
        info.append(details.text)
    
    for PMID in soup.find_all('dd')[x:x+1]:
        PubMedID.append(PMID.text)


#Reading and writing to HTML file
readMe = open('profile.html','r').readlines()
newfile = open('profile.html','w')

#checking for duplicate papers
for line in readMe:
    for index,y in enumerate(PubMedID):
        if line == '\t\t<p class="PMID">'+'PMID: '+y+'</p>\n':
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
                newfile.write('\t<div>\n\t\t<p class="title">\n\t\t\t<a href="https://www.ncbi.nlm.nih.gov/pubmed/'+PubMedID[z]+'">'+papers[z]+'</a>\n\t\t</p>\n\t\t<p class="authors">'+authors[z]+'</p>\n\t\t<p class="journal">'+info[z]+'</p>\n\t\t<p class="PMID">'+'PMID: '+PubMedID[z]+'</p>\n\t</div>\n')
                count += 1
    newfile.write(line)

newfile.close()
