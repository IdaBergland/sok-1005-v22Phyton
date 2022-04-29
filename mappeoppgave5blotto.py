# Mappeoppgave 5 Blotto

import blotto
import numpy as np


def player_strategy(n_battalions,n_fields):
    #defining the array:
    battalions=np.zeros(n_fields,dtype=int)
    
    #assigning 25 battalions to the first four battle fields:
    battalions[0:1]=3
    battalions[1:4]=25
    battalions[4:]=11
#Her har jeg tenkt at 25 i 3 vinduer og 3 i en for så 11 i 2. 
#håper på en god sjangse her, fikk ikke testet de siste rundene da
#jeg kun får error på min maskin og den går i svart, har gjort noen forsøk
#og det virket greit på starten før det gikk i svart.
    
    #asserting that all and no more than all battalions are used:
    battalions=battalions[np.random.rand(n_fields).argsort()]
    assert sum(battalions)==n_battalions
    
    return battalions


def computer_strategy(n_battalions,n_fields):
    battalions=np.zeros(n_fields,dtype=int)
    battalions[0:1]=10
    battalions[1:4]=20
    battalions[4: ]=15
    assert sum(battalions)==n_battalions
    return battalions

#blotto.run(6, 100, player_strategy, computer_strategy)

def call_battle(n_battalions,n_fields, player_strategy, computer_strategy):
    c_battlions=computer_strategy(n_battalions,n_fields)
    p_battlions=player_strategy(n_battalions,n_fields)

    diff=p_battlions-c_battlions
    points=sum(diff>0)-sum(diff<0)
 
    return int(points>0)-int(points<0)


def test_strategies(n_fields,n_battalions,player_strategy, computer_strategy):
    n_tests=100000
    r=0
    record=[]
    for i in range(n_tests):
        p=call_battle(n_battalions,n_fields,
            player_strategy, computer_strategy)
        record.append(p)
        r+=p
    return r/n_tests

r=test_strategies(6,100,player_strategy, computer_strategy)
print(r)

#sourses
#kode hentet fra:
#Espen Sirnes (2022) 8 - git,pythonfiler og IDE (version 1.0)
#  [Source code]. https://github.com/espensirnes/notebooks/blob/main/8%20-%20git%2C%20pythonfiler%20og%20IDE.ipynb

