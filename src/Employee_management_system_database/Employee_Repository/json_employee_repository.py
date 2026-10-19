import json
import os
from .employee_repository import EmployeeRepository


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "employee_data.json")


class JsonEmployeeRepository(EmployeeRepository):

    def load_data(self):
        if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
            with open(FILE_NAME, 'r') as f:
                try:
                    return json.load(f)
                except FileNotFoundError:
                    return {}
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_data(self, data):
        with open(FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        data = self.load_data()
        return list(data.values())

    def add(self, employee):
        employees = self.load_data()

        employees[str(employee["id"])] = employee

        self.save_data(employees)

    def update(self, employee):

        employees = self.load_data()

        employees[str(employee["id"])] = employee

        self.save_data(employees)

    def delete(self, employee_id):

        employees = self.load_data()

        if str(employee_id) in employees:
            del employees[str(employee_id)]

        self.save_data(employees)

