# Cole McLain 
# Lab 03 Pt 2
# 11/3/25

"""Build a sentiment analysis / polarity model

Sentiment analysis can be casted as a binary text classification problem,
that is fitting a linear classifier on features extracted from the text
of the user messages so as to guess whether the opinion of the author is
positive or negative.

In this examples we will use a movie review dataset.

"""

# Author: Olivier Grisel <olivier.grisel@ensta.org>
# With modifications by Cole McLain
# License: Simplified BSD

import sys
from sklearn.linear_model import Perceptron
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


if __name__ == "__main__":
    # Boolean to switch between Perceptron and LinearSVC models
    # LinearSVC seems to work better, leave False
    USING_PERCEPTRON = False


    # NOTE: we put the following in a 'if __name__ == "__main__"' protected
    # block to be able to use a multi-core grid search that also works under
    # Windows, see: http://docs.python.org/library/multiprocessing.html#windows
    # The multiprocessing module is used as the backend of joblib.Parallel
    # that is used when n_jobs != 1 in GridSearchCV

    # the training data folder must be passed as first argument
    # You will need to download the training data from https://github.com/scikit-learn/scikit-learn/tree/1.4.X/doc/tutorial/text_analytics/data/movie_reviews
    # and run the fetch_data.py script
    movie_reviews_data_folder = sys.argv[1]
    dataset = load_files(movie_reviews_data_folder, shuffle=False)
    print("n_samples: %d" % len(dataset.data))

    # split the dataset in training and test set:
    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.25, random_state=None)
    

    # TASK: Build a vectorizer / classifier pipeline that filters out tokens
    # that are too rare or too frequent
    if USING_PERCEPTRON:
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', Perceptron())
        ])
    else:
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LinearSVC())
        ])

    # TASK: Build a grid search to find out whether unigrams or bigrams are
    # more useful.
    # Fit the pipeline on the training set using grid search for the parameters
   
    if USING_PERCEPTRON:
        parameters = {
            'tfidf__ngram_range' : [(1, 1), (2, 2)],
            'tfidf__use_idf' : (True, False),
            'clf__alpha' : (1e-2, 1e-3)
        }
    else:
        parameters = {
            'tfidf__ngram_range' : [(1, 1), (2, 2)],
            'tfidf__use_idf' : (True, False),
            'clf__C' : (0.1, 0.01)
        }
    
    gs_clf = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
    gs_clf.fit(docs_train, y_train)

    # TASK: print the cross-validated scores for the each parameters set
    # explored by the grid search
    for param_name in sorted(parameters.keys()):
        print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

    # TASK: Predict the outcome on the testing set and store it in a variable
    # named y_predicted
    y_predicted = gs_clf.predict(docs_test)

    # Print the classification report
    print(metrics.classification_report(y_test, y_predicted,
                                        target_names=dataset.target_names))

    # Print and plot the confusion matrix
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)

  
    # import matplotlib.pyplot as plt
    # plt.matshow(cm)
    # plt.show()
