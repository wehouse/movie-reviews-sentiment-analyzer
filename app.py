# -*- coding: utf-8 -*-
import falcon

from naive_bayes_resource import NaiveBayesResource


api = falcon.API()
api.add_route('/naive_bayes', NaiveBayesResource())
