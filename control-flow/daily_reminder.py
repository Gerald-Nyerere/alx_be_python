task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f" High priority task: '{task}'."
    case "medium":
        reminder = f" Medium priority task: '{task}'."
    case "low":
        reminder = f" Low priority task: '{task}'."
    case _:
        reminder = f" Unknown priority for task: '{task}'."

if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"


print("\nReminder:")
print(reminder)
