#sub class of Person
from Person import Person
class Patient(Person):
    
    def __init__(self,first_name,surname,age,mobile,postcode):
        """_summary_

        Args:
            first_name(string):FirstName
            surname(string):Surname
            age (int): Age
            mobile (string): Mobile Number
            postcoe (string): Address
        """
        #parent class Person
        Person.__init__(self,first_name,surname)
        self.__age=age
        self.__mobile=mobile
        self.__postcode=postcode
        self.__doctor="None"
        
    #def full_name is Inherited from Person class
        
    #get_doctor method
    def get_doctor(self):
        return (self.__doctor)
    
    #link method
    def link(self,doctor):
        """
        Args:
            doctor (string): The full name of Doctor
        """
        self.__doctor=doctor
        
    #print_symptoms method
    def print_symptoms(self):
        """Printing all the symptoms"""
        pass
    
    #get all the string representational of object
    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    
