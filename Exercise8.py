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
