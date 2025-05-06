"""
Develop a class ‘Hospital’ that has attributes of name and address. Develop two child classes of
‘Doctor’ (name, address and specialization) and ‘Patient’ (name, address and disease). Implement a
class ‘medical_test’. Display the name of doctor, name of patient and medical test information when a
medical test is done.
"""
class Hospital:
    def __init__(self, name, address, doctor, patient):
        self.h_name = name
        self.h_address = address
        self.doctor = doctor
        self.patient = patient
    
    def show_info(self):
        print("Hospital name:", self.h_name)
        print("Hospital address:", self.h_address)

class Doctor:
    def __init__(self, name, address, specialization):
        self.name = name
        self.address = address
        self.specialization = specialization

class Patient:
    def __init__(self, name, address, disease):
        self.name = name
        self.address = address
        self.disease = disease

class MedicalTest:
    def __init__(self, d_name, d_address, d_specialization, p_name, p_address, p_disease, date):
        self.doctor = Doctor(d_name, d_address, d_specialization)
        self.patient = Patient(p_name, p_address, p_disease)
        self.test_date = date
        self.display_info()
    
    def display_info(self):
        print("Medical Test Information:")
        print(f">>> Doctor: {self.doctor.name}")
        print(f">>> Patient: {self.patient.name}")
        print(f">>> Test date: {self.test_date}")