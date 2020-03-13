# Yujie He(1664470, NetId: yh56), Jin Lin(1766362, NetId: jinl9)
# 03-12-2020
# Test the analysis function we wrote
import pandas as pd
from severity_prediction import fit_and_predict_severity
from all_factors import cate_factors
from all_factors import numeric_factors
from wind_speed import wind_speed


def main():
    """
    Test the functions from analysis programs
    """
    # Load dataset
    df = pd.read_csv('US_Accidents_Dec19.csv')

    # Question 1: Using pie charts to show the percentage of each range
    # of a given factor. 
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
