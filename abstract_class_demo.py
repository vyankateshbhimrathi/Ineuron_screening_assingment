# from abc module importing method ABC class
from abc import abstractmethod, ABC


# creating abstract class as insurance inheriting ABC class
class insurance(ABC):

    # creating abstract method as premium which non concrete method which is not implemented
    @abstractmethod
    def premium(self):
        pass

    # creating normal method and implemention is there hence called as concrete method.
    def insurance_renew(self):
        return "after you existing insurance period completes you can renew your insurance."

# creating LIC class which is inherited by insurance i.e,  abstract class
class LIC(insurance):

    # creating abstract method implementation in subclass
    def premium(self):
        return "Premium for the insurance is Rs.5000 annually."

    # creating independant method for LIC class
    def insurance_period(self):
        return "you can opt for insurance more than 1 year."

# creating TataAIA class which is inherited by LIC class i.e, multilevel inheritance
class TataAIA(LIC):

    # creating abstract method implementation in subclass
    def premium(self):
        return "insurance for TataAIA is quite high as compared to peers i.e, Rs.7000 annually."

    # creating independant method for TataAIA class
    def family_plan(self):
        return "you can opt for family plan as per your requirement"

# creating object of LIC class
company = LIC()
# calling different functions of abstract as well as subclass of abstract clas
company.insurance_renew()
company.premium()
company.insurance_period()
# creating object of TataAIA class
tata = TataAIA()
tata.insurance_period()