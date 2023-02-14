#the main parent class
class Person:
    
    def __init__(self,first_name,surname):
        """

        Args:
            first_name (string):First Name
            surname (string): Surname
        """
        self.__first_name=first_name
        self.__surname=surname
        
    #to return the full name
    def full_name(self):
        return(self.__first_name + " " +self.__surname)
        
        
# obj=Person("Ram","Satyal")
# print(obj.full_name())