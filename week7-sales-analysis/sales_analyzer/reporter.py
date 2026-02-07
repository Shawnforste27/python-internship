class ReportGenerator:

    def generate_summary(self, metrics, repeat_customers, clv):
        print("\n📊 EXECUTIVE SUMMARY")
        print("="*40)

        for k,v in metrics.items():
            print(f"{k}: {v:,.2f}")

        print(f"Repeat Customers: {repeat_customers}")
        print(f"Customer Lifetime Value: {clv:,.2f}")

        print("\n💡 RECOMMENDATIONS")
        print("- Focus marketing on top categories")
        print("- Improve retention programs")
        print("- Invest in high-value customers")
