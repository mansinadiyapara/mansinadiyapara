import sqlite3
from .employee_repository import EmployeeRepository


class DatabaseEmployeeRepository(EmployeeRepository):

    def __init__(self, database_name="employees.db"):
        self.database_name = database_name
        self.create_table()

    def create_table(self):

        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
        """)

        connection.commit()
        connection.close()

    def get_all(self):

        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, name, email, department, salary
            FROM employees
        """)

        rows = cursor.fetchall()

        connection.close()

        employees = []

        for row in rows:
            employees.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "department": row[3],
                "salary": row[4]
            })

        return employees
        
    def add(self, employee):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO employees
            (id, name, email, department, salary)
            VALUES (?, ?, ?, ?, ?)
        """, (
            employee["id"],
            employee["name"],
            employee["email"],
            employee["department"],
            employee["salary"]
        ))

        connection.commit()
        connection.close()

    def update(self, employee):

        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE employees
            SET name = ?,
                email = ?,
                department = ?,
                salary = ?
            WHERE id = ?
        """, (
            employee["name"],
            employee["email"],
            employee["department"],
            employee["salary"],
            employee["id"]
        ))

        connection.commit()
        connection.close()

    def delete(self, employee_id):

        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,)
        )

        connection.commit()
        connection.close()