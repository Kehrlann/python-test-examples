from datetime import date
from typing import Sequence


class Employee:
    def __init__(self, name: str, start_date: date) -> None:
        self.name = name
        self.start_date = start_date


class Company:
    def __init__(self, *args: Sequence[Employee]) -> None:
        self.employees: Sequence[Employee] = args

    def get_most_senior_employee(self) -> Employee:
        sorted_employees = sorted(self.employees, key=lambda e: e.start_date)
        return sorted_employees[0] if sorted_employees else None
