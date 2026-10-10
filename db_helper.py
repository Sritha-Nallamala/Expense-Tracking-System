from idlelib import query

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logging
logger = setup_logging("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses
        for expense in expenses:
            print(expense)


def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense: {expense_date}, {amount}, {category}, {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary: {start_date}, {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category,sum(amount) as total
            FROM expense_manager.expenses
            where expense_date between %s and %s group by category;''',
            (start_date, end_date)
        )
        data=cursor.fetchall()
        return data
def fetch_expense_by_month():
    query= """SELECT
    MONTH(expense_date) AS month_number,
    MONTHNAME(expense_date) AS month_name,
    SUM(amount) AS total_expenses
FROM expense_manager.expenses
GROUP BY MONTH(expense_date), MONTHNAME(expense_date)
ORDER BY MONTH(expense_date) ASC;
    """
    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses



if __name__ == "__main__":
    # exp = fetch_expenses_for_date("2024-08-01")
    # print(exp)
    # summary = fetch_expense_summary("2024-08-01","2024-08-05")
    # for record in summary:
    #     print(record)
    print(fetch_expense_by_month())
