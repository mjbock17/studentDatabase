#student ID

import random
for counter in range(50):
    ID=""
    for counter in range(6):
        a=random.randrange(0,10)
        ID=ID+str(a)
    print(ID)
