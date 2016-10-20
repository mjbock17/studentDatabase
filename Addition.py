def FileAddition():
    listfile1 = readFile('StudentInfo.txt','r',7)#Obtain List
    openfile1 = open('StudentInfo.txt', 'r')
    newfile1 = open('StudentInfoUpdate.txt', 'w')
    newfile1.write(openfile1.read()) ###clone of file1

    listfile2 = readFile('StudentInfo2.txt','r',8)#Obtain List
    openfile2 = open('StudentInfo2.txt', 'r')
    newfile2 = open('StudentInfoUpdate2.txt', 'w')
    newfile2.write(openfile2.read()) ###clone of file2
    
    newfile1.write('\n')
    for Heading in listfile1[0]: ### Creation of new values (information)
        value1=input('Please input ' + Heading + ': ')
        if Heading=='Student_ID':
            IdValue=value1 ###Necessary variable for creation of classes
        newfile1.write(value1 + '\t')

    classes = int(input('How many classes need to be added? ')) ###Creation of new values (classes)
    while classes>0:
        newfile2.write('\n' + IdValue + '\t') ###Creates new line, Adds student ID, and continues process
        for Heading in listfile2[0][1:]:
            value2=input('Please input ' + Heading + ': ')
            newfile2.write(value2 + '\t')
        classes -=1
        
    newfile1.close()
    newfile2.close()
    readnewfile1 = open('StudentInfoUpdate.txt', 'r')
    readnewfile2 = open('StudentInfoUpdate2.txt', 'r')
    replacefile1 = open('StudentInfo.txt', 'w')
    replacefile2 = open('StudentInfo2.txt', 'w')
    replacefile1.write(readnewfile1.read())
    replacefile2.write(readnewfile2.read())
