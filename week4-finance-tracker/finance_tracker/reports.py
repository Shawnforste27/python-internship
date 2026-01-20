from collections import defaultdict

def monthly_report(expenses):
    total = 0
    for e in expenses:
        total += float(e["amount"])
    return total


def category_breakdown(expenses):
    summary = defaultdict(float)

    for e in expenses:
        summary[e["category"]] += float(e["amount"])

    return summary
