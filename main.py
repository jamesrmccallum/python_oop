

class Employee:

    """
    Base employee class
    """

    def __init__(self, firstname: str, lastname: str, pay: int, dept: str):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.dept = dept

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
