def Modifier():
    select=input('Please select one: \n' + '1. Add \n' + '2. Modify \n' + '3. Remove \n')

    if select=='1':### Addition of Files
        FileAddition()
        
    if select=='2': ###Modification of scores
        FileMod()
        
    if select=='3':
        FileDel()
        
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
    
def FileMod():
    listfile2 = readFile('StudentInfo2.txt', 'r', 8)
    writefile2 = open('StudentInfo2.txt', 'w')
    
    ID = str(input("Please input Student ID: "))
    ClassCheck = 0
    Counter = 0 ###How many classes printed
    
    print('  '.join(listfile2[0][1:]))
    while len(listfile2)>ClassCheck:
        if ID == listfile2[ClassCheck][0]:
            print(("\t".join(listfile2[ClassCheck][1:]))) ###Prints only relevent semesters of courses pertaining to ID
            LastClassNumber = ClassCheck ###Will Store position of last class
            Counter +=1
        ClassCheck +=1
        
    CourseSelection = str(input('Please choose which course: ')) ###Looks for Course
    while Counter > 0:
        if listfile2[LastClassNumber][3]==CourseSelection:
            ScoreName= input('Which Catagory? ')
            for Listrange in range(4,8): ###range specifies score headings
                if listfile2[0][Listrange]==ScoreName: ###Looks for score heading selected
                    NewValue=input('Please add the new value: ')
                    listfile2[LastClassNumber][Listrange]=NewValue
                    print('Value has been changed.')
                    print(' '.join(listfile2[LastClassNumber]))
        Counter -=1
        LastClassNumber -=1

    writeCounter=0
    while len(listfile2) > writeCounter:
        if len(listfile2) == writeCounter:
            writefile2.write('\t'.join(listfile2[writeCounter]))
            writeCounter +=1
        else:
            writefile2.write('\t'.join(listfile2[writeCounter]) + '\n')
            writeCounter +=1
            
    writefile2.close()

def FileDel():
    listfile1 = readFile('StudentInfo.txt','r',7)#Obtain List
    newfile1 = open('StudentInfoUpdate.txt', 'w')
    
    listfile2 = readFile('StudentInfo2.txt','r',8)#Obtain List
    newfile2 = open('StudentInfoUpdate2.txt', 'w')

    ID = str(input("Please input Student ID: "))
    endofList1 = 0

    while len(listfile1)>endofList1: ###This section finds the student info and deletes it (info
        if ID == listfile1[endofList1][0]:
            indexvalue=endofList1
            break
        else:
            endofList1 +=1
        if endofList1 == len(listfile1):
            ID = str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to the while statement if ID incorrectly entered
            endofList1 = 0
    del listfile1[endofList1]

    ClassCounter=0 ###Deletion of student info (classes)
    endofList2=0
    while len(listfile2)>endofList2:
        if ID == listfile2[endofList2][0]:
            indexvalue = endofList2
            ClassCounter +=1
        endofList2 +=1
    del listfile2[endofList2 - ClassCounter: endofList2]

    writeCounter1 = 0
    while len(listfile1) > writeCounter1:
        if len(listfile1)-1 == writeCounter1:
            newfile1.write('\t'.join(listfile1[writeCounter1]))
            writeCounter1 +=1
        else:
            newfile1.write('\t'.join(listfile1[writeCounter1]) + '\n')
            writeCounter1 +=1

    writeCounter2 = 0                
    while len(listfile2) > writeCounter2:
        if len(listfile2)-1 == writeCounter2:
            newfile2.write('\t'.join(listfile2[writeCounter2]))
            writeCounter2 +=1
        else:
            newfile2.write('\t'.join(listfile2[writeCounter2]) + '\n')
            writeCounter2 +=1
            
    newfile1.close()
    newfile2.close()
    readfile1 = open('StudentInfoUpdate.txt', 'r')
    readfile2 = open('StudentInfoUpdate2.txt', 'r')
    writefile1 = open('StudentInfo.txt', 'w')
    writefile2 = open('Studentinfo2.txt', 'w')
    writefile1.write(readfile1.read())
    writefile2.write(readfile2.read())
    print("Student Deleted")
