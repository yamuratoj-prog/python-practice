def collect_expenses(count):
    expenses = {}
    for _ in range(count):
        name = input("Название: ").strip().lower()
        amount = int(input("Сумма: "))
        expenses[name] = expenses.get(name, 0) + amount
    return expenses


def main():
    expenses = collect_expenses(5)

    total = sum(expenses.values())
    top_name = max(expenses, key=expenses.get)

    print(f"Всего: {total}")
    print(f"Самая дорогая: {top_name} ({expenses[top_name]})")


main()