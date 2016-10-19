def CourseRetrieval(): # Finds the course number and displays the score information of that course
    course = str(input("Please input the requested class: "))

    allInformationStr = IDRetrieval()
    studentInfoList = allInformationStr.split("\n")
    heading = studentInfoList[0].split()[8:]    #creates the heading of the course data
    
    print(heading)
    
#I started over because after making the IDRetrieval method return a statement I forgot that that IDRetrival only returned the one class.
#So I stopped on line 7. I wil start over making this method independent of ID retrieval.    
