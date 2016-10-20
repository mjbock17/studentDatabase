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

