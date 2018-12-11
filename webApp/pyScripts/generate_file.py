import pandas as pd
import sys
import os

print(sys.argv[2:])
path="datafiles/{0}".format(sys.argv[1])


if os.path.isfile(path):
    #print("génération de fichier")
    data=pd.read_csv(path,sep=";",usecols=[int(i) for i in sys.argv[2:]])
    #dataframe = data.filter(sys.argv[2:], axis=1)
    dataframe=data
    #new_path=path.replace(".*","_nettoye.csv")
    new_path= path.split(".")
    new_path=new_path[:-1]
    new_path="".join(new_path)
    new_path="{0}{1}".format(new_path,"_nettoye.csv")
    #print(new_path)
    dataframe.to_csv(new_path,sep=";",header=True,encoding='utf-8',index=False)
else:
    print("le fichier n'existe pas.")



print([int(i) for i in sys.argv[2:]])
