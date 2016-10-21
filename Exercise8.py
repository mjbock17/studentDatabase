def infoSort():
    studentIDList = readFile('StudentInfo.txt','r', 7)
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
