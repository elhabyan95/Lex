#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from collections import defaultdict
# !pip3 install openxyl
import nltk
from nltk import ngrams
import numpy as np
def dunc(tex):
        
    lex = pd.ExcelFile('lexicons (1).xlsx')

    effv=pd.read_excel(lex,'effectivenes')
    sats=pd.read_excel(lex,'satisfaction')
    eff=pd.read_excel(lex,'efficiency')

    effectiveness =pd.concat([effv[["positive","negative"]],effv[["إيجابي","سلبي"]].rename(columns={"إيجابي":"positive","سلبي":"negative"})])
    efficiency=pd.concat([eff[["positive","negative"]],eff[["إيجابي","سلبي"]].rename(columns={"إيجابي":"positive","سلبي":"negative"})])
    satsfication=pd.concat([sats[["positive","negative"]],sats[["إيجابي","سلبي"]].rename(columns={"إيجابي":"positive","سلبي":"negative"})])

    effectiveness_POS=list(set(effectiveness["positive"].astype(str).to_list())-set(["nan"]))
    effectiveness_POS=dict(zip(effectiveness_POS,len(effectiveness_POS)*[1]))
    effectiveness_NEG=list(set(effectiveness["negative"].astype(str).to_list())-set(["nan"]))
    effectiveness_NEG=dict(zip(effectiveness_NEG,len(effectiveness_NEG)*[-1]))

    satsfication_POS=list(set(satsfication["positive"].astype(str).to_list())-set(["nan"]))
    satsfication_POS=dict(zip(satsfication_POS,len(satsfication_POS)*[1]))
    satsfication_NEG=list(set(satsfication["negative"].astype(str).to_list())-set(["nan"]))
    satsfication_NEG=dict(zip(satsfication_NEG,len(satsfication_NEG)*[-1]))

    efficiency_POS=list(set(efficiency["positive"].astype(str).to_list())-set(["nan"]))
    efficiency_POS=dict(zip(efficiency_POS,len(efficiency_POS)*[1]))
    efficiency_NEG=list(set(efficiency["negative"].astype(str).to_list())-set(["nan"]))
    efficiency_NEG=dict(zip(efficiency_NEG,len(efficiency_NEG)*[-1]))

    effectiveness_POS.update(effectiveness_NEG)
    satsfication_POS.update(satsfication_NEG)
    efficiency_POS.update(efficiency_NEG)

    default_effectiveness=defaultdict(int,effectiveness_POS)
    default_satsfication=defaultdict(int,satsfication_POS)
    default_efficiency=defaultdict(int,efficiency_POS)

    # x = input('please enter a sample tweet')
    # x =list(" ".join(token) for token in ngrams(x.split(),2))+x.split()+list(" ".join(token) for token in ngrams(x.split(),3))+list(" ".join(token) for token in ngrams(x.split(),4))+list(" ".join(token) for token in ngrams(x.split(),5))+list(" ".join(token) for token in ngrams(x.split(),6))
    x =list(" ".join(token) for token in ngrams(tex.split(),2))+tex.split()+list(" ".join(token) for token in ngrams(tex.split(),3))+list(" ".join(token) for token in ngrams(tex.split(),4))+list(" ".join(token) for token in ngrams(tex.split(),5))+list(" ".join(token) for token in ngrams(tex.split(),6))

    res=list(map(lambda x : [default_effectiveness[x],default_efficiency[x],default_satsfication[x]],x))
    resEFFV=pd.Series(list(map(lambda x:x[0],res))).mean()
    resEFF=pd.Series(list(map(lambda x:x[1],res))).mean()
    resSATS=pd.Series(list(map(lambda x:x[2],res))).mean()
    final=[resEFFV,resEFF,resSATS]
    finalRES = []
    for item in final:
        if item > 0:
            finalRES.append(1)
        elif item<0:
            finalRES.append(-1)
        else:
            finalRES.append(0)
    usability_score = np.sum(finalRES)

    print('The Effectiveness score is :' , finalRES[0])
    print('The Efficiency score is :' , finalRES[1])
    print('The Satsfication score is :' , finalRES[2])
    print('lenth' , len(finalRES))
    if usability_score == 3:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is High Usable'
        
    elif usability_score == 2:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is Medium Usable'
        
    elif usability_score == 1:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is Low Usable'

    elif usability_score == 0:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is Neutral Usable'
        
    elif usability_score == -1:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is Low Unusable'
        
    elif usability_score == -2:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is Medium Unusable'

    elif usability_score == -3:
        usability_score_2='The overall Usability score is :' , str(usability_score) , ' and it is High Unusable'

    return finalRES[0],finalRES[1],finalRES[2],usability_score_2
    # In[ ]:




