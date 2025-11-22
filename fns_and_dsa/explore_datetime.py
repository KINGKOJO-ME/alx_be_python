from datetime import datetime, timedelta

def display_current_datetime():

    current_date =datetime.now()

    formatted_current = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print (F"Current date and time: {formatted_current}")

display_current_datetime()

def calculate_future_date():
   #current_date = datetime.now()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

calculate_future_date() 


