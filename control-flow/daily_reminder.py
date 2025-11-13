Task = input("Enter the task for your daily reminder: ")
Priority = input("Enter the priority level (high, medium, low): ")
Time_Bound = input("Is it time-bound? (yes/no): ").strip().lower()

match Priority:
    case "high":
        message = f"Reminder: {task} - This is a high priority task."
           
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."

    case "low":
        message = f"Reminder: '{task}' is a low priority task."
    case _:
        message = f"Reminder: '{task}' has an unspecified priority level."

if Time_Bound == "yes":
    message += " that requires immediate attention!"

else:
    message += ". Consider completing it when you have free time."

print(message)