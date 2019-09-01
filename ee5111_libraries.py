
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from datetime import datetime as dt

def csv_processing(filename,engine_number):
    engine_d = pd.read_csv(filename,delimiter=' |\n',header=None,engine='python')
    # To read the engine data

    Header = ['ID','Cycle','os 1','os 2','os 3']
    Header += ['sensor '+str(sensor_num) for sensor_num in range(1,len(engine_d.columns)-4)]
    # Initialize the headers

    engine_d.columns = Header # Insert headers for the data
    ID = ['FD00'+str(engine_number)+'_'+str(id) for id in range(1,len(engine_d.index)+1)]
    engine_d['ID'] = ID # Change the ID column

    engine_d['Timestamp'] = str(np.nan)
    engine_d['Matric Number'] = 'A0108484B'

    return engine_d

eng_d1 = csv_processing('train_FD001.txt',1)
now = dt.utcnow()
eng_d1.at[1,'Timestamp'] = str(now)
eng_d1.iloc[1]['Timestamp']
