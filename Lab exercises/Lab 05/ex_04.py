"""
Develop a class ‘Hospital’ that has attributes of name and address. Develop two child classes of
‘Doctor’ (name, address and specialization) and ‘Patient’ (name, address and disease). Implement a
class ‘medical_test’. Display the name of doctor, name of patient and medical test information when a
medical test is done.
"""

class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Doctor(Hospital):
    def __init__(self, name, address, specialization):
        Hospital.__init__(self, name, address)
        self.specialization = specialization

class Patient(Hospital):
    def __init__(self, name, address, disease):
        Hospital.__init__(self, name, address)
        self.disease = disease

class MedicalTest():
    def __init__(self, doctor, patient):
        print(f"Doctor: {doctor.name}, Patient: {patient.name}, Test: {patient.disease}")

d = Doctor("Dr. John", "123 Main St", "Cardiologist")
p = Patient("Jane Doe", "456 Elm St", "Heart Disease")

m = MedicalTest(d, p)
