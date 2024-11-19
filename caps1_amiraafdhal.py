"""
CRUD (create-read-update-delete) Program

User : admin klinik gigi
Objectives: membuat jadwal klinik
"""

#import libraries
import datetime as dt
from tabulate import tabulate
import sys

# patient data list
patient_data_list = [
{
        'patient_id': 123,
        'full_name' : 'Rina Wijaya',
        'dob': '1974-10-09',
        'age': 50
    },
    {
        'patient_id': 124,
        'full_name' : 'Budi Santoso',
        'dob': '1996-12-25',
        'age': 27
    },
    {
        'patient_id': 125,
        'full_name' : 'Siti Rahmawati',
        'dob': '1999-02-14',
        'age': 25
    },
    {
        'patient_id': 126,
        'full_name' : 'Dewi Kartika',
        'dob': '1985-07-01',
        'age': 39
    },
    {
        'patient_id': 127,
        'full_name': 'Andi Pratama',
        'dob': '1990-05-12',
        'age': 34
    },
    {
        'patient_id': 128,
        'full_name': 'Farida Suharto',
        'dob': '1988-03-20',
        'age': 36
    },
    {
        'patient_id': 129,
        'full_name': 'Yusuf Nugraha',
        'dob': '1993-11-03',
        'age': 31
    },
    {
        'patient_id': 130,
        'full_name': 'Maya Sari',
        'dob': '2000-08-15',
        'age': 24
    }
]

# available procedures list
procedures_list = [
{
    'procedure' : 'Teeth Cleaning',
    'doctor' : 'Drg. Saraswati',
    'available_time' : [dt.time(9, 0), dt.time(10, 0), dt.time(10, 30), dt.time(11, 0),]
},
{
    'procedure' : 'Vaccination',
    'doctor' : 'Dr. William',
    'available_time' : [dt.time(9, 30), dt.time(10, 0), dt.time(10, 30), dt.time(11, 0),]
},
{   'procedure' : 'Tooth Extraction',
    'doctor' : 'Drg. Tina',
    'available_time' : [dt.time(9, 0), dt.time(9, 30), dt.time(10, 30), dt.time(11, 0),]
},
{
    'procedure': 'Root Canal',
    'doctor': 'Drg. Hendra',
    'available_time': [dt.time(12, 0), dt.time(13, 0), dt.time(13, 30)]
},
{
    'procedure': 'Dental Filling',
    'doctor': 'Drg. Yuna',
    'available_time': [dt.time(14, 0), dt.time(15, 0), dt.time(15, 30)]
},
{
    'procedure': 'Braces Consultation',
    'doctor': 'Drg. Amina',
    'available_time': [dt.time(16, 0), dt.time(17, 0), dt.time(17, 30)]
}
]

# existing appointments list
appointments_list = [
    {
        'appt_id' : 1,
        'procedure' : 'Teeth Cleaning',
        'appt_time': dt.time(11, 30),
        'patient_id': 123,
        'full_name' : 'Rina Wijaya',
        'age': 50,
        'doctor' : 'Drg. Saraswati'
    },
    {
        'appt_id' : 2,
        'procedure' : 'Tooth Extraction',
        'appt_time': dt.time(12, 0),
        'patient_id': 124,
        'full_name' : 'Budi Santoso',
        'age': 27,
        'doctor' : 'Drg. Tina'
    },
        {
        'appt_id': 3,
        'procedure': 'Vaccination',
        'appt_time': dt.time(9, 0),
        'patient_id': 125,
        'full_name': 'Siti Rahmawati',
        'age': 25,
        'doctor': 'Dr. William'
    },
    {
        'appt_id': 4,
        'procedure': 'Root Canal',
        'appt_time': dt.time(12, 30),
        'patient_id': 126,
        'full_name': 'Dewi Kartika',
        'age': 39,
        'doctor': 'Drg. Hendra'
    },
    {
        'appt_id': 5,
        'procedure': 'Dental Filling',
        'appt_time': dt.time(14, 30),
        'patient_id': 127,
        'full_name': 'Andi Pratama',
        'age': 34,
        'doctor': 'Drg. Yuna'
    },
    {
        'appt_id': 6,
        'procedure': 'Braces Consultation',
        'appt_time': dt.time(16, 30),
        'patient_id': 128,
        'full_name': 'Farida Suharto',
        'age': 36,
        'doctor': 'Drg. Amina'
    },
    {
        'appt_id': 7,
        'procedure': 'Teeth Cleaning',
        'appt_time': dt.time(9, 30),
        'patient_id': 129,
        'full_name': 'Yusuf Nugraha',
        'age': 31,
        'doctor': 'Drg. Saraswati'
    },
    {
        'appt_id': 8,
        'procedure': 'Tooth Extraction',
        'appt_time': dt.time(10, 0),
        'patient_id': 130,
        'full_name': 'Maya Sari',
        'age': 24,
        'doctor': 'Drg. Tina'
    }
]

