def infoSort():
    studentIDList = readFile('StudentInfo.txt','r',6)
    colCount = int(input("How would you like to sort your data? Please select a number \n" +
                       "0. Student ID \n" + "1. First Name \n" + "2. Last Name \n" +
                       "3. Phone Number \n" + "4. Email ID \n" + "5. Major" ))#The selection made by the user identifies the column to be switched and sorted.
    rowCount = 1
    temp = ""

    while(rowCount<len(studentIDList)):#This while loop swaps the identified values for each student with the first value to be sorted.
        temp = studentIDList[rowCount][0]
        studentIDList[rowCount][0]=studentIDList[rowCount][colCount]
        studentIDList[rowCount][colCount]= temp
        rowCount = rowCount+1

    studentIDList.sort() #sorts the first index of each list of list which was previously switched
        
    rowCount=1

    while(rowCount<len(studentIDList)):#returns the now sorted list to its original format. 
        temp = studentIDList[rowCount][0]
        studentIDList[rowCount][0]=studentIDList[rowCount][colCount]
        studentIDList[rowCount][colCount]= temp
        rowCount = rowCount+1

    print(studentIDList) # You can remove, this was just to test whether or not this shit worked.
