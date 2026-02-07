from sales_analyzer.data_loader import DataLoader
from sales_analyzer.data_cleaner import DataCleaner
from sales_analyzer.analyzer import SalesAnalyzer
from sales_analyzer.visualizer import Visualizer
from sales_analyzer.reporter import ReportGenerator

def main():
    loader = DataLoader("data/raw/sales_data.csv")
    df = loader.load_csv()

    cleaner = DataCleaner()
    df = cleaner.clean(df)

    analyzer = SalesAnalyzer(df)
    visualizer = Visualizer()
    reporter = ReportGenerator()

    metrics = analyzer.basic_metrics()
    category_sales = analyzer.sales_by_category()
    monthly, growth = analyzer.monthly_sales()
    forecast = analyzer.forecast()
    repeat_customers, clv = analyzer.customer_analysis()

    visualizer.plot_monthly_trend(monthly)
    visualizer.plot_category_pie(category_sales)
    visualizer.plot_forecast(forecast)

    reporter.generate_summary(metrics, repeat_customers, clv)

if __name__ == "__main__":
    main()
