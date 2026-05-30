import math

def check_attendance(attended, total, target_percent=75.0):
    
    current_percent = (attended / total) * 100
    requirements_met = current_percent >= target_percent
    classes_to_attend = 0
    
    if not requirements_met:
        
        numerator = (target_percent * total) - (100 * attended)
        denominator = 100 - target_percent
        classes_to_attend = math.ceil(numerator / denominator)
        
    return current_percent, requirements_met, classes_to_attend

classes_attended = 42
total_classes_held = 60
required_target = 75.0

current, status, short_by = check_attendance(classes_attended, total_classes_held, required_target)

print(f"--- Attendance Tracker ---")
print(f"Current Attendance: {current:.2f}%")
print(f"Target Required:    {required_target}%")
print(f"Status Requirement: {'MET' if status else 'SHORT'}")

if not status:
    print(f"Action Needed:You must attend the next {short_by} classes consecutively.")