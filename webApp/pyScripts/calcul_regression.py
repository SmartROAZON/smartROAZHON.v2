import pandas as pd
import sys
import os
import numpy as np
from sklearn import linear_model
from datetime import date

#samples call :         python calcul_regression.py Emploi.csv_0 Logement.csv_0 Emploi.csv_1 Logement.csv_2

#recupérer tous les arguments sous forme fichier.csv_indexColumn ou fichier.txt_indexColumn **
arguments=sys.argv[1:]


listFiles=[]

for value in arguments:
    l = value.split("_")
    fileName='_'.join(l[:-1])
    listFiles.append(fileName)


#list contenant les noms des fichiers reçus en args sans redondance sous forme fichier.csv ou fichier.txt
listFiles=list(set(listFiles))

#list qui contiendrait nos nom de fichier.csv ou fichier.txt avec les index columns regroupé, exemple comme suit :[ [ fichier.csv,[1,2] ] , [ fichier.txt,[5] ] ]
file_col=[]


for idx,val in enumerate(arguments):
    l = val.split("_")
    fileName='_'.join(l[:-1])
    if idx == 0:
        file_col.append([fileName,[l[-1]]])
    else:
        for i, value in enumerate(file_col):          
            if fileName == file_col[i][0]:
                list_to=file_col[i][1]
                list_to.append(l[-1])
                list_to.sort()
                break;
        else:
            file_col.append([fileName,[l[-1]]])



def calcul_regression_avec_temps(dataFile,usingColumn):
    ## retourne modele de l'equation sous forme y(column) = a * temps + b
    data=pd.read_csv(dataFile,sep=";",usecols=usingColumn)
    #print(data.columns[usingColumn[0]].lower())
    #if data.columns[usingColumn[0]].lower() == "année":
    #    print("continue")
    #else:
    #    print("pas de column année")
    #    exit(0)
    #data=data.reset_index()



    for index in range(1,len(data.columns)):
        reg = linear_model.LinearRegression()
        features=data[[data.columns[0]]]
        target=data.iloc[:,index]
        reg.fit(features,target)
        
        #print("regression de {0}".format(dataFile))
        print("{0}  =  {1} * {2} + {3}".format(data.columns[index],reg.coef_[0],data.columns[0],reg.intercept_))
        today = date.today() #avoir l'année d'aujourdhui et faire les prédictions dans 20 ans 
    
        predictions = reg.predict(np.array([x for x in range(today.year,today.year+21)]).reshape(-1, 1))
        df = pd.DataFrame(np.array([x for x in range(today.year,today.year+21)]).reshape(-1, 1), columns=[data.columns[0]])
        df[data.columns[index]]=predictions.astype(int)

        #print(df)
        #print(data.tail())

        
    
    return [reg,df]


path="../dataFiles/"
result=[]
for value in file_col:
    value[1] = list(map(int, value[1]))  #convert columns indexes all to int
    name=path+value[0]

    reg,df=calcul_regression_avec_temps(name,value[1])
    result.append([reg,df])

#result contient liste de : [ modele, dataframe Prediction dans 20 ans ]

#maintenant on faire la régression entre criteres et population

#print(result)



################
# size of target different de size of features (features contains predicted values also need to fix)
def calcul_regression_avec_population(populationFile,resRegAevcTemps):

    data=pd.read_csv(populationFile,sep=";")

    for index in range(1,len(data.columns)):
        reg = linear_model.LinearRegression()
        features=pd.DataFrame()
        for val in resRegAevcTemps:
            #val[1] => feature dataframe
            #data_logement[[data_logement.columns[len(data_logement.columns)-1]]]
            features=pd.concat([features,val[1][val[1].columns[len(val[1].columns)-1]]],axis=1)
            

        print(features)
        
        
        #features=data[[data.columns[0]]]
        target=data.iloc[:,index]

        print(target)
        reg.fit(features,target)
    
        print("{0}  =  {1} * {2} + {3}".format(data.columns[index],reg.coef_[0],data.columns[0],reg.intercept_))

    

    


calcul_regression_avec_population(path+"Population.csv",result)


