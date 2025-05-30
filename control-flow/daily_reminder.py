task = input("Enter task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound (yes/no): ")

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
         reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
         reminder = f"Reminder: '{task}' is a LOW priority task."
    case "_":
        reminder = f"Reminder: '{task}' is a UNKNOWN priority task."
if time_bound == "yes":
    reminder += " This task requires immediate attention!"
print(reminder)