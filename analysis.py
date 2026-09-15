from pathlib import Path

import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates().copy()

    df["company"] = df["company"].fillna("Unknown")
    df["contract_type"] = df["contract_type"].fillna("Not Specified")
    df["contract_time"] = df["contract_time"].fillna("Not Specified")

    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

    return df


def export_mysql_safe_csv(df: pd.DataFrame, output_path: Path) -> None:
    mysql_df = df.copy()

    for column in mysql_df.select_dtypes(include="object").columns:
        mysql_df[column] = (
            mysql_df[column]
            .fillna("")
            .astype(str)
            .str.encode("ascii", errors="ignore")
            .str.decode("ascii")
        )

    mysql_df.to_csv(output_path, index=False, encoding="ascii")


def main():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "ai_job_market.csv"

    if not input_file.exists():
        raise FileNotFoundError(f"Could not find dataset at {input_file}")

    utf8_output = base_dir / "ai_job_market_utf8.csv"
    mysql_output = base_dir / "ai_job_market_mysql.csv"

    df = pd.read_csv(input_file)
    print("Original shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())

    df = clean_dataset(df)

    df_salary = df.dropna(subset=["salary_avg"]).copy()

    print("\nCleaned shape:", df.shape)
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    print("\nData types:")
    print(df.dtypes)
    print("\nSalary dataset shape:", df_salary.shape)
    print("\nFirst 5 cleaned records:")
    print(df.head())

    df.to_csv(utf8_output, index=False, encoding="utf-8-sig")
    export_mysql_safe_csv(df, mysql_output)

    print("\nUTF-8 CSV created successfully!")
    print(utf8_output)
    print("\nMySQL-ready CSV created successfully!")
    print(mysql_output)


if __name__ == "__main__":
    main()