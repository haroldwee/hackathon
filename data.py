import os
import pandas as pd
import math
import ast

'''Read file'''
path = 'PeekingDuck/data'
files = os.listdir(path)
result = [i for i in files if i.startswith('stats')]
df = pd.read_csv(('PeekingDuck/data/' + str(result[0])), sep=',' )
places = ["Block 329B Anchorvale Link", "Block 215 Yishun Ave 2", "Block 122 Potong Pasir Ave 1", "Block 575 Pasir Ris Street 52", "Block 182 Stirling Rd" ]
'''analyses csv file output from peekingduck'''
def countcat():
    avgcatlist = []
    for i in places:
        # print(i)
        x = df.loc[(df['filename'] == i + '.mov')]
        y = x['bbox_labels']
        z = list(y.values.ravel())
        '''editing the data format'''
        mylist = []
        for i in z:
            mylist.append(ast.literal_eval(i.replace(" ", ", ")))
        mylist2 = []
        '''get the number of cats detected in each frame'''
        for i in mylist:
            mylist2.append(len(i))
        '''get the average number of cats detected in the video'''
        catsum = 0
        avgcatno = 0
        for i in mylist2:
            catsum += i
        avgcatno = math.ceil(catsum/len(mylist))
        avgcatlist.append(avgcatno)
    return(avgcatlist)

countcat()