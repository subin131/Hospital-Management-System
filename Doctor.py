#Doctor class
from Person import Person
class Doctor(Person):
    """A class that deals with the Doctor operations"""
    def __init__(self,first_name,surname,speciality):
        """

        Args:
            first_name (string):First Name
            surname (string): Surname
            speciality (string): Doctor Speciality
        """
        Person.__init__(self,first_name,surname)
        self.__speciality=speciality
        self.__patients=[]
        self.__appointments=[]
        
    #def full_name is Inherited from Person class
    
    #get first name
    def get_first_name(self):
        return(self.__first_name)
    
    #set first name
    def set_first_name(self,new_first_name):
        self.__first_name=new_first_name
        return "Updated Successfully"
        
    #get surname
    def get_surname(self):
        return(self.__surname)
    
    
    #set surname
    def set_surname(self,new_surname):
        self.__surname=new_surname
        return "Updated Successfully"
    
    #get speciality
    def get_speciality(self):
        return(self.__speciality)
    
    #set speciality
    def set_speciality(self,new_speciality):
        self.__speciality=new_speciality
        return "Updated Successfully"
        
    #add patient
    def add_patient(self,patient):
        """
        Args:
            patient (string): The full name of Patient
        """
        self.__patients.append(patient)
        
    #__str__
    def __str__(self):
        return f'{self.full_name():^30}|{self.__speciality:^15}'
        