# ----------SUPPLEMENTARY FUNCTIONS---------------
# supplementary function - count age
def countAge(dob):
    born = dt.date.fromisoformat(dob)
    today = dt.date.today()
    return today.year - born.year - ((today.month, today.day) <= (born.month, born.day))

#validation function
def validate(statement):
    status = False
    while True:
        print(statement)
        answer = input('Yes (y) / No (n) :').capitalize()

        if answer == 'Y':
            status = True
            return status
        
        elif answer == 'N':
            status = False
            return status
        
        else:
            print('Please input a valid answer!')

def getPatientIndex():
    while True:
        try:
            p_id = int(input('Insert Patient ID :'))

            patient = None
            for i in patient_data_list:
                if i['patient_id'] == p_id:
                    patient = i
                    break

            patient_index = patient_data_list.index(patient)
            return patient_index
        
        except ValueError:
            print('Please Input a valid patient ID')

def getApptIndex():
    while True:
        try:
            appt_id = int(input('Insert Appointment ID :'))

            appt = None
            for i in appointments_list:
                if i['appt_id'] == appt_id:
                    appt = i
                    break

            appt_index = appointments_list.index(appt)
            return appt_index
        
        except ValueError:
            print('Please Input a valid appointment ID')

def searchPatientData():
    search_input = input('Search Patient Name : ')

    search_results = []
    for i in patient_data_list:
        if search_input.lower() in i['full_name'].lower():
            search_results.append(i)
    
    if len(search_results) == 0:
        print('No results match your search.')

    else:
          headers = [ 'Patient_ID',
                'Patient_Name',
                'Date_of_Birth'
                'Age'
                ]
          patient_list_aslist = [[a['patient_id'], a['full_name'], a['dob'], a['age']] for a in search_results]

          return print(tabulate(patient_list_aslist, headers=headers, tablefmt="mixed_grid"))


def searchDoctor():
    search_input = input('Search Doctor Name : ')

    search_results = []
    for i in appointments_list:
        if search_input.lower() in i['doctor'].lower():
            search_results.append(i)
    
    if len(search_results) == 0:
        print('No results match your search.')

    else:
        headers = ['Appt_ID',
                'Procedure',
                'Appointment_Time',
                'Patient_ID',
                'Patient_Name',
                'Age',
                'Doctor']
        appointments_list_aslist = [[a['appt_id'], a['procedure'], a['appt_time'], a['patient_id'],
                                 a['full_name'], a['age'], a['doctor']] for a in search_results]
        
        return print(tabulate(appointments_list_aslist, headers=headers, tablefmt="mixed_grid"))

def filterAppointmentBy(key, value):
    filterlist = []

    for i in appointments_list:
        if i[key] == value:
            filterlist.append(i)

        headers = ['Appt_ID',
                'Procedure',
                'Appointment_Time',
                'Patient_ID',
                'Patient_Name',
                'Age',
                'Doctor']
    
    appointments_list_aslist = [[a['appt_id'], a['procedure'], a['appt_time'], a['patient_id'],
                                a['full_name'], a['age'], a['doctor']] for a in filterlist]
    
    return print(tabulate(appointments_list_aslist, headers=headers, tablefmt="mixed_grid"))

def previewPatient(patient):
    headers = [ 'Patient_ID',
                'Patient_Name',
                'Date_of_Birth',
                'Age'
                ]

    patient_list_aslist = [patient.values()]

    return print(tabulate(patient_list_aslist, headers=headers, tablefmt="mixed_grid"))

