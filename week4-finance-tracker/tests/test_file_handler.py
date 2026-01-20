from finance_tracker.file_handler import save_expenses, load_expenses

save_expenses([])
data = load_expenses()
assert isinstance(data, list)

print("File handler test passed")
