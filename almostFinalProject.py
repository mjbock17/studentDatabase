## Reading File

def readFile(data,row,length): ###row=Read or Write, length=number of table headings
    datalist = []
    file1 = open(data)
    file2 = file1.read()
    completelist = file2.split() ###Use of Split
    while len(completelist) > 0:
        list1 = completelist[0:length]
        datalist = datalist + [list1] ###Creates a list of list
        del completelist[0:length]
    return datalist

def mainMenu():

    Exit=True
    while Exit:
        Selection = input(" Welcome to the Student Database. Please select a number: \n" +
                         '1. All Information \n' + '2. Course Grades \n' + '3. Semester Classes and Grades \n' +
                          '4. Maximum and Minimum Grades \n' + '5. Add, Remove or Change Student \n' + '6. Student Year \n' + '7. Sorted Information \n' + '8. Exit \n')
        if Selection=='1':
            IDRetrieval() 
        elif Selection=='2':
            CourseRetrieval()
        elif Selection=='3':
            SemesterRetrieval()
        elif Selection=='4':
            MaxMinRetrieval()
        elif Selection=='5':
            Modifier()
        elif Selection=='6':
            ID1 = str(input("Please input Student ID: "))
            YearRetrieval(ID1)
        elif Selection=='7':
            infoSort()
        elif Selection=='8':
            Exit=False ##exits out
    
def IDRetrieval(): ###Finds ID and displays information

    ID = str(input("Please input Student ID: "))
    endofList = 0
    
    file1 = readFile('StudentInfo.txt','r',7)
    file2 = readFile('StudentInfo2.txt','r',8)
    
    while len(file1)>endofList: ###This section finds the student info
        if ID == file1[endofList][0]:
            indexvalue=endofList
##            print(" ".join(file1[0]) + " " + " ".join(file2[0][1:]) + "\n" + "\t".join(file1[endofList]) + "  " + "\t".join(file2[endofList][1:])) ###Initial Heading/First Semester Listed. Use of Join
            break
        else:
            endofList+=1
        if endofList == len(file1):
            ID = str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to the while statement if ID incorrectly entered
            endofList = 0

    ClassCheck = 0   ###Checking for extra semesters of courses###
    PrintHeading=True ###Will make sure Heading prints once
    while len(file2)>ClassCheck:
        if ID == file2[ClassCheck][0] and PrintHeading==False: ###Checks if Heading has been printed
            print(("\t" * 8) + "\t".join(file2[ClassCheck][1:])) ###Prints only relevent semesters of courses pertaining to ID
        if ID == file2[ClassCheck][0] and PrintHeading==True:
            print(" ".join(file1[0]) + " " + " ".join(file2[0][1:]) + "\n" + "\t".join(file1[indexvalue]) + "  " + "\t".join(file2[ClassCheck][1:])) ###Initial Heading/First Semester Listed. Use of Join
            PrintHeading=False
        ClassCheck+=1

def CourseRetrieval():  #Takes in student ID and course number as inputs and displays the score for the indicated class
    ID = str(input("Please input Student ID: "))
    course = str(input("Please input Course Number: ")).upper()
    studentIDList = readFile('StudentInfo2.txt','r',8)
    
    courseHeaderList = studentIDList[0][3:] #List which is later used to create the header of the table.
    headerCounter = 3    #initialization of varibles used for counters for print statements used in loops 
    header =""
    printCounter = 3
    studentGrades = ""
    
    while(headerCounter<8): #Displays the header 
        header = header + "\t" + studentIDList[0][headerCounter]
        headerCounter = headerCounter + 1
    print (header)
    
    found = False   
    counterID = 0 #this varible keeps track of the row position. 
    for i in range(len(studentIDList)):#Loop determines whether or not the ID exists
        if(ID == str(studentIDList[i][0])):
            found = True
            counterID = i-1
    if(found == False):
        print("There is no student associated with this ID")
    else:
        if course == studentIDList[counterID][3]:  #checks for the indicated class and prints the assocaited scores. 
            while(printCounter<8):
                studentGrades = studentGrades + "\t" + studentIDList[counterID][printCounter]
                printCounter = printCounter + 1
            print(studentGrades)
        elif course == studentIDList[counterID+1][3]:
            while(printCounter<8):
                studentGrades = studentGrades + "\t" + studentIDList[counterID+1][printCounter]
                printCounter = printCounter + 1
            print(studentGrades)
        else:
            print("This student exists but the class does not. ")

def SemesterRetrieval(): #Takes the studentID and the specified semester name as input and displays the grade for all the courses taken in the semester
    ID = str(input("Please input Student ID: "))
    semester = str(input("Please input the semester: "))
    studentIDList = readFile('StudentInfo2.txt','r',8)

    courseHeaderList = studentIDList[0][2:] #List which is later used to create the header of the table.

    headerCounter = 2    #initialization of varibles used for counters for print statements used in loops 
    header =""
    printCounter = 2
    studentGrades = ""

    while(headerCounter<8): #Displays the header 
        header = header + "\t" + studentIDList[0][headerCounter]
        headerCounter = headerCounter + 1
    print (header)

    found = False   
    counterID = 0 #this varible keeps track of the row position. 
    for i in range(len(studentIDList)): #Loop determines whether or not the ID exists
        if(ID == str(studentIDList[i][0])):
            found = True
            counterID = i-1
    if found == False:
        print("There is no student associated with this ID. ")
        
    else:
        if semester == studentIDList[counterID][2]:  #checks for the indicated semester and prints the associated scores. 
            while(printCounter<8):
                studentGrades = studentGrades + "\t" + studentIDList[counterID][printCounter]
                printCounter = printCounter + 1
            print(studentGrades)
        elif semester == studentIDList[counterID+1][2]:
            while(printCounter<8):
                studentGrades = studentGrades + "\t" + studentIDList[counterID+1][printCounter]
                printCounter = printCounter + 1
            print(studentGrades)
        else:
            print("This student exists but the indicated semester does not. ")

