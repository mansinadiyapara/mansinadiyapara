from Repository.LoadSaveData import load_data, save_data
from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent.parent
BONUS_FILE = BASE_DIR / "Repository" / "department_bonus.json"

class DepartmentRule:

    def calculate_bonus(self):

        employees = load_data()

        bonus_results = self.load_bonus_results()

        for emp_id, emp_details in employees.items():

            name = emp_details["name"]
            department = emp_details["department"]
            salary = emp_details["salary"]

            if department == "IT":
                bonus = salary * 0.10       # Discount=30%
            elif department == "HR":
                bonus = salary * 0.30       # Discount=30%
            elif department == "Finance":
                bonus = salary * 0.30       # Discount=30%
            elif department == "Marketing":
                bonus = salary * 0.20       # Discount=20%
            elif department == "Sales":
                bonus = salary * 0.20       # Discount=20%
            else:
                bonus = 0

            new_bonus = {
                "employee_id": emp_id,
                "name": name,
                "bonus": bonus
            }

            # Update existing employee
            for index, existing_bonus in enumerate(bonus_results):

                if existing_bonus["employee_id"] == emp_id:
                    bonus_results[index] = new_bonus
                    break

            # Add new employee
            else:
                bonus_results.append(new_bonus)

        self.save_bonus_results(bonus_results)
        print("Bonus Saved Successfully...")


    def save_bonus_results(self,bonus_results):

        with open(BONUS_FILE, "w") as file:
            json.dump(bonus_results, file, indent=4)

    def load_bonus_results(self):

        if not BONUS_FILE.exists():
            return []

        with open(BONUS_FILE, "r") as file:
            return json.load(file)
