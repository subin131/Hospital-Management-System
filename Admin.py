#Admin Class
from Doctor import Doctor
class Admin:
    def __init__(self, username, password,address):
        self.username = username
        self.password = password
        self.address = address
        
    #view method
    def view(self,a_list):
        for i in a_list:
            print(i)
            
    #login mwthod
    def login(self):
        #A method that deals with the Admin login, check if theusername and password match the registered ones.
        print("------Admin Login------")
        uname=input("Enter the username: ")
        password=input("Enter the password: ")
        if self.username == uname and self.password == password:
            return True
       
    #find_index method
    def find_index(self,index,doctors):
        #check if a dcoctor id exists
        if index in range(len(doctors)):
            return True
        else:
            return False
        
    #get_doctor_details method
    def get_doctor_details(self):
        first_name=input("Enter the first name of the doctor: ")
        surname=input("Enter the surname of the doctor: ")
        speciality=input("Enter the speciality of the doctor: ")
        
        return first_name,surname,speciality
    
    #doctor_management method
    def doctor_management(self,doctors):
        
        print("------Doctor Management------")
        print("Choose the operation: \n1. Register \n2. View \n3. Update  \n4. Delete")
        option=int(input("Enter the option: "))
        
        #Register
        if(option==1):
            print("------Register------")
            print("Enter the doctor's details: ")
            first_name= input("Enter the first name of the doctor: ")
            surname=input("Enter the surname of the doctor: ")
            speciality=input("Enter the speciality of the doctor: ")
            doctors.append(Doctor(first_name,surname,speciality))
            print("Doctor registered successfully")
            
        #view
        elif option==2:
            print("------Lists of Doctors------")
            self.view(doctors)
            
            
        #update
        elif option==3:
            print("------Update Doctor's Details------")
            self.view(doctors)
            index=int(input("Enter the index of the doctor: "))
            if self.find_index(index,doctors):
                #to update the details of the doctor
                # doctors[index]=Doctor(*self.get_doctor_details())
                #check to update first name or surname or speciality
                choice=int(input("Choose the field to update: \n1. First Name \n2. Surname \n3. Speciality"))
                if choice==1:
                    doctors[index].set_first_name(input("Enter the new first name: "))
                    
                    
                elif choice==2:
                    doctors[index].set_surname(input("Enter the new surname: "))
                    
                elif choice==3:
                    doctors[index].set_speciality(input("Enter the new speciality: "))
                print("Doctor updated successfully")
            else:
                print("Doctor not found")
                
        #delete
        elif option==4:
            print("------Delete Doctor------")
            index=int(input("Enter the index of the doctor: "))
            if self.find_index(index,doctors):
                doctors.pop(index)
                print("Doctor deleted successfully")
            else:
                print("Doctor not found")
            
        else:
            print("Invalid option")
    
    #view_patient method
    def view_patient(self,patients):
        print("------Lists of Patients------")
        self.view(patients)
        
        
    #assign_doctor_to_patient method
    def assign_doctor_to_patient(self,patients,doctors):
        print("------Lists of Patients------")
        self.view(patients)
        print("------Assign Doctor to Patient------")
        index=int(input("Enter the index of the patient: "))
        if self.find_index(index,patients):
            print("------Lists of Doctors------")
            self.view(doctors)
            index2=int(input("Enter the index of the doctor: "))
            if self.find_index(index2,doctors):
                doctors[index2].add_patient(patients[index])
                print("Doctor assigned to patient successfully")
            else:
                print("Doctor not found")
        else:
            print("Patient not found")
            
            
    #discharge method
    def discharge(self,patients,discharged_patients):
        print("------Lists of Patients------")
        self.view(patients)
        while True:
            choice=input("Do you want to discharge a patient? (y/n): ")
            if choice=="y":
                print("------Discharge Patient------")
                index=int(input("Enter the index of the patient: "))
                if self.find_index(index,patients):
                    discharged_patients.append(patients[index])
                    patients.pop(index)
                    print("Patient discharged successfully")
                else:
                    print("Patient not found")
            
            elif choice=="n":
                break
        
        
    #view_discharged method
    def view_discharge(self,discharge_patients):
        print("------Discharged Patients------")
        self.view(discharge_patients)
        
    
    #update_details
    def update_details(self):
        #allows the admin to update their details
        self.__username=input("Enter the new username: ")
        self.__password=input("Enter the new password: ")
        self.__address=input("Enter the new address: ")
        
        return self.__username,self.__password,self.__address
        
            
    
        
            
       
        
    