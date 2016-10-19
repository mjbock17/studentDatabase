## Reading File

def readFile(data,row,length): ###row=Read or Write, length=number of table headings
    datalist=[]
    file1=open(data)
    file2=file1.read()
    completelist=file2.split()
    while len(completelist)>0:
        list1=completelist[0:length]
        datalist=datalist+[list1] ###Creates a list of list
        del completelist[0:length]
    return datalist

def IDRetrieval():
    ID=str(input("Please input Student ID: "))
    endofList=0
    
    file1=readFile('StudentInfo.txt','r',6)
    file2=readFile('StudentInfo2.txt','r',8)
    
    while len(file1)>endofList:
        if ID==file1[endofList][0]: ###This section finds the student info
            print(endofList)
            print(" ".join(file1[0]) + " " + " ".join(file2[0][1:]) + "\n" + "\t".join(file1[endofList]) + "  " + "\t".join(file2[endofList][1:])) ###Heading with more than 1 semester
            break
        else:
            endofList+=1
        if endofList==len(file1):
            ID=str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to program if incorrectly entered
            endofList=0
            
    ###Checking for extra semesters of courses###
    ClassCheck=0
    while len(file2)>ClassCheck:
        if ID==file2[ClassCheck][0]:
            while ID==file2[ClassCheck+1][0]:
                print(("\t" * 8) + "\t".join(file2[ClassCheck+1][1:])) ###Prints only relevent semesters of courses###
                ClassCheck+=1
        ClassCheck+=1

IDRetrieval()
