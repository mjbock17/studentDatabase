def MaxMinRetrieval():#takes the student ID as the input and and displays the course number
    ID = int(input("Please input Student ID: "))
    studentIDList = readFile('StudentInfo2.txt','r',8)

    counter = 1 #this variable keeps track of the row position in the list
    ycounter = 4 #this variable keeps track of the column position in the list, it starts at 4 because the scores start at the 4th column
    maxScore = 0 #this varible stores the max score
    maxScoreCol = 0 
    minScore = 150
    minScoreCol = 0
    col2max = False
    col2min = False

    found = True   #used by the loops to determine whether or not to end
    while(counter<(len(studentIDList)-1)):   #checks for the indicated student ID 
        if ID == studentIDList[counter][0]:
            print("found")
            break
        else:
            counter = counter + 1
        if counter<(len(studentIDList)-1):
            found = False
            
    if found == False:
        print("There is no student associated with this ID. ")
    else:
        while(ycounter<8):
            if int(studentIDList[counter][ycounter])>maxScore:
                maxScore = int(studentIDList[counter][ycounter])
                maxScoreCol = ycounter
            ycounter = ycounter + 1

        ycounter = 4 #reinitialization so the counter can also be used to locate the minimum value

        while(ycounter<8):
            if int(studentIDList[counter+1][ycounter])>maxScore:
                maxScore = int(studentIDList[counter+1][ycounter])
                maxScoreCol = ycounter
                col2max = True 
            ycounter = ycounter + 1

        ycounter = 4
        
        while(ycounter<8):
            if int(studentIDList[counter][ycounter])<minScore:
                minScore = int(studentIDList[counter][ycounter])
                minScoreCol = ycounter
            ycounter = ycounter + 1

        ycounter = 4

        while(ycounter<8):
            if int(studentIDList[counter+1][ycounter])<minScore:
                minScore = int(studentIDList[counter+1][ycounter])
                minScoreCol = ycounter
                col2min = True
            ycounter = ycounter + 1

        classPosMax = counter
        classPosMin = counter
        
        if col2max == True:
            classPosMax = classPosMax + 1
        if col2min == True:
            classPosMin = classPosMin + 1
            

        print("The maximum score acheived by this student was in",studentIDList[classPosMax][3], "with a score of", maxScore, "under the category of ", studentIDList[0][maxScoreCol] )
        print("The minimum score acheived by this student was in",studentIDList[classPosMin][3], "with a score of", minScore, "under the category of ", studentIDList[0][minScoreCol] )

