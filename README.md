# Bird-Songs-Recognition


***Machine Learning Algorithm to identify different bird songs***

This program was created as a project for a DSP class at Georgia Tech. The task for the project was to create a a machine learning algorithm to identify different bird songs.

**Approach**
- Mel-frequency cepstral coefficients (MFCC) was choosen as a feature for machine learning. We used Matlab built-in function mfcc as the feature extractor for this project. The extracted features of the labeled recordings were stored as a CSV file for training. 
- Scikit - learn Library was used to create a Classifier for that created through training and later be used for prediction. 
- Any outcomes or guessings that below 0.7 will not show as a classified bird. 

