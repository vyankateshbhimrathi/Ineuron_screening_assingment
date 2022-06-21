
# creating graduation class as parent class
class graduation():

    # initializing constructor
    def __init__(self, college, highedu):
        self.college = college
        self.highedu = highedu


# creating job class as parent class
class job():

    def __init__(self, role, salary, company):
        self.role = role
        # salary is a protected variable
        self._salary = salary
        self.company = company

    def income_tax(self):
        """
        This function is used for a person is eligible to pay income tax or not.
        """
        if self._salary > 500000:
            return f"you will have to pay tax as per your tax slab"
        else:
            return f"your income is less than 500000 annually."


# creating child class which is inherited by both graduation and job class hence which becomes multiple inheritance.
class basic_details(graduation, job):

    # creating number of arguments
    def __init__(self, name, surname, mail, college, highedu, role, salary, company):
        self.name = name
        self.surname = surname
        # mail attribute is a protected one
        self.__mail = mail
        # initializing init of parent classed that is not to override init of parent class
        graduation.__init__(self, college, highedu)
        job.__init__(self, role, salary, company)

    def graduation(self):
        """
        This function provides basic details of graduation like college, highedu etc.
        """
        return f"{self.name} graduated from {self.college} college with higher education in {self.highedu}."

    def working_company(self):
        """
        This function provides company details along with profile details
        """
        return f"{self.name} is working in {self.company} as {self.role}."


# creating object/instance of basic_details class which is subclass of graduation and job class
info = basic_details('Mahesh', 'Patil', 'MaheshP@gmail.com', 'WIT''BSC', 'data analyst', 600000, 'Genpact')
# calling graduation method from child class
info.graduation()
# calling income_tax method from job class
info.income_tax()
# calling working_company from basic_details class
info.working_company()
# calling protected variable with class name
info._basic_details__mail
