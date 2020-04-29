# written by Eduard Shuvaev and Hong Yee Cheah.

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from os.path import join

## the line to add specific dirrectiry for the project
os.chdir('project 4')

## the function to save results in the txt file
def SAVETEXT(input,fileused):
    f=open('output.txt','w')
    f.write(fileused+'.wav' + '\n')
    f.write('start'+'    ' +'end'+'    ' +'bird species'+ '\n')
    i=np.size(input)
    for k in range(0,i-1):
        if input[k]>0:
            bird=input[k]
            start=k*3
            end=(k+1)*3
            f.write(repr(start)+'    '+repr(end)+'    '+'bird'+repr(int(bird)) + '\n')
    f.close()

## Training data: coverting csv file to npy (csv file has MFCC data for each bird)

data1 = pd.read_csv("bird1.csv", sep=',', header=None)
data1 = np.asarray(data1)
np.save('bird1.npy', data1)

data2 = pd.read_csv("bird2.csv", sep=',', header=None)
data2 = np.asarray(data2)
np.save('bird2.npy', data2)

data3 = pd.read_csv("bird3.csv", sep=',', header=None)
data3 = np.asarray(data3)
np.save('bird3.npy', data3)

## Testing data: coverting csv file to npy (format MFCC)
test = '5E6BB766'
test11=test
data4 = pd.read_csv(test + '.csv', sep=',', header=None)
data4 = np.asarray(data4)
np.save(test + '.npy', data4)

## loading testing sounds (MFCC)
test_dir = test + '.npy'

## Load feature
root_dir1 = 'bird1.npy'
root_dir2 = 'bird2.npy'
root_dir3 = 'bird3.npy'
data = {}
splited_data = {}
label = {}
data['class1'] = np.load(join(root_dir1))
data['class2'] = np.load(join(root_dir2))
data['class3'] = np.load(join(root_dir3))
# data['class4'] = np.load(join(root_dir,'class4.npy'))
# data['class5'] = np.load(join(root_dir,'class5.npy'))

## Generate balance dataset:
for key in data:
    train,test = train_test_split(data[key] ,test_size = 0.2, random_state = 33)
    if 'train' not in splited_data:
        splited_data['train'] = train
        label['train'] = np.ones(len(train)) * int(key[-1])
    else:
        splited_data['train'] = np.append(splited_data['train'],train,axis=0)
        label['train'] = np.append(label['train'],np.ones(len(train)) * int(key[-1]))
    if 'test' not in splited_data:
        splited_data['test'] = test
        label['test'] = np.ones(len(test)) * int(key[-1])
    else:
        splited_data['test'] = np.append(splited_data['test'],test,axis=0)
        label['test'] = np.append(label['test'],np.ones(len(test)) * int(key[-1]))

## Training classifier
classifier = SVC(kernel='linear',probability=True)
classifier.fit(splited_data['train'], label['train'])

## Prediction for tested sounds
pr = np.load(test_dir)
pred_prop = classifier.predict_proba(pr)
pred_prop=np.amax(pred_prop,axis=1)

# print(pred_prop)
filters=pred_prop < 0.7
pred = classifier.predict(pr)
pred[filters] = 0

# print(pred)
SAVETEXT(pred, test11)

## Testing
accuracy = classifier.score(splited_data['test'], label['test'])
print(accuracy)
