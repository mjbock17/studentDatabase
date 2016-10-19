def YearRetrieval(ID):
    file1 = readFile('StudentInfo.txt','r',7)###Reading File
    endofList = 0
    while len(file1)>endofList: ###This section finds the student info
            if ID == file1[endofList][0]:
                year=file1[endofList][3]
                break
            else:
                endofList+=1
            if endofList == len(file1):
                ID = str(input("No ID exists, Please enter a new ID: "))### Checks for ID. Sends user back to the while statement if ID incorrectly entered
                endofList = 0
    if year=='2020':### Checks for Class Year
        print('Freshman')
    elif year=='2019':
        print('Sophomore')
    elif year=='2018':
        print('Junior')
    elif year=='2017':
        print('Senior')
