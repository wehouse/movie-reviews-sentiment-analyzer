# Natural Language Processing

# Importing the libraries
import glob

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array

# Importing the dataset
data=[]
filepath = "txt_sentoken/pos/*.txt"
txt = glob.glob(filepath)
for textfile in txt:
    with open(textfile, 'r') as myfile:
        tmp_arr=[]
        tmp_arr.append(myfile.read().replace('\n', ''))
        data.append(tmp_arr)
data=array(data)
data_pos=np.insert(data,1,1,axis=1)

data=[]
filepath = "txt_sentoken/neg/*.txt"
txt = glob.glob(filepath)
for textfile in txt:
    with open(textfile, 'r') as myfile:
        tmp_arr=[]
        tmp_arr.append(myfile.read().replace('\n', ''))
        data.append(tmp_arr)
data=array(data)
data_neg=np.insert(data,1,0,axis=1)

data_combined=np.append(data_pos,data_neg,axis=0)

dataset = pd.DataFrame(data=data_combined,columns=['Review','Score'])

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 2000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 2000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

import pickle

pickle.dump(classifier, open( "naive_bayes_model.p", "wb" ) )
pickle.dump(cv,open( "count_vectorizer.p", "wb" ) )

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)