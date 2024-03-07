from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Prepare data structure to store birthdays for each day of the week
    birthdays_per_week = defaultdict(list)
    
    # Get the current date
    today = datetime.today().date()
    
    # Adjust current date to the start of the next week (Monday)
    monday_of_next_week = today + timedelta(days=(7 - today.weekday()))
    
    # Iterate through each user
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Calculate birthday for this year
        birthday_this_year = birthday.replace(year=today.year)
        
        # If birthday has passed this year, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Calculate the difference between birthday and current date
        delta_days = (birthday_this_year - today).days
        
        # Determine the day of the week for the birthday
        birthday_weekday = birthday_this_year.weekday()
        
        # If birthday falls on a weekend, move it to Monday
        if birthday_weekday >= 5:
            birthday_weekday = 0  # Monday
        
        # Check if the birthday is within the next week starting from Monday
        if delta_days < 7 + today.weekday():
            # Store the user's name under the appropriate day of the week
            birthday_weekday_name = (monday_of_next_week + timedelta(days=birthday_weekday)).strftime("%A")
            birthdays_per_week[birthday_weekday_name].append(name)
    
    # Display the result
    for day, birthdays in birthdays_per_week.items():
        print(f"{day}: {', '.join(birthdays)}")

# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 12)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 15)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
]

get_birthdays_per_week(users)
