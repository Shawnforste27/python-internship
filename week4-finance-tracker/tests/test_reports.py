from finance_tracker.reports import monthly_report

data = [
    {"amount": 10},
    {"amount": 20}
]

assert monthly_report(data) == 30
print("Report test passed")
