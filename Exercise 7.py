def Modifier():
    select=input('Please select one: \n' + '1. Add \n' + '2. Modify \n' + '3. Remove \n')

    if select=='1':### Addition of Files
        openfile1 = open('StudentInfo.txt', 'r')
        newfile1 = open('StudentInfo.txt', 'w')
        newfile1.write(openfile1.read()) ###clone of file1
        
        openfile2 = open('StudentInfo2.txt', 'r')
        newfile2 = open('StudentInfo.txt', 'w')
        
        newfile2.write(openfile2.read()) ###clone of file2
        listfile1 = readFile('StudentInfo.txt','r',7)#Obtain List
        listfile2 = readFile('StudentInfo2.txt','r',8)#Obtain List
        
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
            
    if select=='2': ###Modification of scores
        listfile2 = readFile('StudentInfo2.txt', 'r', 8)
        Writefile2 = open('StudentInfo2.txt', 'w')
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
                for Listrange in range(4,8):
                    if listfile2[0][Listrange]==ScoreName:
                        NewValue=input('Please add the new value: ')
                        listfile2[LastClassNumber][Listrange]=NewValue
                        print('Value has been changed.')
                        print(' '.join(listfile2[LastClassNumber]))
            Counter -=1
            LastClassNumber -=1

        writeCounter=0
        while len(listfile2)>writeCounter:
            Writefile2.write('\t'.join(listfile2[writeCounter]) + '\n')
            writeCounter +=1
        
    if select=='3':
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

        ClassCounter=0
        endofList2=0
        while len(listfile2)>endofList2:
            if ID == listfile2[endofList2][0]:
                indexvalue = endofList2
                ClassCounter +=1
            endofList2 +=1
            print(endofList2 - ClassCounter, endofList2)
        del listfile2[endofList2 - ClassCounter: endofList2]
        print(listfile2)
