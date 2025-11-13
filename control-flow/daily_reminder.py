task = input("Enter the task for your daily reminder: ")
priority = input("Enter the priority level (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        message = f"Reminder: {task} - This is a high priority task."
           
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."

    case "low":
        message = f"Reminder: '{task}' is a low priority task."
    case _:
        message = f"Reminder: '{task}' has an unspecified priority level."

if time_bound == "yes":
    message += " that requires immediate attention!"

else:
    message += ". Consider completing it when you have free time."

print(message)