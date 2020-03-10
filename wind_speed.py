import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def wind_speed(df):
    """
    Takes in a U.S. accident dataset, plots pie charts that show 
    the percentage of the each range of wind speed between -0.472 
    mph and 47.18 mph when severity is 4. 
    """
    sev = df[df['Severity'] == 4]
    df6 = sev[sev['Wind_Speed(mph)'].notna()]
    df6 = df6[(df['Wind_Speed(mph)'] > -0.472) & 
              (df['Wind_Speed(mph)'] <= 47.18)]
    df6['wind_speed'] = pd.cut(df6['Wind_Speed(mph)'], 5)
    wind_speed_count = df6.groupby(['wind_speed'], as_index=False).count()
    plt.pie(wind_speed_count['Wind_Speed(mph)'],
            labels=wind_speed_count['wind_speed'], 
            autopct='%1.1f%%')
    plt.legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    plt.title('Wind_Speed(mph)')
    plt.savefig('wind speed.png')


def main():
    df = pd.read_csv('US_Accidents_Dec19.csv')
    wind_speed(df)


if __name__ == '__main__':
    main()