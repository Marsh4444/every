import random   # Used to generate random patient ID numbers

class Patient:
    """A simple nursing tracking system to manage patient records and vitals."""

    def __init__(self, name, age, gender):
        """
        Constructor method:
        This runs automatically whenever a new patient object is created.

        Attributes:
        - name: The patient's name.
        - age: The patient's age.
        - gender: The patient's gender.
        - patient_id: A unique ID number generated for each patient.
        - vitals: A dictionary to store health data like temperature, blood pressure, and pulse.
        """
        self.patient_id = self.generate_ID()      # Automatically generate patient ID
        self.name = name.title()                  # Format name to title case (e.g., "melo" → "Melo")
        self.age = age
        self.gender = gender.capitalize()         # Format gender (e.g., "female" → "Female")
        self.vitals = {}                          # Empty dictionary for vitals until recorded

        # Confirm creation
        print(f"✅ New Patient Registered!\nID Number: {self.patient_id}\n")

    def generate_ID(self):
        """
        Generates a unique 5-digit patient ID using random numbers.
        Example output: 'PAT-34825'
        """
        return f"PAT-{''.join(str(random.randint(0, 9)) for _ in range(5))}"

    def print_info(self):
        """
        Displays all patient information in a readable format.
        Includes both personal details and vitals.
        """
        # If vitals are recorded, print them nicely. If not, show a message.
        vitals_info = (
            "\n".join(f"  - {key}: {value}" for key, value in self.vitals.items())
            if self.vitals else "No vitals recorded yet."
        )

        # Return a formatted summary of patient data
        return (
            f"\n🧾 Patient Information\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Patient ID: {self.patient_id}\n"
            f"Vitals:\n{vitals_info}"
        )

    def update_info(self):
        """
        Allows the nurse or user to update the patient's basic information.
        If the input is left blank, the old value is kept.
        """
        print("\n🔄 Update Patient Information:")
        self.name = input("Enter new name (leave blank to skip): ") or self.name
        self.age = input("Enter new age (leave blank to skip): ") or self.age
        self.gender = input("Enter new gender (leave blank to skip): ") or self.gender
        print("✅ Patient information updated successfully.\n")

    def patience_vitals(self):
        """
        Collects and records patient vitals interactively.
        Stores the data inside the 'vitals' dictionary.
        """
        print(f"\nRecording vitals for {self.name}:")
        info_1 = input("Enter Temperature (°C): ")
        info_2 = input("Enter Blood Pressure (e.g., 120/80): ")
        info_3 = input("Enter Pulse (bpm): ")

        # Store the collected information as key-value pairs
        self.vitals = {
            "Temperature": info_1,
            "Blood Pressure": info_2,
            "Pulse": info_3
        }

        print(f"✅ Vitals recorded successfully for {self.name}.\n")


# 🧪 Example usage below (for testing the class)
# Create a new patient record
p1 = Patient('meso', 17, 'female')

# Record patient vitals
p1.patience_vitals()

# Display full patient information
print(p1.print_info())
