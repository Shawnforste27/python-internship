import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    # BASIC METRICS
    def basic_metrics(self):
        return {
            "Total Sales": self.df["total_amount"].sum(),
            "Average Order": self.df["total_amount"].mean(),
            "Total Orders": len(self.df),
            "Unique Customers": self.df["customer_id"].nunique(),
        }

    # SALES BY CATEGORY
    def sales_by_category(self):
        return self.df.groupby("category")["total_amount"].sum().sort_values(ascending=False)

    # TOP PRODUCTS
    def top_products(self):
        return self.df.groupby("product_name")["total_amount"].sum().sort_values(ascending=False).head(10)

    # MONTHLY TREND
    def monthly_sales(self):
        monthly = self.df.groupby("month")["total_amount"].sum()
        monthly_growth = monthly.pct_change()*100
        return monthly, monthly_growth

    # CUSTOMER INSIGHTS
    def customer_analysis(self):
        customer_spend = self.df.groupby("customer_id")["total_amount"].sum()

        repeat_customers = (customer_spend > customer_spend.mean()).sum()
        clv = customer_spend.mean()

        return repeat_customers, clv

    # SALES FORECAST (Moving Average)
    def forecast(self, window=3):
        monthly, _ = self.monthly_sales()
        forecast = monthly.rolling(window).mean()
        return forecast
