"""
    Module incorporating basic employee types
"""


class Employee:

    """
    Base employee class
    """

    def __init__(self, firstname: str, lastname: str, pay: int, dept: str):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.dept = dept

    def fullname(self)->str:
        """
        Prints an employees name in 'firstname lastname' format

        :return: The employee name in 'firstname lastname' format

        :rtype: str
        """

        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self, percentage: float):
        """Applies a given percentage increase to the salary

        :param percentage: The amount to increase salary by

        """
        self.pay = self.pay * (1 + percentage)


class Technician(Employee):
    """
    A special subclass of employee, has a grade
    """

    def __init__(self, grade, *args, **kwargs):

        self.grade = grade
        super().__init__(*args, **kwargs)

    # @property
    # def grade(self)->int:
    #     """Get employee grade"""
    #     return self.grade

    # @grade.setter
    # def grade(self, grade):
    #     self.grade = grade
