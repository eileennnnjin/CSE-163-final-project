# Yujie He
# 1664470
# NetId: yh56
# Use Machine Learning to train the program to predict the
# severity of the traffic accident with given features.
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import pandas as pd

def fit_and_predict_severity(data):
    filtered = data.fillna(0)
    print(len(filtered))
    X = filtered.loc[:, ['Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)',
                         'Pressure(in)', 'Visibility(mi)',
                         'Wind_Speed(mph)', 'Precipitation(in)',
                         'Sunrise_Sunset']]
    print(len(X))
    X = pd.get_dummies(X)
    y = filtered['Severity']
    print(len(y))
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.20)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_test_pred))
    return mean_squared_error(y_test, y_test_pred)

def main():
    data = pd.read_csv('US_Accidents_Dec19.csv', na_values=0)
    print(len(data))
    print(fit_and_predict_severity(data))

if __name__ == '__main__':
    main()