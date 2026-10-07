import rules
from rule_engine import RuleEngine


class Main:

    def run(self):

        print("===== Rule Engine =====")

        salary = int(input("Enter Salary:- "))
        age = int(input("Enter Age:- "))

        employee = {
            "salary": salary,
            "age": age
        }

        rules_list = [
            rules.SalaryRule(),
            rules.EmployeeEligible(),
            rules.DiscountRule(),
            rules.AccessRule(),
            rules.ApprovalRule()
        ]

        engine = RuleEngine(rules_list)

        results = engine.evaluate(employee)

        print("\nRule Results:")

        for result in results:
            print(
                f"Rule: {result['rule']} | "
                f"Result: {result['result']}"
            )


main = Main()
main.run()

