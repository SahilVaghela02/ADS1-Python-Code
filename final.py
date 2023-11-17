# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:28:37 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt


def get_mortality_data():
    '''


    Returns
    -------
    dataframe.

    '''
    # Reading the csv file into dataframe
    life_expentancy_data = pd.read_csv('D:\Applied data science \
project\Life_Expentancy_Data1.csv', iterator=False)
    return life_expentancy_data


def get_hate_crime_data():
    '''


    Returns
    -------
    dataframe.

    '''
    #  Reading the csv file into dataframe
    hate_crimes_data = pd.read_csv(
        'D:\Applied data science project\hate_crimes.csv', iterator=False)
    return hate_crimes_data


def plot_line_chart(data):
    '''


    Returns
    -------
    None.

    '''
    # Specifying the columns for x and y axis respectively
    x_column = 'Year'
    y_column = 'Adult Mortality'

    # Different countries to include in chart
    countries = ['Afghanistan', 'Ghana', 'Finland', 'India', 'Zambia']
    print(data)
    plt.figure()
    # For creating line chart for specified countries
    for country in countries:
        countries_data = data[data['Country'] == country]
        plt.plot(countries_data[x_column],
                 countries_data[y_column], marker='o', label=country)

    # Finalising the chart
    plt.title('Mortality of Adults Over Years')
    plt.xlabel('Years')
    plt.ylabel('Mortality Numbers')
    plt.legend()
    plt.grid(True)


def plot_pie_chart(am_data):
    '''


    Returns
    -------
    None.

    '''
    ## For Pie Chart ##

    # Different countries to include in chart
    countries = ['Afghanistan', 'Ghana', 'Finland', 'India', 'Zambia']

    # Specifying data column
    data_column = 'Adult Mortality'

    # Specifying year for the data
    specified_year = 2014

    # Filtering the dataframe
    condition = (am_data['Year'] == specified_year) & \
        (am_data['Country'].isin(countries))

    # Checking for matching rows
    if am_data[condition].empty:
        print(f"No data for the selected countries in {specified_year}")
    else:
        plt.figure()
        # Creating pie chart for selected countries and selected year
        plt.pie(am_data[condition][data_column], labels=am_data[condition]
                   ['Country'], autopct='%1.1f%%', startangle=90)
        plt.axis('equal')

        plt.title(
            '{data_column} Distribution for Selected Countries \
in {specified_year}')


def plot_bar_chart(hate_df):
    '''


    Returns
    -------
    None.

    '''

    # Specifying the columns name
    city_column = 'state'
    income_column = 'median_household_income'

    # Specifying the states to show
    selected_states = ['Maryland', 'California', 'Alabama',
                       'Mississippi', 'Oregon']

    # Filtering the Dataframe for selected states
    filtered_data = hate_df[hate_df[city_column].isin(selected_states)]

    # Checking for data for selected states
    if filtered_data.empty:
        print("No data for the selected states.")
    else:
        plt.figure()
        # If lenghts matches it would create a bar graph
        if len(filtered_data[city_column]) != \
                len(filtered_data[income_column]):
            print("Lengths of data columns do not match.")
        else:
            # Creating bar graph for selected states
            plt.bar(filtered_data[city_column], filtered_data[income_column])

            # Finalisation of chart
            plt.title('Income for Selected states')
            plt.xlabel('City')
            plt.ylabel('Income')

            # Rotationing X-axis labels for better readability
            plt.xticks(rotation=45, ha='right')


# Main Function
mr_data = get_mortality_data()
plot_line_chart(mr_data)
plot_pie_chart(mr_data)

hc_data = get_hate_crime_data()
plot_bar_chart(hc_data)

plt.show()
