from abc import ABC, abstractmethod


class EmployeeRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, employee):
        pass

    @abstractmethod
    def update(self, employee):
        pass

    @abstractmethod
    def delete(self, employee_id):
        pass