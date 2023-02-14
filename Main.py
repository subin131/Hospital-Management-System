#main function
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    The main function to be ran when the program runs
    
    """
    #initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'),
Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'),
Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15,
'07123456789','C1 ABC')]
    discharged_patients = []
    
    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
           running = True # allow the program to run
           break
        else:
            print('Incorrect username or password.')
    
    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Quit')
        
        # get the option
        op = input('Option: ')
        if op == '1':
            #call the doctor_management method
            admin.doctor_management(doctors)
            
        elif op == '2':
            #call the discharge method 
            admin.discharge(patients,discharged_patients)
            
        elif op == '3':
            #call view_discharged method
            admin.view_discharge(discharged_patients)
            
        elif op == '4':
            #call the assign_to_doctor method
            admin.assign_doctor_to_patient(patients,doctors)
            
        elif op == '5':
            #call the update_admin method
            admin = admin.update_details()
            
        elif op == '6':
            #terminate the program
            running = False
            
        else:
            print('Invalid option.')
            
            
# run the main function
if __name__ == '__main__':
    main()