import pytest
from models.employee import Employee, Technician

# pylint: disable=C0111


@pytest.fixture
def employee():
    return Employee('test', 'employee', 35000, 'Marketing')


@pytest.fixture
def technician():
    return Technician('John', 'Technician', 20000, 'Maintenance', 4)


def test_employee_name_is_correct(employee: Employee):
    assert employee.fullname() == 'test employee'


def test_employee_name_is_none(employee: Employee):
    assert employee.fullname() is not None


def test_technician_has_grade(technician: Technician):
    assert 'grade' in technician.__dict__
