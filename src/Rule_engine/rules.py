from abc import ABC, abstractmethod


class Rule(ABC):

    @abstractmethod
    def evaluate(self, input_data):
        pass


class SalaryRule(Rule):

    def evaluate(self, employee):
        salary = employee["salary"]

        if salary <= 10000:
            return "Fail"
        else:
            return "Pass"


class EmployeeEligible(Rule):

    def evaluate(self, employee):
        age = employee["age"]

        if age <= 25:
            return "Fail"
        else:
            return "Pass"


class DiscountRule(Rule):

    def evaluate(self, employee):
        salary = employee["salary"]

        if salary >= 50000:
            return "20% Discount"
        elif salary >= 30000:
            return "10% Discount"
        else:
            return "No Discount"


class AccessRule(Rule):

    def evaluate(self, employee):
        age = employee["age"]

        if age >= 18:
            return "Access Granted"
        else:
            return "Access Denied"


class ApprovalRule(Rule):

    def evaluate(self, employee):
        salary = employee["salary"]

        if salary >= 30000:
            return "Approved"
        else:
            return "Rejected"