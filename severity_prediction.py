# Yujie He
# 1664470
# NetId: yh56
# 03-12-2020
# Use Machine Learning to train the program to predict the
# severity of the traffic accident with given features.
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import pandas as pd


def fit_and_predict_severity(data):
    """
    Predict the severity of traffic accident by learning
    from historical data.

    The model we use is classifier. The features of the model
    includes meteorological factors and traffic facility factors.
    """
    filtered = data.fillna(0)
    X = filtered.loc[:, ['Temperature(F)', 'Wind_Chill(F)',
                         'Humidity(%)', 'Pressure(in)',
                         'Visibility(mi)', 'Wind_Speed(mph)',
                         'Precipitation(in)', 'Sunrise_Sunset',
                         'Amenity', 'Bump', 'Crossing', 'Give_Way',
                         'Junction', 'No_Exit', 'Railway',
                         'Roundabout', 'Station', 'Stop',
                         'Traffic_Calming', 'Traffic_Signal',
                         'Turning_Loop']]
    X = pd.get_dummies(X)
    y = filtered['Severity']
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.20)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_test_pred)
    acs = accuracy_score(y_test, y_test_pred)
    return mse, acs
