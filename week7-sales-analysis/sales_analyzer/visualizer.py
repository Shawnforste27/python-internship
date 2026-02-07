import matplotlib.pyplot as plt

class Visualizer:

    def plot_monthly_trend(self, monthly):
        monthly.plot(marker="o")
        plt.title("Monthly Sales Trend")
        plt.savefig("data/reports/monthly_trend.png")
        plt.close()

    def plot_category_pie(self, category_sales):
        category_sales.head(5).plot(kind="pie", autopct="%1.1f%%")
        plt.title("Top Categories")
        plt.ylabel("")
        plt.savefig("data/reports/category_pie.png")
        plt.close()

    def plot_forecast(self, forecast):
        forecast.plot()
        plt.title("Sales Forecast")
        plt.savefig("data/reports/forecast.png")
        plt.close()
