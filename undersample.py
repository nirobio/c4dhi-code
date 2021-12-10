from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter

# defining the dataset

X, y = make_classification(n_samples= 10000, weights=[.99])
# class distribution
print(Counter(y))
Counter({0: a, 1: b})
