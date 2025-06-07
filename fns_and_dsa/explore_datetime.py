from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"The date after {days} days will be: {formatted_future}")

def main():
    # Display current date and time
    display_current_datetime()

    # Ask user for number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