def previewAppointment(appt):
    headers = ['Appt_ID',
                'Procedure',
                'Appointment_Time',
                'Patient_ID',
                'Patient_Name',
                'Age',
                'Doctor']
    
    appointments_aslist = [appt.values()]

    return print(tabulate(appointments_aslist, headers=headers, tablefmt="mixed_grid"))

# -----------CREATE Functions----------------
# CREATE -- Add new patient
def add_name(new_patient):
    while True:
        name = input("Please input the full name of the patient: ").strip().title()
        alphabet_only = all(a.isalpha() for a in name.split())

        if alphabet_only == True :
            new_patient['full_name'] = name
            break
            
        else:
            print('Please input the patient full name with alphabetical characters and spaces only.')

def add_dob(new_patient):
    while True:
        try:
            new_dob = input("Please input the date of birth of the patient in the format YYYY-MM-DD : ")
            born = dt.date.fromisoformat(new_dob)

            # check_dob_duplicate = True
            # for i in patient_data_list:
            #     if i['dob'] == new_dob:
            #         check_dob_duplicate = False
            
            # if (add_name == True) and (check_dob_duplicate == True):
            new_patient['dob'] = new_dob
            break

        except ValueError:
            print('Please Input date in a valid format.')

def add_new_patient():
    new_patient =  {
        'patient_id': '',
        'full_name' : '',
        'dob': '',
        'age': ''
    }
    global lastPatientID

    # add new patient id based on the last created patient ID
    lastPatientID += 1
    new_patient['patient_id'] = lastPatientID

    # input full name
    add_name(new_patient)

    # input date of birth
    add_dob(new_patient)

    # calculate age using function
    new_patient['age'] = countAge(new_patient['dob'])

    # check for any duplicates in patient data
    check_duplicate = False
    for i in patient_data_list:
        if (i['full_name'] == new_patient['full_name']) and (i['dob'] == new_patient['dob']):
            check_duplicate = True
            break
    
    if check_duplicate == True:
        print('----------The patient data you tried to add already exists, no new patient was registered.----------')
        patient_data_menu()
        
    else:
        previewPatient(new_patient)
        add_patient = "Do you want to save this patient's data?"
        ans = validate(add_patient) # validate save patient data

        if ans == True:
            patient_data_list.append(new_patient)
            print('---------- New Patient Successfully Registered ----------')
            patient_data_menu()


        else:
            print('---------- Registration cancelled, no new patient was registered.----------')
            patient_data_menu()

# CREATE -- add new appointment from exiisting patient
def choose_procedure(appt):
    while True:
        try:
            for i in range(len(procedures_list)):
                print(f"{i} ----- {procedures_list[i]['procedure']}")
            procedure_code = int(input('Which Procedure would you like to register? : '))

            appt['procedure'] = procedures_list[procedure_code]['procedure']
            selected_procedure = procedures_list[procedure_code]

            return selected_procedure
        
        
        # except:
        #     print('Please input a valid procedure code!')
        except Exception as e:
            print("Terjadi error:", e)

def choose_appt_time(selected_procedure, appt):
    while True:
        try:
            for k in range(len(selected_procedure['available_time'])):
                print(f"{k} --- {selected_procedure['available_time'][k]}")
            choose_time = int(input('Select from available times : '))

            appt['appt_time'] = selected_procedure['available_time'][choose_time]
            break

        except ValueError:
            print('Please Input a valid available time option.')

        except IndexError:
            print('Please Input a valid available time option.')

# add appointment with existing patient
def new_appt(patient):
    appt = {
        'appt_id' : '',
        'procedure' : '',
        'appt_time': '',
        'patient_id': patient['patient_id'],
        'full_name' : patient['full_name'],
        'age': patient['age'],
        'doctor' : ''
    }

    global lastApptID

    # generating new appointment id
    lastApptID += 1
    appt['appt_id'] = lastApptID

    # choose procedure
    selected_procedure = choose_procedure(appt)

    # choose available appointment time
    choose_appt_time(selected_procedure, appt)

    # add doctor information
    appt['doctor'] = selected_procedure['doctor']

    return appt

