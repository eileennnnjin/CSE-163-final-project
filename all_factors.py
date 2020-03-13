import pandas as pd
import matplotlib.pyplot as plt


def numeric_factors(df):
    """
    Gives a U.S. accident dataset, plots pie charts that show the percentage
    of the range of each factor when severity is 4.
    """
    sev = df[df['Severity'] == 4]
    df1 = sev[sev['Temperature(F)'].notna()]
    df2 = sev[sev['Wind_Chill(F)'].notna()]
    df3 = sev[sev['Humidity(%)'].notna()]
    df4 = sev[sev['Pressure(in)'].notna()]
    df5 = sev[sev['Visibility(mi)'].notna()]
    df6 = sev[sev['Wind_Speed(mph)'].notna()]

    # cut each numeric factors into 5/10 buckets for drawing the pie chart
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

    plt.savefig('numerical factors.png')


def cate_factors(df):
    """
    Gives a U.S. accident dataset, plots pie charts that show the percentage
    of each category of each factor.
    """
    sev1 = df[df['Severity'] == 4]
    sev1 = sev1[['Side']]
    sev2 = df.loc[df['Severity'] == 4, 'Amenity':'Astronomical_Twilight']

    sev1['side'] = sev1['Side']
    sev2['amenity'] = sev2['Amenity']
    sev2['bump'] = sev2['Bump']
    sev2['crossing'] = sev2['Crossing']
    sev2['give_way'] = sev2['Give_Way']
    sev2['junction'] = sev2['Junction']
    sev2['no_exit'] = sev2['No_Exit']
    sev2['railway'] = sev2['Railway']
    sev2['roundabout'] = sev2['Roundabout']
    sev2['station'] = sev2['Station']
    sev2['stop'] = sev2['Stop']
    sev2['traffic_calming'] = sev2['Traffic_Calming']
    sev2['traffic_signal'] = sev2['Traffic_Signal']
    sev2['turning_loop'] = sev2['Turning_Loop']
    sev2['sunrise_sunset'] = sev2['Sunrise_Sunset']
    sev2['civil_twilight'] = sev2['Civil_Twilight']
    sev2['nautical_twilight'] = sev2['Nautical_Twilight']
    sev2['astronomical_twilight'] = sev2['Astronomical_Twilight']

    side_count = sev1.groupby(['Side'], as_index=False).count()
    amenity_count = sev2.groupby(['Amenity'], as_index=False).count()
    bump_count = sev2.groupby(['Bump'], as_index=False).count()
    crossing_count = sev2.groupby(['Crossing'], as_index=False).count()
    give_way_count = sev2.groupby(['Give_Way'], as_index=False).count()
    junction_count = sev2.groupby(['Junction'], as_index=False).count()
    no_exit_count = sev2.groupby(['No_Exit'], as_index=False).count()
    railway_count = sev2.groupby(['Railway'], as_index=False).count()
    roundabout_count = sev2.groupby(['Roundabout'], as_index=False).count()
    station_count = sev2.groupby(['Station'], as_index=False).count()
    stop_count = sev2.groupby(['Stop'], as_index=False).count()
    traffic_calming_count = sev2.groupby(['Traffic_Calming'],
                                         as_index=False).count()
    traffic_signal_count = sev2.groupby(['Traffic_Signal'],
                                        as_index=False).count()
    turning_loop_count = sev2.groupby(['Turning_Loop'],
                                      as_index=False).count()
    sunrise_sunset_count = sev2.groupby(['Sunrise_Sunset'],
                                        as_index=False).count()
    civil_twilight_count = sev2.groupby(['Civil_Twilight'],
                                        as_index=False).count()
    astronomical_twilight_count = \
        sev2.groupby(['Astronomical_Twilight'], as_index=False).count()
    nautical_twilight_count = sev2.groupby(['Nautical_Twilight'],
                                           as_index=False).count()

    fig, axs = plt.subplots(3, 6, figsize=(20, 10))
    axs[0, 0].pie(side_count['side'], labels=side_count['Side'],
                  autopct='%1.1f%%')
    axs[0, 1].pie(amenity_count['amenity'], labels=amenity_count['Amenity'],
                  autopct='%1.1f%%')
    axs[0, 2].pie(bump_count['bump'], labels=bump_count['Bump'],
                  autopct='%1.1f%%')
    axs[0, 3].pie(crossing_count['crossing'],
                  labels=crossing_count['Crossing'],
                  autopct='%1.1f%%')
    axs[0, 4].pie(give_way_count['give_way'],
                  labels=give_way_count['Give_Way'],
                  autopct='%1.1f%%')
    axs[0, 5].pie(junction_count['junction'],
                  labels=junction_count['Junction'],
                  autopct='%1.1f%%')
    axs[1, 0].pie(no_exit_count['no_exit'],
                  labels=no_exit_count['No_Exit'],
                  autopct='%1.1f%%')
    axs[1, 1].pie(railway_count['railway'],
                  labels=railway_count['Railway'],
                  autopct='%1.1f%%')
    axs[1, 2].pie(roundabout_count['roundabout'],
                  labels=roundabout_count['Roundabout'],
                  autopct='%1.1f%%')
    axs[1, 3].pie(station_count['station'],
                  labels=station_count['Station'],
                  autopct='%1.1f%%')
    axs[1, 4].pie(stop_count['stop'],
                  labels=stop_count['Stop'],
                  autopct='%1.1f%%')
    axs[1, 5].pie(traffic_calming_count['traffic_calming'],
                  labels=traffic_calming_count['Traffic_Calming'],
                  autopct='%1.1f%%')
    axs[2, 0].pie(traffic_signal_count['traffic_signal'],
                  labels=traffic_signal_count['Traffic_Signal'],
                  autopct='%1.1f%%')
    axs[2, 1].pie(turning_loop_count['turning_loop'],
                  labels=turning_loop_count['Turning_Loop'],
                  autopct='%1.1f%%')
    axs[2, 2].pie(sunrise_sunset_count['sunrise_sunset'],
                  labels=sunrise_sunset_count['Sunrise_Sunset'],
                  autopct='%1.1f%%')
    axs[2, 3].pie(civil_twilight_count['civil_twilight'],
                  labels=civil_twilight_count['Civil_Twilight'],
                  autopct='%1.1f%%')
    axs[2, 4].pie(astronomical_twilight_count['astronomical_twilight'],
                  labels=astronomical_twilight_count['Astronomical_Twilight'],
                  autopct='%1.1f%%')
    axs[2, 5].pie(nautical_twilight_count['nautical_twilight'],
                  labels=nautical_twilight_count['Nautical_Twilight'],
                  autopct='%1.1f%%')

    axs[0, 0].set_title('Side')
    axs[0, 1].set_title('Amenity')
    axs[0, 2].set_title('Bump')
    axs[0, 3].set_title('Crossing')
    axs[0, 4].set_title('Give Way')
    axs[0, 5].set_title('Junction')
    axs[1, 0].set_title('No Exit')
    axs[1, 1].set_title('Railway')
    axs[1, 2].set_title('Roundabout')
    axs[1, 3].set_title('Station')
    axs[1, 4].set_title('Stop')
    axs[1, 5].set_title('Traffic_Calming')
    axs[2, 0].set_title('Traffic_Signal')
    axs[2, 1].set_title('Turning Loop')
    axs[2, 2].set_title('Sunrise Sunset')
    axs[2, 3].set_title('Civil Twilight')
    axs[2, 4].set_title('Nautical Twilight')
    axs[2, 5].set_title('Atronomical Twilight')

    plt.savefig('categorical factors.png')
