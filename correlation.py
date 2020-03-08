from scipy.stats import pearsonr
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def do_corr(csv_file):
    """
    Gives a us accident dataset, plots scatter plots between differnt factors
    and the severity of the accident.
    """
    df = pd.read_csv(csv_file)
    sev = df[df['Severity'] == 4]
    df1 = sev[sev['Temperature(F)'].notna()]
    df2 = sev[sev['Wind_Chill(F)'].notna()]
    df3 = sev[sev['Humidity(%)'].notna()]
    df4 = sev[sev['Pressure(in)'].notna()]
    df5 = sev[sev['Visibility(mi)'].notna()]
    df6 = sev[sev['Wind_Speed(mph)'].notna()]
    
    # cut each numeric factors into 5 buckets for drawing the pie chart
    sev['temp'] = pd.cut(df1['Temperature(F)'], 5)
    sev['wind_chill'] = pd.cut(df2['Wind_Chill(F)'], 5)
    
    sev['humidity'] = pd.cut(df3['Humidity(%)'], 5)
    sev['pressure'] = pd.cut(df4['Pressure(in)'], 10)
    sev['visibility'] = pd.cut(df5['Visibility(mi)'], 10)
    sev['wind_speed'] = pd.cut(df6['Wind_Speed(mph)'], 10)
    
    temp_count = sev.groupby(['temp'], as_index=False).count()
    
    wind_chill_count = sev.groupby(['wind_chill'], as_index=False).count()
    
    humidity_count = sev.groupby(['humidity'], as_index=False).count()
    
    pressure_count = sev.groupby(['pressure'], as_index=False).count()
    
    visibility_count = sev.groupby(['visibility'], as_index=False).count()
    
    wind_speed_count = sev.groupby(['wind_speed'], as_index=False).count()

    # plot the pie charts
    fig, axs = plt.subplots(3, 2, figsize=(20, 10))
    axs[0, 0].pie(temp_count['Temperature(F)'], 
                  labels=temp_count['temp'],
                  autopct='%1.1f%%')
    
    axs[0, 1].pie(wind_chill_count['Wind_Chill(F)'], 
                  labels=wind_chill_count['wind_chill'], 
                  autopct='%1.1f%%')
    
    axs[1, 0].pie(humidity_count['Humidity(%)'], 
                  labels=humidity_count['humidity'], 
                  autopct='%1.1f%%')
    
    axs[1, 1].pie(pressure_count['Pressure(in)'], 
                  labels=pressure_count['pressure'], 
                  autopct='%1.1f%%')
    
    axs[2, 0].pie(visibility_count['Visibility(mi)'],
                  labels=visibility_count['visibility'], 
                  autopct='%1.1f%%')
    
    axs[2, 1].pie(wind_speed_count['Wind_Speed(mph)'],
                  labels=wind_speed_count['wind_speed'], 
                  autopct='%1.1f%%')
    
    axs[0, 0].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    axs[0, 1].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    axs[1, 0].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    axs[1, 1].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    axs[2, 0].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    axs[2, 1].legend(loc='upper left', bbox_to_anchor=(0.9, 0.1, 0.2, 0.5))
    
    axs[0, 0].set_title('Temperature(F)')
    axs[0, 1].set_title('Wind_Chill(F)')
    axs[1, 0].set_title('Humidity(%)')
    axs[1, 1].set_title('Pressure(in)')
    axs[2, 0].set_title('Visibility(mi)')
    axs[2, 1].set_title('Wind_Speed(mph)')

    plt.savefig('correlation.png')

def main():
    df = do_corr('US_Accidents_Dec19.csv')
    do_corr(df)

if __name__ == '__main__':
    main()
