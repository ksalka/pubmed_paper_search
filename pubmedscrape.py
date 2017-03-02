from Bio import Entrez
from Bio import Medline


# The term and the max number of results that can be found
MAX_COUNT = 20
TERM = 'Cystic Fibrosis MUC5AC MUC5B proteomics'

Entrez.email = 'yourEmail@gmail.com'
handle = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
result = Entrez.read(handle)

papers = []
authors = []
info = []
PubMedID = []
ids = result['IdList']

handle = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
records = Medline.parse(handle)

#Obtaining paper title, authors, and journal info
for record in records:
    papers.append(record.get("TI", "?"))
    authors.append(record.get("AU", "?"))
    info.append(record.get("SO", "?"))

for PMIDs in result['IdList']:
    PubMedID.append(PMIDs)


#Reading and writing to HTML file
readMe = open('templates/profile.html','r').readlines()
newfile = open('templates/profile.html','w')

#checking for duplicate papers
for line in readMe:
    for index,y in enumerate(PubMedID):
        if line == '\t\t\t<p class="PMID">PMID: '+y+'</p>\n':
            del papers[index]
            del authors[index]
            del info[index]
            del PubMedID[index]


#code for displaying # of papers currently on website
papercount = 0

for line in readMe:
    if line == '\t\t\t<p class="title">\n':
        papercount += 1
        
#Adding papers to html file
for line in readMe:
    if line[0:7] == '\t\t\t<dd>':
        newfile.write('\t\t\t<dd>'+str(papercount + len(papers))+'</dd>\n')
    elif line == '\t<div class="papers">\n':    
        newfile.write(line)
        for z in range(len(papers)):
            header = '\t\t<div>\n\t\t\t<p class="title">\n'
            line1 = '\t\t\t\t<a href="https://www.ncbi.nlm.nih.gov/pubmed/{0}">{1}</a>\n'.format(PubMedID[z], papers[z])
            line2 = '\t\t\t</p>\n\t\t\t<p class="authors">{0}</p>\n'.format(', '.join(authors[z]))
            line3 = '\t\t\t<p class="journal">{0}</p>\n'.format(info[z])
            line4 = '\t\t\t<p class="PMID">PMID: {0}</p>\n\t\t</div>\n'.format(PubMedID[z])
            newfile.write(header+line1+line2+line3+line4)
    elif line != '\t<div class="papers">\n' or line[0:7] != '\t\t\t<dd>':                
        newfile.write(line)

newfile.close()
