patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
age = input("Enter age: ")
gender = input("Enter gender: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
address = input("Enter address: ")
blood_group = input("Enter blood group: ")
disease = input("Enter disease/complaint: ")
date = input("Enter date of registration: ")

print("\n--- Patient Details ---")
print("Patient ID :", patient_id)
print("Name       :", name)
print("Age        :", age)
print("Gender     :", gender)
print("Phone      :", phone)
print("Email      :", email)
print("Address    :", address)
print("Blood Group:", blood_group)
print("Complaint  :", disease)
print("Date       :", date)

with open("patients.txt", "a") as f:
    f.write(
        f"{patient_id}, {name}, {age}, {gender}, {phone}, "
        f"{email}, {address}, {blood_group}, {disease}, {date}\n"
    )

print("\nPatient details saved successfully!")
