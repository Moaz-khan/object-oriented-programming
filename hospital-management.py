# HOSPITAL MANAGEMENT SYSTEM


class Hospital:
    def __init__(self,name,location,timings):
        self.name = name
        self.location = location
        self.timings = timings
        self.doctors = []
        self.patients = []
            
    
    def add_doctor(self,doctor,specialization,doctor_timings,date):
        self.doctor = doctor
        self.specialization = specialization
        self.doctor_timmings = doctor_timings
        self.date = date
        self.doctors.append(doctor + " - " + specialization + " - " + self.doctor_timmings + " - " + self.date)

    def add_patient(self,patient):
        self.patient = patient
        self.patients.append(patient)

  
        

 
# Creating a hospital object        
Hospital_name = Hospital("Apollo Hospital","New York","Monday To Friday")
print(f"Welcome to {Hospital_name.name}")
print(f"Location: {Hospital_name.location}")
print(f"Timings: {Hospital_name.timings}")

# Adding doctors to the hospital
# Doctor name, specialization and timings
Doctor_name = ["Dr. John", "Dr. Smith", "Dr. Emily", "Dr. Michael", "Dr. Sarah"]
Specialization = ["Cardiologist", "Neurologist", "Pediatrician", "Orthopedic", "Dermatologist"]
Doctor_timings = ["Monday 9:00 AM To 5:00 PM", "Tuesday 10:00 AM To 6:00 PM", "Wednesday 11:00 AM To 7:00 PM", "Thursday 12:00 PM To 8:00 PM", "Friday 1:00 PM To 9:00 PM"]
Appointment_date = ["2025-05-11", "2025-05-12", "2025-05-13", "2025-05-14", "2025-05-15"]
# Adding doctors to the hospital
for i in range(len(Doctor_name)):
    Hospital_name.add_doctor(Doctor_name[i],Specialization[i],Doctor_timings[i],Appointment_date[i])
print("Doctors Available:")
for doctor in Hospital_name.doctors:
    print(doctor)   

# Adding patients to the hospital
Patient_name = ["Alice", "Bob", "Charlie", "David", "Eva"]
for i in range(len(Patient_name)):
    Hospital_name.add_patient(Patient_name[i])
print("Patients Available:")
for patient in Hospital_name.patients:
    print(patient)

# Appointing a doctor to a patient
def appoint_doctor():
  print("This Week appointments:")
  for i in range(len(Doctor_name)):
      print(f"Patient {Patient_name[i]} is appointed to {Doctor_name[i]},{Specialization[i]} on {Appointment_date[i]}, {Doctor_timings[i]}")   
    
appoint_doctor()  
        


   
    







        
