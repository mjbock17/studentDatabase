def FileMod():
    listfile2 = readFile('StudentInfo2.txt', 'r', 8)
    writefile2 = open('StudentInfo2.txt', 'w')
    
    ID = str(input("Please input Student ID: "))
    ClassCheck = 0
    Counter = 0 ###How many classes printed
    
    print('  '.join(listfile2[0][1:]))
    while len(listfile2)>ClassCheck:
        if ID == listfile2[ClassCheck][0]:
            print(("\t".join(listfile2[ClassCheck][1:]))) ###Prints only relevent semesters of courses pertaining to ID
            LastClassNumber = ClassCheck ###Will Store position of last class
            Counter +=1
        ClassCheck +=1
        
    CourseSelection = str(input('Please choose which course: ')) ###Looks for Course
    while Counter > 0:
        if listfile2[LastClassNumber][3]==CourseSelection:
            ScoreName= input('Which Catagory? ')
            for Listrange in range(4,8): ###range specifies score headings
                if listfile2[0][Listrange]==ScoreName: ###Looks for score heading selected
                    NewValue=input('Please add the new value: ')
                    listfile2[LastClassNumber][Listrange]=NewValue
                    print('Value has been changed.')
                    print(' '.join(listfile2[LastClassNumber]))
                    print(listfile2)
        Counter -=1
        LastClassNumber -=1

    writeCounter=0
    while len(listfile2) > writeCounter:
        if len(listfile2) == writeCounter:
            writefile2.write('\t'.join(listfile2[writeCounter]))
            writeCounter +=1
        else:
            writefile2.write('\t'.join(listfile2[writeCounter]) + '\n')
            writeCounter +=1
            
    writefile2.close()
