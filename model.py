import numpy as np
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        bigness = (X[:,0] + X[:,2]) / 2
        return np.column_stack([X, bigness])


pipeline = Pipeline([
    ('features', FeatureEngineer()),
    ('scale', StandardScaler()),
    ('balance', SMOTE(random_state=42)),
    ('model', RandomForestClassifier(random_state=42))
])

# Create dataset
X, y = make_classification(n_samples=1000,n_features=4,n_informative=2,
                           weights=[0.9,0.1],random_state=42)

pipeline.fit(X,y)

def predict_fruit(values):
    values = np.array(values).reshape(1,-1)
    result = pipeline.predict(values)
    return int(result[0])


def predict_house(area, rooms, age):
    b = 10
    m1 = 1000
    m2 = 4
    m3 = 3
    price = b + m1*area + m2*rooms + m3*age
    return price

