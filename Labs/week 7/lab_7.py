#Task 1

import pandas as pd
import json

data_csv = [
    [1, "Ali", 22, "isl", 1, 50000, "BS"],
    [2, "Sara", None, "Lahore", 3, 70000, "MS"],
    [3, "Ahmed", 25, "Karachi", None, "?", "BS"],
    [4, "Fatima", 28, "Islamabad", 5, 90000, None],
    [5, "Usman", 21, "isl", 0, 40000, "BS"],
    [6, None, 30, "Lahore", 7, 85000, "PhD"]
]

columns = ["id", "name", "age", "city", "experience", "expected_salary", "education"]
df_csv = pd.DataFrame(data_csv, columns=columns)
df_csv.to_csv("applicants.csv", index=False)

data_json = [
    {"id": 1, "skills": ["python", "sql"]},
    {"id": 2, "skills": ["java", "c++"]},
    {"id": 3, "skills": None},
    {"id": 4, "skills": ["python", "ml"]},
    {"id": 5, "skills": ["html", "css"]}
]

with open("applicants_extra.json", "w") as f:
    json.dump(data_json, f)

df1 = pd.read_csv("applicants.csv")
df2 = pd.read_json("applicants_extra.json")

print(df1.head())
print(df1.dtypes)
print(df1.isnull().sum())
print(df1.shape)

print(df2.head())
print(df2.dtypes)
print(df2.isnull().sum())
print(df2.shape)

#Task 2

import pandas as pd

df1 = pd.read_csv("applicants.csv")
df2 = pd.read_json("applicants_extra.json")

df_merged = pd.merge(df1, df2, on="id", how="left")

print(df_merged)
print("Shape:", df_merged.shape)

#Task 3

import numpy as np

df = pd.read_csv("applicants.csv")
df_extra = pd.read_json("applicants_extra.json")

df = pd.merge(df, df_extra, on="id", how="left")

df["age"].fillna(df["age"].median(), inplace=True)

df["experience"].fillna(0, inplace=True)

df["expected_salary"] = df["expected_salary"].replace("?", np.nan)
df["expected_salary"] = df["expected_salary"].astype(float)
df["expected_salary"].fillna(df["expected_salary"].median(), inplace=True)

df["education"].fillna("Unknown", inplace=True)

df["name"].fillna("Unknown", inplace=True)

print(df.isnull().sum())

#Task 4

df = pd.read_csv("applicants.csv")

df["city"] = df["city"].replace("isl", "Islamabad")
df["city"] = df["city"].str.lower()

print(df["city"].unique())

#Task 5

import pandas as pd

df = pd.read_csv("applicants.csv")

df["experience"].fillna(0, inplace=True)

bins = [-1, 1, 5, float("inf")]
labels = ["junior", "mid", "senior"]

df["experience_level"] = pd.cut(df["experience"], bins=bins, labels=labels)

print(df[["experience", "experience_level"]])

#Task 6

df = pd.read_csv("applicants.csv")

df["expected_salary"] = df["expected_salary"].replace("?", None)
df["expected_salary"] = df["expected_salary"].astype(float)

df["age"].fillna(df["age"].median(), inplace=True)
df["experience"].fillna(0, inplace=True)
df["expected_salary"].fillna(df["expected_salary"].median(), inplace=True)

for col in ["age", "experience", "expected_salary"]:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print(df)

#Task 7

def preprocess_applicants(df):
    
    df["age"].fillna(df["age"].median(), inplace=True)
    df["experience"].fillna(0, inplace=True)
    
    df["expected_salary"] = df["expected_salary"].replace("?", np.nan)
    df["expected_salary"] = df["expected_salary"].astype(float)
    df["expected_salary"].fillna(df["expected_salary"].median(), inplace=True)
    
    df["education"].fillna("Unknown", inplace=True)
    df["name"].fillna("Unknown", inplace=True)

    df["city"] = df["city"].replace("isl", "Islamabad")
    df["city"] = df["city"].str.lower()

    bins = [-1, 1, 5, float("inf")]
    labels = ["junior", "mid", "senior"]
    df["experience_level"] = pd.cut(df["experience"], bins=bins, labels=labels)

    for col in ["age", "experience", "expected_salary"]:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    return df


df = pd.read_csv("applicants.csv")
df_clean = preprocess_applicants(df)

print(df_clean.head())

# Task 8

df1 = pd.read_csv("applicants.csv")
df2 = pd.read_json("applicants_extra.json")

df = pd.merge(df1, df2, on="id", how="left")


df["skill_count"] = df["skills"].apply(lambda x: len(x) if isinstance(x, list) else 0)

all_skills = set()

for skills in df["skills"]:
    if isinstance(skills, list):
        all_skills.update(skills)

for skill in all_skills:
    df[f"has_{skill}"] = df["skills"].apply(
        lambda x: 1 if isinstance(x, list) and skill in x else 0
    )

print(df)

