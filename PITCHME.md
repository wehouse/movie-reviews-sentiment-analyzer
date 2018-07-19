# Natural Language Processing

“Can we determine the underlying positivity or negativity of a transcribed conversation or email?”

---

## AGENDA
* What is natural language processing?
* What is the problem we are solving here?
* Analysis and Preliminary Conclusion
* What is the Hypothesis and Methodology?
* Experimental and Practical Significance
* More on p-value interpretation

---

## What is natural language processing?
Natural language processing (NLP) is an area of computer science and artificial intelligence concerned with the interactions between computers and human (natural) languages, 
in particular how to program computers to process and analyze large amounts of natural language data.


---

## What is the problem we are solving here?

- Can we determine the underlying positivity or negativity of a transcribed conversation or email?
- Why would that be valuable? It can lead to service call data analysis to figure out a Churn vector or service quality improvements analysis.
- What else can we glean from NLP? Age category or Origin or Sex of the caller... learn more about customers unintrusively.


---

## How to interpret results?

Is this model any good?

---

## Confusion Matrix

|   	| 0  	| 1  	|
|---	|---	|---	|
| 0  	| 159  	| 41  	|
| 1  	| 91  	| 109  	|

**Accuracy: %67**

---

## F1, precision and recall results
* Precision: 0.726667
* Recall: 0.545
* F1: 0.67