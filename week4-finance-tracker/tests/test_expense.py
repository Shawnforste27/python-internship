from finance_tracker.expense import Expense

def test_expense():
    e = Expense("2026-01-01", 50, "Food", "Lunch")
    assert e.amount == 50

print("Expense test passed")
