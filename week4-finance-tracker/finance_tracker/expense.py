from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        expense = Expense(date, amount, category, description)
        self.expenses.append(expense)

    def get_all(self):
        return self.expenses

    def search_by_category(self, category):
        return [e for e in self.expenses if e.category.lower() == category.lower()]

    def to_list(self):
        return [e.to_dict() for e in self.expenses]

    def load_from_list(self, data):
        self.expenses = []
        for item in data:
            self.expenses.append(
                Expense(
                    item["date"],
                    item["amount"],
                    item["category"],
                    item["description"]
                )
            )
