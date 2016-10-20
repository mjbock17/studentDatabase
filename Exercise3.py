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