def MaxMinRetrieval():#takes the student ID as the input and and displays the course number
    ID = str(input("Please input Student ID: "))
    studentIDList = readFile('StudentInfo2.txt','r',8)
    
    ycounter = 4 #this variable keeps track of the column position in the list, it starts at 4 because the scores start at the 4th column
    maxScore = 0 #this varible stores the max score
    maxScoreCol = 0 
    minScore = 150
    minScoreCol = 0
    col2max = False #Determines what class the higest or lowest score was recieved
    col2min = False

    found = False 
    counterID = 0 #this varible keeps track of the row position. 
    for i in range(len(studentIDList)):#Loop determines whether or not the ID exists
        if(ID == str(studentIDList[i][0])):
            found = True
            counterID = i-1         
    if(found == False):
        print("There is no student associated with this ID")
    else:
        while(ycounter<8):#The following while loops determine the Min and Max Scores for both of the classes being taken by the student.
            if int(studentIDList[counterID][ycounter])>maxScore:
                maxScore = int(studentIDList[counterID][ycounter])
                maxScoreCol = ycounter
            ycounter = ycounter + 1

        ycounter = 4 #reinitialization so the counter can also be used to locate the minimum value

        while(ycounter<8):
            if int(studentIDList[counterID+1][ycounter])>maxScore:
                maxScore = int(studentIDList[counterID+1][ycounter])
                maxScoreCol = ycounter
                col2max = True 
            ycounter = ycounter + 1

        ycounter = 4
        
        while(ycounter<8):
            if int(studentIDList[counterID][ycounter])<minScore:
                minScore = int(studentIDList[counterID][ycounter])
                minScoreCol = ycounter
            ycounter = ycounter + 1

        ycounter = 4

        while(ycounter<8):
            if int(studentIDList[counterID+1][ycounter])<minScore:
                minScore = int(studentIDList[counterID+1][ycounter])
                minScoreCol = ycounter
                col2min = True
            ycounter = ycounter + 1

        classPosMax = counterID #Saves th location of the highest and lowest score in order to print out the corresponding headings.
        classPosMin = counterID
        
        if col2max == True:
            classPosMax = classPosMax + 1
        if col2min == True:
            classPosMin = classPosMin + 1
            
        print("The maximum score acheived by this student was in",studentIDList[classPosMax][3], "with a score of", maxScore, "under the category of ", studentIDList[0][maxScoreCol] )
        print("The minimum score acheived by this student was in",studentIDList[classPosMin][3], "with a score of", minScore, "under the category of ", studentIDList[0][minScoreCol] )


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

def YearRetrieval(ID):
    file1 = readFile('StudentInfo.txt','r',7)###Reading File
    endofList = 0
    while len(file1)>endofList: ###This section finds the student info
            if ID == file1[endofList][0]:
                year=file1[endofList][3]
                break
            else:
                endofList+=1
            if endofList == len(file1):
                ID = str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to the while statement if ID incorrectly entered
                endofList = 0
    if year=='2020':### Checks for Class Year
        print('Freshman')
    elif year=='2019':
        print('Sophomore')
    elif year=='2018':
        print('Junior')
    elif year=='2017':
        print('Senior')

def infoSort():
    studentIDList = readFile('StudentInfo.txt','r', 7)
    file2 = readFile('StudentInfo2.txt', 'r', 8)
    
    colCount = int(input("How would you like to sort your data? Please select a number \n" +
                       "0. Student ID \n" + "1. First Name \n" + "2. Last Name \n" +
                       "3. Class Year \n" + "4. Phone Number \n" + "5. Email ID \n" + "6. Major" + '\n'))#The selection made by the user identifies the column to be switched and sorted.
    Heading = studentIDList.pop(0)###Removes Heading
    rowCount = 0
    temp = ""

    while(rowCount<len(studentIDList)):#This while loop swaps the identified values for each student with the first value to be sorted.
        temp = studentIDList[rowCount][0]
        studentIDList[rowCount][0]=studentIDList[rowCount][colCount]
        studentIDList[rowCount][colCount]= temp
        rowCount = rowCount+1
    

    studentIDList.sort() #sorts the first index of each list of list which was previously switched

    rowCount=0 ###Needs to be 0 

    while(rowCount<len(studentIDList)):#returns the now sorted list to its original format. 
        temp = studentIDList[rowCount][0]
        studentIDList[rowCount][0]=studentIDList[rowCount][colCount]
        studentIDList[rowCount][colCount]= temp
        rowCount = rowCount+1

    studentIDList.insert(0,Heading) ###Puts Heading back in
    print(" ".join(studentIDList[0]) + " " + " ".join(file2[0][1:]) + "\n")

    File1counter = 1
    while len(studentIDList)>File1counter:
        ClassCheck = 0   ###Checking for extra semesters of courses###
        PrintHeading=True ###Will make sure Heading prints once
        ID = studentIDList[File1counter][0]
        while len(file2)>ClassCheck:
            if ID == file2[ClassCheck][0] and PrintHeading==False: ###Checks if Heading has been printed
                print(("\t"*8) + "\t".join(file2[ClassCheck][1:])) ###Prints only relevent semesters of courses pertaining to ID
            if ID == file2[ClassCheck][0] and PrintHeading==True:
                print(("\t").join(studentIDList[File1counter]) + "\t" + "\t".join(file2[ClassCheck][1:])) ###Initial Heading/First Semester Listed. Use of Join
                PrintHeading=False
            ClassCheck +=1           
        File1counter +=1





mainMenu()
