## Reading File

def readFile(data,row,length): ###row=Read or Write, length=number of table headings
    datalist=[]
    file1=open(data)
    file2=file1.read()
    completelist=file2.split()
    while len(completelist)>0:
        list1=completelist[0:length]
        datalist=datalist+[list1]
        del completelist[0:length]
    return datalist
def IDRetrieval():
    ID=str(input("Please input Student ID: "))
    endofList=0
    file1=readFile('StudentInfo.txt','r',6)
    while len(file1)>endofList:
        if ID==file1[endofList][0]:
            return(" ".join(file1[0]) + "\n"+ "   ".join(file1[endofList]))
        else:
            endofList+=1
        if endofList==len(file1):
            ID=str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to program if incorrectly entered
            endofList=0
print(IDRetrieval())
