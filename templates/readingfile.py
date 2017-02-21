readMe = open('profile.html','r').readlines()
#newfile = open('profile.html','w')

papers = ['paper1', 'paper2', 'This is paper #3']

#checking for duplicate papers
for line in readMe:
    if line[0:4] == '\t\t<p':
        print line


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

