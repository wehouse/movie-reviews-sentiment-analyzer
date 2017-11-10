[![Docker Repository on Quay](https://quay.io/repository/wehouse/movie-reviews-sentiment-analyzer/status "Docker Repository on Quay")](https://quay.io/repository/wehouse/movie-reviews-sentiment-analyzer)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


# Movie Reviews Sentiment Analyzer

## Introduction
By using a well known dataset (Rotten Tomatoes reviews set). We will be demonstrating how to create a Natural Language Processing
classification system. Also our secondary aim is to demonstrate how to correctly functionalize such as a system using
microservices architecture

## Dataset
By using Pang and Lee's polarity sentiment dataset V2.0 [1]. This dataset consists of 2000 movie reviews that are painstakingly
categorized as positive and negative by authors. 

## Data Pre-processing
Dataset generously contributed by Pang and Lee is quite high quality in its completeness. All reviews are inside text files
that are uniquely idenfied via a notification

## Models
In order to analyze any dataset, we first need to have a model of explanation in mind. Each model has its strengths and
weaknesses which must be carefully evaluated.

In order of implementation, we used the following models:
1. Naive Bayes

## Results
In order to compare results of multiple models, we will be using the standard confusion matrix in order to evaluate test vs pred
accuracy. We will introduce other techniques of comparison in time.

### Naive Bayes Classifier
Confusion matrix yielded

|   	| 0  	| 1  	|
|---	|---	|---	|
| 0  	| 163  	| 37  	|
| 1  	| 67  	| 133  	|

This translates into accuracy of correctly predicting test values by 296/400 ~ %75


## How to deploy and run?
### From Code
Install requirements from requirements.txt via 
```
pip install -r requirements.txt
```
Afterwards
```
gunicorn app:api
```
Port 8000 u will have it launched that will only address 127.0.0.1 requests and can be accessed using the postman collection in repo.

### From Docker
Docker image is provided via Quay, its launch instructions are here:
[Container Registry](https://quay.io/repository/wehouse/movie-reviews-sentiment-analyzer?tab=settings)

postman collection in repo again will be the primary way to use it.

## References
1. This data was first used in Bo Pang and Lillian Lee,
``A Sentimental Education: Sentiment Analysis Using Subjectivity Summarization 
Based on Minimum Cuts'',  Proceedings of the ACL, 2004.