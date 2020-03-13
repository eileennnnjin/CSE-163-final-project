# Yujie He
# 1664470
# NetId: yh56
# Test the analysis function we wrote
import pandas as pd
from severity_prediction import fit_and_predict_severity
from all_factors import cate_factors
from all_factors import numeric_factors
from wind_speed import wind_speed


def main():
    # Load dataset
    df = pd.read_csv('US_Accidents_Dec19.csv')

    # Question 1:
    wind_speed(df)
    numeric_factors(df)
    cate_factors(df)

    # Question 2: Predict the severity of traffic accident
    # with machine learning model
    result = fit_and_predict_severity(df)
    print('Mean Squared Error:', result[0])
    print('Accuracy Score:', result[1])


if __name__ == '__main__':
    main()
