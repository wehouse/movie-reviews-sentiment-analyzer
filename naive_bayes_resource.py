# -*- coding: utf-8 -*-

import pickle
import nltk

class NaiveBayesResource:
    classifier={}
    cv={}
    def __init__(self):
        self.classifier = pickle.load( open( "naive_bayes_model.p", "rb" ) )
        self.cv = pickle.load(open('count_vectorizer.p', 'rb'))
        nltk.download('stopwords')
    
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        resp.media = quote

    def on_post(self, req, resp):      
        review = req.stream.read().decode('utf-8')
        import re
        from nltk.corpus import stopwords
        from nltk.stem.porter import PorterStemmer
        review = re.sub('[^a-zA-Z]', ' ', review)
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        X = self.cv.transform([review]).toarray()
        resp.media = self.classifier.predict(X)[0]

