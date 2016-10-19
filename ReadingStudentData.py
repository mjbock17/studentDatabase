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
                         '1. All Information \n' + '2. Year Identification \n' + '3. Course Information \n' +
                          '4. Grades \n' + '5. Add, Remove or Change Student \n' + '6. Exit \n')
        if Selection=='1':
            IDRetrieval() 
        elif Selection=='2':
            IDRetrieval()##Add function
        elif Selection=='3':
            IDRetrieval()## addfunction
        elif Selection=='4':
            IDRetrieval()##add fucntion
        elif Selection=='5':
            IDRetrieval()##add fucntion
        elif Selection=='6':
            Exit=False ##exits out
    
def IDRetrieval(): ###Finds ID and displays information
    ID = str(input("Please input Student ID: "))
    endofList = 0
    
    file1 = readFile('StudentInfo.txt','r',6)
    file2 = readFile('StudentInfo2.txt','r',8)
    
    while len(file1)>endofList: ###This section finds the student info
        if ID == file1[endofList][0]: 
            print(" ".join(file1[0]) + " " + " ".join(file2[0][1:]) + "\n" + "\t".join(file1[endofList]) + "  " + "\t".join(file2[endofList][1:])) ###Initial Heading/First Semester Listed. Use of Join
            break
        else:
            endofList+=1
        if endofList == len(file1):
            ID = str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to the while statement if ID incorrectly entered
            endofList = 0
            
    ###Checking for extra semesters of courses###
    ClassCheck = 0
    while len(file2)>ClassCheck:
        if ID == file2[ClassCheck][0]:
            while ID == file2[ClassCheck+1][0]:
                print(("\t" * 8) + "\t".join(file2[ClassCheck+1][1:])) ###Prints only relevent semesters of courses pertaining to ID
                ClassCheck+=1
        ClassCheck+=1



mainMenu()