#add appointment after create menu
def add_new_appt():
    while True:
        try:
            patient_index = getPatientIndex()

            view_patients(patient_index)

            message = "Do you want to create an appointment for this patient?"
            ans = validate(message)

            if ans == True:
                added = new_appt(patient_data_list[patient_index]) # user inputs new appointment data (unsaved)

                for i in appointments_list: # check if there is duplicate appointment for this patient
                    if (added['full_name'] == i['full_name']) and (added['appt_time'] == i['appt_time']):
                        print('----------This Patient already has an appointment at this time, no appointment was created.----------')
                        break
                    else: # there are no duplicate appointments
                        previewAppointment(added)
                        add_this = 'Do you want to create this appointment?'
                        ans = validate(add_this) # validate to save appointment
                        if ans == True:
                            appointments_list.append(added)
                            print('-------------------- New Appointment Successfully Created -------------------------')
                            break

                        else:
                            print('-------------------- No changes were made.--------------------')
                            break
                break
            else:
                print('-------------------- No changes were made.--------------------')
                break

        # except:
            # print('-------------------- Patient ID does not exist --------------------')
        except Exception as e:
            print("Terjadi error:", e)

# -----------READ Functions-------------------
def view_available_times(procedure):
    procedure_name = procedure['procedure']
    doctor = procedure['doctor']

    print(f'''
Procedure Name : {procedure_name}
Doctor : {doctor}
''')
    available_time = procedure['available_time']

    display_table = [[i.strftime("%I:%M %p")] for i in available_time]

    print(tabulate(display_table, headers=["Time Slots"], tablefmt='mixed_grid'))

def view_patients(index=None):
    """
    args: 
        index (int) : index for appointments_list to get specific patient, default = None

    returns: 
        prints table of all existing patients, or specific based on index
    """

    headers = [ 'Patient_ID',
                'Patient_Name',
                'Date_of_Birth',
                'Age'
                ]
    
    if index is None:
        patient_list_aslist = [[a['patient_id'], a['full_name'], a['dob'], a['age']] for a in patient_data_list]
    else:
        patient_list_aslist = [patient_data_list[index].values()]

    return print(tabulate(patient_list_aslist, headers=headers, tablefmt="mixed_grid"))

def view_appointments(index=None):
    """
    args: 
        index (int) : index for appointments_list to get specific appointment, default = None

    returns: 
        prints table of all existing appointments, or specific based on index
    """

    headers = ['Appt_ID',
                'Procedure',
                'Appointment_Time',
                'Patient_ID',
                'Patient_Name',
                'Age',
                'Doctor']
    
    if index is None:
        appointments_list_aslist = [[a['appt_id'], a['procedure'], a['appt_time'], a['patient_id'],
                                 a['full_name'], a['age'], a['doctor']] for a in appointments_list]
    else:
        appointments_list_aslist = [appointments_list[index].values()]

    return print(tabulate(appointments_list_aslist, headers=headers, tablefmt="mixed_grid"))

def view_procedures(doctor=None):
    """
    args:
        doctor (str) name of doctor for which the available procedures are viewed
    returns:
        prints list of available procedure times based on doctor and procedure name
    """

    if doctor == None:
        for i in procedures_list:
            view_available_times(i)

    else:
        pro = None
        for k in procedures_list:
            if k['doctor'] == doctor:
                pro = k
                break

        view_available_times(pro)

# ------- UPDATE Functions ------------
def edit_appointment_time():
    while True:
        try:
            appt_index = getApptIndex()
            view_appointments(appt_index)
            appt = appointments_list[appt_index]

            message = 'Do you want to edit this appointment?'
            ans = validate(message)
            if ans == True:
                procedure = None
                for a in procedures_list:
                    if a['procedure'] == appt['procedure']:
                        procedure = a
                        break

                for i in range(len(procedure['available_time'])):
                    print(f"{i} ----- {procedure['available_time'][i]}")

                while True: 
                    try:
                        select_time = int(input('Input the available time you want to select :'))
                        if select_time < len(procedure['available_time']):
                            val = f'Do you want to change the appointment time to {procedure['available_time'][select_time]}?'
                            ans = validate(val)
                            
                            if ans == True:
                                print('----------Appointment Time Successfully Changed----------')
                                procedure['available_time'].append(appt['appt_time'])
                                appt['appt_time'] = procedure['available_time'][select_time]
                                previewAppointment(appt)
                                del procedure['available_time'][select_time]

                                break

                        else:
                            print('Invalid input, Please enter a valid input!')
                        

                    except ValueError:
                        print('Invalid input')
                break # GANTI CALL MAIN MENU

            else:
                print('No appointments were edited.')
                break

        except ValueError:
            print(f"Appointment ID not found")
            break

