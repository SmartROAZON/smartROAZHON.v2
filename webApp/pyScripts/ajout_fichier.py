import pandas as pd
import sys
import os
import glob
import importlib


#mylist = glob.glob("../data/*.csv") + glob.glob("../data/*.txt")

#[print(os.path.basename(f)) for f in mylist]

importlib.reload(os)
#for root, dirs, files in os.walk("../data/"):  
#    for filename in files:
#        print(filename)


fileList=[]
for files in os.listdir("dataFiles/"):
    #print(files)
    #pd.read_csv(sys.argv[1], sep=sys.argv[2])
    name=os.path.basename(files)
    #print(name)
    if name.lower().endswith(('.txt','.csv')):
        with open("dataFiles/"+name,encoding="utf-8") as f:
            first_line = f.readline()
            #print(first_line)
            #print([name,first_line.split(";")])
            print([name,[[idx,val] for idx,val in enumerate(first_line.split(";"))]])
##    else:
##        data=pd.read_csv("dataFiles/"+name,sep=";")
##        #print(data.columns)
##        #fileList.append([name,data.columns])
##        print([name,data.columns])






#print(fileList)
