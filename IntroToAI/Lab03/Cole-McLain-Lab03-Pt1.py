# Cole McLain 
# Lab 03 Pt 1
# 11/3/25

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
import pandas as pd

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

# # Vectorize the data
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

# Send data through tfidf
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Train model
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

# Get test set of data
twenty_test = fetch_20newsgroups(subset="test", categories=categories, shuffle=True)
docs_new = twenty_test.data

# Do transformations on test set
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

# Make prediction
predicted = clf.predict(X_new_tfidf)
print('General accuracy score: ' + str(np.mean(predicted == twenty_test.target)))
print(f"something {predicted}")

# Generate confusion matrix and pretty print
report = metrics.confusion_matrix(twenty_test.target, predicted)
panda_table = pd.DataFrame(report, index=categories, columns=categories)
print(panda_table)