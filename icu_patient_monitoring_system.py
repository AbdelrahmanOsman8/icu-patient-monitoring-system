# Initial State: Patients in ICU with vital signs
icu_patients = [
    {"Name": "Ali", "Oxygen": 95, "Heart_Rate": 80},   # Normal
    {"Name": "Sara", "Oxygen": 88, "Heart_Rate": 105}, # Low O2 + High HR → Emergency
    {"Name": "Mona", "Oxygen": 92, "Heart_Rate": 95}   # Slightly low O2
]

# Safety Rules Function
def check_vitals(patient):
    """Check ICU patient vital signs for emergency"""
    # Rule 1: Low Oxygen → Warning
    if patient["Oxygen"] < 90:
        return False, f"Emergency! {patient['Name']}'s oxygen level is critically low ({patient['Oxygen']}%)"
    
    # Rule 2: High Heart Rate → Warning
    if patient["Heart_Rate"] > 100:
        return False, f"Alert! {patient['Name']}'s heart rate is high ({patient['Heart_Rate']} bpm)"
    
    # Rule 3: Combination of Low O2 + High HR → Emergency
    if patient["Oxygen"] < 90 and patient["Heart_Rate"] > 100:
        return False, f"Critical Emergency! {patient['Name']} has Low O2 + High Heart Rate!"
    
    return True, f"{patient['Name']}'s vitals are stable ✅"

# Function to monitor all patients
def monitor_icu(patients):
    for patient in patients:
        safe, message = check_vitals(patient)
        if safe:
            print(message)
        else:
            print(message)  # Emergency / Alert message

# Example Usage
monitor_icu(icu_patients)
