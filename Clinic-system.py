Morning_appointments = []
Afternoon_appointments = []
current_id = 1

# Appointment class
class Appointment:
    def __init__(self, id, patient, time, doctor):
        self.id = id
        self.patient = patient
        self.time = time
        self.doctor = doctor


# Add appointment
def add_appointment():
    global current_id

    patient = input("Enter the name of the patient: ")
    time_str = input("Enter the appointment time (HH or HH:MM): ")
    doctor = input("Enter the name of the doctor: ")

    # Extract hour from time
    try:
        hour = int(time_str.split(":")[0])
    except ValueError:
        print("Invalid time format.")
        return

    # Create an appointment object
    appt = Appointment(current_id, patient, time_str, doctor)

    # Morning vs Afternoon
    if hour >= 12:
        Afternoon_appointments.append(appt)
        print("Assigned to Afternoon appointments.")
    else:
        Morning_appointments.append(appt)
        print("Assigned to Morning appointments.")

    print(f"Appointment added with ID: {current_id}")
    current_id += 1



# Delete appointment by ID
def delete_appointment(list_name):
    dlt_id = int(input("Enter the ID to delete: "))

    for i in range(len(list_name)):
        if list_name[i].id == dlt_id:
            del list_name[i]
            print("Appointment deleted.")
            return

    print("Appointment ID not found.")



# Search appointment by ID
def search_appointment(list_name):
    search_id = int(input("Enter the ID to search: "))

    for appt in list_name:
        if appt.id == search_id:
            print(f"Found: ID={appt.id}, Patient={appt.patient}, Time={appt.time}, Doctor={appt.doctor}")
            return

    print("Appointment ID not found.")



# Display appointments
def display_appointments(list_name, label):
    print(f"\n{label} Appointments:")
    
    if not list_name:
        print("No appointments scheduled.")
        return
    
    for appt in list_name:
        print(f"ID: {appt.id}, Patient: {appt.patient}, Time: {appt.time}, Doctor: {appt.doctor}")



# Main menu
def main():
    while True:
        print("\nClinic Appointment System")
        print("1. Add Appointment")
        print("2. Delete Appointment (Morning)")
        print("3. Delete Appointment (Afternoon)")
        print("4. Search Appointment (Morning)")
        print("5. Search Appointment (Afternoon)")
        print("6. Display Morning Appointments")
        print("7. Display Afternoon Appointments")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_appointment()
        elif choice == '2':
            delete_appointment(Morning_appointments)
        elif choice == '3':
            delete_appointment(Afternoon_appointments)
        elif choice == '4':
            search_appointment(Morning_appointments)
        elif choice == '5':
            search_appointment(Afternoon_appointments)
        elif choice == '6':
            display_appointments(Morning_appointments, "Morning")
        elif choice == '7':
            display_appointments(Afternoon_appointments, "Afternoon")
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")



# Program execution
if __name__ == "__main__":
    main()
