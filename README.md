# Subreddit Classification Modeling
_Author: Hunter Henninger_ 


## Problem Statement
The goal of this study is to create a classification model using the Reddit API that can predict which subreddit a given post is from based on the words contained in that post. The two classes used in this project are the Buddhism and Taoism subreddits. In doing this, the fundamental differences and keywords of these two philoposphies are identified.


## Executive Summary
Natural language processing techniques are widely used to model the complexities of human language. Reddit, the 4th most visited site in the United States contains a vast collection of discussions and debate on various topics. The question can therefore be asked: can a classification model use NLP methods to predict the subreddit from which a post came from?
<br><br> 
This study begins by scraping posts from the Reddit API. The corpus of posts is lemmatized and vectorized in preparation for modeling. A comparison of classification models leads to the production of the most accurate model. Evaluation of the best model then guides the key interpretations and conclusions of the study.


### Subreddits

- [Buddhism](https://www.reddit.com/r/Buddhism/)  
- [Taoism](https://www.reddit.com/r/taoism/)  


## Contents:
- [01_Data_Wrangling](./01_Data_Wrangling.ipynb)  
- [02_Preprocessing_and_Modeling](./02_Preprocessing_and_Modeling.ipynb)  
- [03_Model_Evaluation_and_Insights](./03_Model_Evaluation_and_Insights.ipynb)  


## Key Remarks

Classifying subreddits using a logistic regression, because of its low bias-variance tradeoff, large R-squared, and its high degree of interpretability using coefficients, is the best model produced by this study. A 92.5% accuracy score confirms the ability of this model to correctly classify a given post. By ranking the predictive power of each token based on coefficient magnitude, significant topics/themes of each subreddit can be drawn and interpreted. Using this kind of classification model allows for quick learning of the each topic. For instance, someone that knows very little about Buddhism and Taoism can take away frequently discussed key terms of both religions.

#### Further Research:
- Incorporate more classes (religions) to the model and evaluate accuracy
- Latent Dirichlet Allocation
    - Use LDA techniques to gather key topics of a collection of posts or any sort of corpus

