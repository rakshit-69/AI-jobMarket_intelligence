import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("ai_job_market.csv")

# Basic cleaning
df["company"] = df["company"].fillna("Unknown")
df["contract_type"] = df["contract_type"].fillna("Not Specified")
df["contract_time"] = df["contract_time"].fillna("Not Specified")

df["created"] = pd.to_datetime(df["created"])
df["created_date"] = pd.to_datetime(df["created_date"])

print("Dataset loaded successfully!")
print("Total jobs:", len(df))

print("\n--- AI JOB DISTRIBUTION ---")

ai_jobs = df["is_ai_related"].value_counts()

print(ai_jobs)


ai_percentage = df["is_ai_related"].mean() * 100

print( f"AI-related jobs: {ai_percentage:.2f}%")



print("\n--- JOBS BY COUNTRY ---")

country_jobs = (
    df["country_name"]
    .value_counts()
)

print(country_jobs)



country_percentage = (
    df["country_name"]
    .value_counts(normalize=True) * 100
)

print("\nCountry percentage:")
print(country_percentage.round(2))



print("\n--- TOP JOB CATEGORIES ---")

top_categories = (
    df["category"]
    .value_counts()
    .head(10)
)

print(top_categories)



print("\n--- TOP JOB TITLES ---")

top_titles = (
    df["title"]
    .value_counts()
    .head(15)
)

print(top_titles)




salary_df = df.dropna(subset=["salary_avg"]).copy()

print("\n--- SALARY ANALYSIS ---")

print("Jobs with salary data:", len(salary_df))

print(
    "Average salary:",
    round(np.mean(salary_df["salary_avg"]), 2)
)

print(
    "Median salary:",
    round(np.median(salary_df["salary_avg"]), 2)
)

print(
    "Minimum salary:",
    round(np.min(salary_df["salary_avg"]), 2)
)

print(
    "Maximum salary:",
    round(np.max(salary_df["salary_avg"]), 2)
)




print("\n--- AVERAGE SALARY BY COUNTRY ---")

salary_by_country = (
    salary_df
    .groupby("country_name")["salary_avg"]
    .mean()
    .sort_values(ascending=False)
)

print(salary_by_country.round(2))






print("\n--- AI VS NON-AI SALARY ---")

ai_salary = (
    salary_df
    .groupby("is_ai_related")["salary_avg"]
    .agg(["count", "mean", "median"])
)

print(ai_salary.round(2))



print("\n--- HIGHEST SALARY RECORDS ---")

print(
    salary_df[
        [
            "title",
            "country_name",
            "salary_avg",
            "currency"
        ]
    ]
    .sort_values("salary_avg", ascending=False)
    .head(15)
)





print("\n--- LOWEST SALARY RECORDS ---")

print(
    salary_df[
        [
            "title",
            "country_name",
            "salary_avg",
            "currency"
        ]
    ]
    .sort_values("salary_avg")
    .head(15)
)




print("\n--- SALARY BY COUNTRY AND CURRENCY ---")

salary_summary = (
    salary_df
    .groupby(["country_name", "currency"])["salary_avg"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
)

print(salary_summary)



print("\n--- AI VS NON-AI SALARY BY COUNTRY ---")

ai_country_salary = (
    salary_df
    .groupby(["country_name", "currency", "is_ai_related"])["salary_avg"]
    .agg(["count", "mean", "median"])
    .round(2)
)

print(ai_country_salary)



print("\n--- CONTRACT TIME ---")
print(
    salary_df.groupby(
        ["country_name", "currency", "contract_time"]
    )["salary_avg"]
    .agg(["count", "median", "min", "max"])
    .round(2)
)




# Salary analysis dataset
salary_df = df.dropna(subset=["salary_avg"]).copy()

# Keep only full-time jobs
salary_df = salary_df[
    salary_df["contract_time"] == "full_time"
].copy()

print("\n--- CLEAN SALARY DATASET ---")
print("Salary records:", len(salary_df))

print("\nSalary records by country:")
print(salary_df["country_name"].value_counts())

print("\nSalary summary:")
print(
    salary_df
    .groupby(["country_name", "currency"])["salary_avg"]
    .agg(["count", "median", "mean", "min", "max"])
    .round(2)
)





print("\n--- AI VS NON-AI SALARY ---")

ai_salary = (
    salary_df
    .groupby(["country_name", "currency", "is_ai_related"])["salary_avg"]
    .agg(["count", "median", "mean"])
    .round(2)
)

print(ai_salary)





print("\n--- AI JOB DEMAND ---")

ai_jobs = df[df["is_ai_related"] == True].copy()

print("Total AI-related jobs:", len(ai_jobs))

print("\nTop AI job titles:")
print(
    ai_jobs["title"]
    .value_counts()
    .head(15)
)

print("\nTop AI job categories:")
print(
    ai_jobs["category"]
    .value_counts()
    .head(10)
)





print("\n--- AI JOBS BY COUNTRY ---")

ai_country = (
    ai_jobs["country_name"]
    .value_counts()
)

print(ai_country)

print("\nAI job percentage by country:")

ai_country_percentage = (
    pd.crosstab(
        df["country_name"],
        df["is_ai_related"],
        normalize="index"
    ) * 100
)

print(ai_country_percentage.round(2))






print("\nTop AI job titles:")
print(
    ai_jobs["title"]
    .value_counts()
    .head(15)
)

print("\nTop AI job categories:")
print(
    ai_jobs["category"]
    .value_counts()
    .head(10)
)




print("\n--- SKILL DEMAND ANALYSIS ---")

skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "generative ai",
    "aws",
    "azure",
    "google cloud",
    "tensorflow",
    "pytorch",
    "data science",
    "data analysis",
    "nlp",
    "javascript",
    "react",
    "docker",
    "kubernetes"
]

skill_counts = {}

for skill in skills:
    skill_counts[skill] = df["description"].str.contains(
        skill, case=False, na=False
    ).sum()

skill_demand = (
    pd.Series(skill_counts)
    .sort_values(ascending=False)
)

print(skill_demand)


print("\nAnalysis completed successfully!")


