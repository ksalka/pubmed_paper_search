readMe = open('profile.html','r').readlines()
#newfile = open('profile.html','w')

papers = ['paper1', 'paper2', 'paper3']
authors = ['author1', 'author2', 'author3']
info = ['journal1', 'journal2', 'journal3']
PubMedID = ['PMID1', 'PMID2', 'PMID3']

#checking for duplicate papers
for x,y in enumerate(papers):
    if y == 'paper4':
        del papers[x]
        del authors[x]
        del info[x]
        del PubMedID[x]
    #print x,y 

for z in range(len(papers)):
    print papers[z], authors[z], info[z], PubMedID[z]


#Adding papers to html file
#count = 0

#for line in readMe:
#    if line[0:4] == '\t<p>':
#        if count == 0:
#            for x in papers[::-1]:
#                newfile.write('\t<p>'+x+'</p>\n')
#                count += 1
#    newfile.write(line)

#newfile.close()