def change_dob(patient, patient_index):
    while True:
        try:
            new_dob = input("Please input the date of birth of the patient in the format YYYY-MM-DD : ")
            born = dt.date.fromisoformat(new_dob)

            message = f'Do you want to change the date of birth to {new_dob}?'
            ans = validate(message)
            if ans == True:
                print('''-------------------- Data successfully updated --------------------''')
                patient['dob'] = new_dob
                view_patients(patient_index)
                
                patient_data_menu()

            else:
                print('No patient data has been edited.')

        except ValueError:
            print('Please Input date in a valid format.')

def change_name(patient, patient_index):
    while True:
        new_name = input("Please input the full name of the patient: ").strip().title()
        alphabet_only = all(a.isalpha() for a in new_name.split())

        if alphabet_only == True:
            message = f"Would you like to change this patient's name to {new_name}?"
            ans = validate(message)
            if ans == True:
                print('''-------------------- Data successfully updated --------------------''')
                patient['full_name'] = new_name
                view_patients(patient_index)
                
                patient_data_menu()

            else:
                print('No patient data has been edited.')
        else:
            print('Please input the patient full name with alphabetical characters and spaces only.')

def choose_patient_column(patient, patient_index):
    while True:
        column = input('''
                    1 ---- Patient Name
                    2 ---- Date of Birth
                    Enter the column you want to edit : 
                ''')

        if column == '1':
                change_name(patient, patient_index)
        elif column == '2':
                change_dob(patient, patient_index)
        else:
            print('Invalid Input! Please input a valid input.')


def edit_patient_data():
    while True:
        try:
            # ask for patient ID to get patient data
            patient_index = getPatientIndex()
            patient = patient_data_list[patient_index]

            view_patients(patient_index) # display the selected patient's data
            message = "Do you want to edit this patient's data?"
            ans = validate(message) # validate if its the right patient
            if ans == True:
                choose_patient_column(patient, patient_index) # choose which data to be edited
                
            else:
                print('No patient data was edited.')
                break
        
        except Exception as e:
            print("Terjadi error:", e)
        # except:
        #     print(f"Patient ID not found")
        #     break




# ------- DELETE Functions ------------
# delete appointment
def delete_appointment():
    while True:
        try:

            appt_index = getApptIndex()

            view_appointments(appt_index)
            message = 'Do you want to delete this appointment?'
            ans = validate(message)
            if ans == True:
                print('---------------- Appointment successfully deleted ----------------')
                del appointments_list[appt_index]

                appointments_menu()

            else:
                print('---------------- No appointments were deleted.----------------')
                break

        except ValueError:
            print("Appointment ID not found")
            break

# delete patient data
def delete_patient():
    while True:
        try:
  
            patient_index = getPatientIndex()

            view_patients(patient_index)

            message = "Do you want to delete this patient's data?"
            ans = validate(message)
            if ans == True:
                print('Patient data successfully deleted')
                del patient_data_list[patient_index]
                patient_data_menu()

            else:
                print('---------------- No patient data was deleted.----------------')
                break

        except ValueError:
            print(f"Patient ID not found")
            break

# -------- MENU Functions -----------------

