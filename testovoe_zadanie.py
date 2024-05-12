class Transaction:
    """
    Представляет запись о доходе или расходе.
    """

    def __init__(self, date: str, category: str, amount: float, description: str):
        """
        Инициализирует объект Transaction.

        :param date: Дата записи в формате "ГГГГ-ММ-ДД"
        :param category: Категория записи ("Доход" или "Расход")
        :param amount: Сумма записи
        :param description: Описание записи
        """
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


def load_transactions(filename: str) -> list[Transaction]:
    """
    Загружает записи о транзакциях из файла.

    :param filename: Имя файла для чтения
    :return: Список объектов Transaction
    """
    transactions = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                date, category, amount, description = line.strip().split(', ', 3)
                transaction = Transaction(date, category, float(amount), description)
                transactions.append(transaction)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Будет создан новый файл.")
    return transactions


def save_transactions(transactions: list[Transaction], filename: str):
    """
    Сохраняет записи о транзакциях в файл.

    :param transactions: Список объектов Transaction для сохранения
    :param filename: Имя файла для записи
    """
    try:
        with open(filename, 'w') as file:
            for transaction in transactions:
                line = f"{transaction.date}, {transaction.category}, {transaction.amount}, {transaction.description}\n"
                file.write(line)
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")


def show_balance(transactions: list[Transaction]):
    """
    Выводит текущий баланс, а также отдельно доходы и расходы.

    :param transactions: Список объектов Transaction
    """
    total_income = sum(t.amount for t in transactions if t.category == "Доход")
    total_expense = sum(t.amount for t in transactions if t.category == "Расход")
    balance = total_income - total_expense
    print(f"Баланс: {balance}")
    print(f"Доходы: {total_income}")
    print(f"Расходы: {total_expense}")


def add_transaction(transactions: list[Transaction]):
    """
    Добавляет новую запись о доходе или расходе.

    :param transactions: Список объектов Transaction
    """
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    category = input("Введите категорию (Доход/Расход): ")
    amount = float(input("Введите сумму: "))
    description = input("Введите описание: ")
    transaction = Transaction(date, category, amount, description)
    transactions.append(transaction)
    print("Запись успешно добавлена!")


def edit_transaction(transactions: list[Transaction]):
    """
    Редактирует существующую запись о доходе или расходе.

    :param transactions: Список объектов Transaction
    """
    index = int(input("Введите индекс записи для редактирования: "))
    if 0 <= index < len(transactions):
        transaction = transactions[index]
        print(f"Текущие данные: {transaction.date}, {transaction.category}, {transaction.amount}, {transaction.description}")
        transaction.date = input("Введите новую дату (ГГГГ-ММ-ДД): ") or transaction.date
        transaction.category = input("Введите новую категорию (Доход/Расход): ") or transaction.category
        transaction.amount = float(input("Введите новую сумму: ") or transaction.amount)
        transaction.description = input("Введите новое описание: ") or transaction.description
        print("Запись успешно отредактирована!")
    else:
        print("Неверный индекс записи.")


def delete_transaction(transactions: list[Transaction]):
    """
    Удаляет существующую запись о доходе или расходе.

    :param transactions: Список объектов Transaction
    """
    index = int(input("Введите индекс записи для удаления: "))
    if 0 <= index < len(transactions):
        transaction = transactions.pop(index)
        print(f"Запись '{transaction.date}, {transaction.category}, {transaction.amount}, {transaction.description}' успешно удалена.")
    else:
        print("Неверный индекс записи.")


def view_transactions(transactions: list[Transaction]):
    """
    Выводит все существующие записи о доходах и расходах.

    :param transactions: Список объектов Transaction
    """
    if transactions:
        print("Все записи:")
        for i, transaction in enumerate(transactions):
            print(f"{i}. {transaction.date}, {transaction.category}, {transaction.amount}, {transaction.description}")
    else:
        print("Нет записей.")


def search_transactions(transactions: list[Transaction]):
    """
    Осуществляет поиск записей по категории, дате или сумме.

    :param transactions: Список объектов Transaction
    """
    criteria = input("Введите критерий поиска (категория, дата или сумма): ")
    found = []
    for t in transactions:
        if criteria.lower() in str(t.category).lower() or \
           criteria.lower() in str(t.date) or \
           criteria.lower() in str(t.amount):
            found.append(t)
    if found:
        print("Найденные записи:")
        for t in found:
            print(f"{t.date}, {t.category}, {t.amount}, {t.description}")
    else:
        print("Записи не найдены.")


def main():
    """
    Главная функция приложения, реализующая консольный интерфейс.
    """
    filename = "transactions.txt"
    transactions = load_transactions(filename)

    while True:
        print("\nЛичный финансовый кошелек")
        print("1. Показать баланс")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Просмотреть все записи")
        print("6. Поиск по записям")
        print("7. Выход")

        choice = input("Введите номер операции: ")

        if choice == "1":
            show_balance(transactions)
        elif choice == "2":
            add_transaction(transactions)
            save_transactions(transactions, filename)
        elif choice == "3":
            edit_transaction(transactions)
            save_transactions(transactions, filename)
        elif choice == "4":
            delete_transaction(transactions)
            save_transactions(transactions, filename)
        elif choice == "5":
            view_transactions(transactions)
        elif choice == "6":
            search_transactions(transactions)
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()