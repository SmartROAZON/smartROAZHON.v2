import pandas as pd
import sys
import os

#data = pd.read_csv(sys.argv[1], sep=sys.argv[2])

#print(data.columns)



for files in os.listdir("../dataFiles/"):
    #print(files)
    #pd.read_csv(sys.argv[1], sep=sys.argv[2])
    name=os.path.basename(files)
    #print(name)
    with open("../dataFiles/"+name) as f:
        first_line = f.readline()
        print(first_line)