## -------- PATIENT MENU FUNCTIONS -----------
def view_patient_menu():
     while True:
        print('''
=========== View Patient Data Menu ===========
1 -------- View All Patient Data
2 -------- View Patient Data based on Patient ID
3 -------- Search Patient by Name
4 -------- Back to Patient Data Menu
''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                view_patients()
                break

            elif choice == 2:
                 
                 patient_ids = [i['patient_id'] for i in patient_data_list]
                 print('Existing patient IDs:')
                 print(patient_ids)

                 while True:
                    try:
                        patient_index = getPatientIndex()
                        view_patients(patient_index)
                        break


                    except IndexError:
                        print('Invalid input, please input a valid index.')
            
            elif choice == 3:
                searchPatientData()

            elif choice == 4:
                patient_data_menu()
            
            else:
                print("Invalid Input, please enter a valid menu choice.")

        # except:
        #     print("Invalid Input, please enter a valid menu choice.")
        except Exception as e:
            print("Terjadi error:", e)


def patient_data_menu():
     while True:
        print('''
=========== Patient Data Menu ===========
1 -------- View Patient Data
2 -------- Register New Patient
3 -------- Edit Patient Data
4 -------- Delete Patient Data
5 -------- Back to Main Admin Menu
''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                view_patient_menu()

            elif choice == 2:
                add_new_patient()
            
            elif choice == 3:
                view_patients()

                print('To Edit Patient Data based on Patient ID,')
                edit_patient_data()

            elif choice == 4:
                view_patients()

                print('To Delete Patient Data based on Patient ID,')
                delete_patient()

            elif choice == 5:
                main_admin_menu()
                sys.exit()

        except ValueError:
            print("Invalid Input, please enter a valid menu choice.")

# -------- APPOINTMENT MENU FUNCTIONS ---------
def create_appt_menu():
    while True:
        print('''
=========== Create New Appointment Menu ===========
*** To create an appointment, please make sure the patient has already been registered ***
1 -------- Create New Appointment
2 -------- View Patient Data List
3 -------- Back to Appointments Menu
              
''')
        
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                view_patients()

                print('To create new appointment with a registered patient,')
                add_new_appt()

            elif choice == 2:
                view_patient_menu()
            
            elif choice == 3:
                appointments_menu()

        except ValueError:
            print("Invalid Input, please enter a valid menu choice.")


def view_appointment_menu():
    while True:
        print('''
=========== View Appointments Menu ===========
1 -------- View All Appointments
2 -------- View Appointment Based on Appointment ID
3 -------- Back to Appointments Menu
''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                view_appointments()
                break

            elif choice == 2:
                appt_ids = [i['appt_id'] for i in appointments_list]
                print('Existing appointment IDs:')
                print(appt_ids)

                print('To View Appointment,')
                appt_index = getApptIndex()
                view_appointments(appt_index)

            
            elif choice == 3:
                appointments_menu()

            else:
                print("Invalid Input, please enter a valid menu choice.")

        # except:
        #     print("Invalid Input, please enter a valid menu choice.")
        except Exception as e:
            print("Terjadi error:", e)


def appointments_menu():
    while True:
        print('''
=========== Appointments Menu ===========
1 -------- View Appointments
2 -------- Create New Appointment
3 -------- Edit Existing Appointment Time
4 -------- Delete Appointment
5 -------- Back to Main Admin Menu
              
''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                view_appointment_menu()

            elif choice == 2:
                create_appt_menu()
                
            
            elif choice == 3:
                view_appointments()

                print('To Change the Appointment Time of an Existing Appointment,')
                edit_appointment_time()

            elif choice == 4:
                view_appointments()

                print('To Delete Existing Appointment,')
                delete_appointment()
            
            elif choice == 5:
                main_admin_menu()

            else:
                print("Invalid Input, please enter a valid menu choice.")

        except ValueError:
            print("Invalid Input, please enter a valid menu choice.")


#---------DOCTOR VIEW FUNCTIONS-------------

# def doctor_main_menu()

#-------- MAIN MENUS -----------------

def main_admin_menu():
    while True:
        print('''
=========== Admin Main Menu ===========
1 -------- Appointments Menu
2 -------- Patient Data Menu
3 -------- Back to Views Menu
''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                appointments_menu()

            elif choice == 2:
                patient_data_menu()
            
            elif choice == 3:
                views_menu()

            else:
                print("Invalid Input, please enter a valid menu choice.")

        except ValueError:
            print("Invalid Input, please enter a valid menu choice.")


def views_menu():
    while True:
        print('''
=========== Views Menu ===========
1 -------- Admin View
2 -------- Exit Program
    
        ''')
        try:
            choice = int(input("Please input the number for the choice of menu: "))
            
            if choice == 1:
                main_admin_menu()

            elif choice == 2:
                print('Thank You for using the program.')
                sys.exit()
                
  
            else:
                print("Invalid Input, please enter a valid menu choice.")
        
        
        except ValueError:
            print("Invalid Input, please enter a valid menu choice.")
            

lastApptID = appointments_list[-1]['appt_id']
lastPatientID = patient_data_list[-1]['patient_id']

views_menu()

