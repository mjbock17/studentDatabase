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
