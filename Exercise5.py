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
