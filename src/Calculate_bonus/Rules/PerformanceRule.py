from Repository.LoadSaveData import load_data, save_data
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
BONUS_FILE = BASE_DIR / "Repository" / "performance_bonus.json"

class PerformanceRule:
    
    def calculate_bonus(self):
        employees = load_data()

        bonus_results = self.load_bonus_results()

        for emp_id, emp_details in employees.items():

            name = emp_details["name"]
            performance = emp_details["performance"]
            salary = emp_details["salary"]

            if performance == "1/5 Rating":
                bonus = salary * 0.10       # Discount=10%
            elif performance == "2/5 Rating":
                bonus = salary * 0.20       # Discount=20%
            elif performance == "3/5 Rating":
                bonus = salary * 0.30       # Discount=30%
            elif performance == "4/5 Rating":
                bonus = salary * 0.40       # Discount=40%
            elif performance == "5/5 Rating":
                bonus = salary * 0.50       # Discount=50%
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