import numpy as np

class DataCleaner:

    def clean(self, df):
        print("🧹 Cleaning data...")

        # remove duplicates
        df = df.drop_duplicates()

        # convert date
        df["order_date"] = pd.to_datetime(df["order_date"])

        # fill missing numbers with median
        num_cols = df.select_dtypes(include=np.number).columns
        for col in num_cols:
            df[col] = df[col].fillna(df[col].median())

        # fill categorical with mode
        cat_cols = df.select_dtypes(include="object").columns
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        # new column
        df["month"] = df["order_date"].dt.to_period("M")

        print("✅ Cleaning complete")
        return df
