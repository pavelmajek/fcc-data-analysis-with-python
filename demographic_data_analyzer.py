# Demographic Data Analyzer solution for freeCodeCamp Data Analysis with Python certification

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    mean = df[df["sex"] == "Male"].age.mean()
    average_age_men = mean.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_perc = (df["education"].value_counts()["Bachelors"] / df.education.count()) * 100

    percentage_bachelors = bachelors_perc.round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    filter_advanced = ["Bachelors", "Masters", "Doctorate"]
    advanced_ed = df["education"].isin(filter_advanced)
    more50k = df["salary"] == ">50K"
    h = len(df[advanced_ed & more50k]) / len(df[advanced_ed]) * 100

    # What percentage of people without advanced education make more than 50K?
    filter_advanced = ["Bachelors", "Masters", "Doctorate"]
    non_advanced_ed = ~df["education"].isin(filter_advanced)
    more50k = df["salary"] == ">50K"

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df["education"].isin(filter_advanced)
    lower_education = ~df["education"].isin(filter_advanced)

    # percentage with salary >50K
    higher_education_rich = round(h, ndigits=1)
    lower_education_rich = round(len(df[non_advanced_ed & more50k]) / len(df[non_advanced_ed]) * 100, ndigits=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df["hours-per-week"] == df["hours-per-week"].min())])

    rich_percentage = len(df[(df["hours-per-week"] == df["hours-per-week"].min()) & (df["salary"] == ">50K")]) / len(
        df[(df["hours-per-week"] == df["hours-per-week"].min())]) * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df["salary"] == ">50K"]["native-country"].value_counts() / df[
        "native-country"].value_counts() * 100).idxmax()
    highest_earning_country_percentage = round(
        (df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts() * 100).max(),
        ndigits=1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts()).idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
