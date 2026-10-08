import os
import pandas as pd


def calculate_demographic_data(print_data=True):

    folder_script = os.path.dirname(os.path.abspath(__file__))
    file_csv = os.path.join(folder_script, "adult.data.csv")

    df = pd.read_csv(file_csv)

    # 1. How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(
        df.loc[df["sex"] == "Male", "age"].mean(),
        1
    )

    # 3. What percentage of people have a Bachelor's degree?
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # 4. What percentage of people with advanced education
    #    (Bachelors, Masters, or Doctorate) make >50K?
    advanced_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (
            (df.loc[advanced_education, "salary"] == ">50K").sum()
            / advanced_education.sum()
        ) * 100,
        1
    )

    # 5. What percentage of people without advanced education make >50K?
    lower_education = ~advanced_education

    lower_education_rich = round(
        (
            (df.loc[lower_education, "salary"] == ">50K").sum()
            / lower_education.sum()
        ) * 100,
        1
    )

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # 7. What percentage of people who work the minimum number
    #    of hours per week have a salary >50K?
    min_hours_workers = df["hours-per-week"] == min_work_hours

    num_min_workers = min_hours_workers.sum()

    rich_percentage = round(
        (
            (
                df.loc[min_hours_workers, "salary"] == ">50K"
            ).sum()
            / num_min_workers
        ) * 100,
        1
    )

    # 8. What country has the highest percentage of people that earn >50K?
    country_salary = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(),
        1
    )

    # 9. What is the most popular occupation for those who earn >50K in India?
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelors degrees:",
            percentage_bachelors
        )
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print(
            "Min work time:",
            min_work_hours,
            "hours/week"
        )
        print(
            "Percentage of rich among those who work fewest hours:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people:",
            highest_earning_country_percentage
        )
        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }