from datetime import datetime, timedelta

# List to store transactions
txns = [
  {"type": "Purchase", "amount": 100.50, "date": "2024-01-14"},
  {"type": "Sale", "amount": 200.75, "date": "2024-01-14"},
  {"type": "Purchase", "amount": 50.20, "date": "2024-01-15"},
]

# Function to calculate transactions done yesterday
def txns_done_yesterday(txns_list):
  yesterday = datetime.now() - timedelta(days=1)
  yesterday_str = yesterday.strftime("%Y-%m-%d")
  yesterday_txns = [t for t in txns_list if t["date"] == yesterday_str]
  return len(yesterday_txns)

# Function to calculate total income and expense
def calc_total_income_expense(txns_list):
  total_income = sum(t["amount"] for t in txns_list if t["type"] == "Sale")
  total_expense = sum(t["amount"] for t in txns_list if t["type"] == "Purchase")
  return total_income, total_expense

# Example usage
yesterday_txns_count = txns_done_yesterday(txns)
total_income, total_expense = calc_total_income_expense(txns)

print(f"Transactions done yesterday: {yesterday_txns_count}")
print(f"Total Income: {total_income}")
print(f"Total Expense: {total_expense}")