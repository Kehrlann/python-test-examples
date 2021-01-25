from examples.company import Company, Employee
from datetime import date


def test_seniority():
    # Arrange
    alice = Employee("Alice", date(2021, 1, 1))
    bob = Employee("Bob", date(2019, 9, 5))
    carol = Employee("Carol", date(2019, 3, 2))
    company = Company(alice, bob, carol)

    # Act
    most_senior = company.get_most_senior_employee()

    # Assert
    assert most_senior == carol


def test_seniority_when_no_employee():
    # Arrange
    company = Company()

    # Act
    most_senior = company.get_most_senior_employee()

    # Assert
    assert most_senior is None
