from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import load_expenses, save_expenses, export_to_csv
from finance_tracker.reports import monthly_report, category_breakdown
from finance_tracker.utils import valid_amount


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        data = load_expenses()
        self.manager.load_from_list(data)

    def run(self):
        while True:
            print("\nPERSONAL FINANCE TRACKER")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Category Report")
            print("4. Monthly Total")
            print("5. Export CSV")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.category_report()
            elif choice == "4":
                self.monthly_total()
            elif choice == "5":
                export_to_csv(self.manager.to_list())
                print("Exported to CSV.")
            elif choice == "0":
                save_expenses(self.manager.to_list())
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def add_expense(self):
        date = input("Date (YYYY-MM-DD): ")
        amount = input("Amount: ")

        if not valid_amount(amount):
            print("Invalid amount.")
            return

        category = input("Category: ")
        desc = input("Description: ")

        self.manager.add_expense(date, amount, category, desc)
        save_expenses(self.manager.to_list())
        print("Expense added.")

    def view_expenses(self):
        for e in self.manager.get_all():
            print(f"{e.date} | {e.amount} | {e.category} | {e.description}")

    def category_report(self):
        data = category_breakdown(self.manager.to_list())
        for cat, total in data.items():
            print(cat, ":", total)

    def monthly_total(self):
        total = monthly_report(self.manager.to_list())
        print("Total Expenses:", total)
