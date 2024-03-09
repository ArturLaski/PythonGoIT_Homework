from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    # Adjust current date to the start of the next week (Monday)
    monday_of_next_week = today + timedelta(days=(7 - today.weekday()))
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        birthday_weekday = birthday_this_year.weekday()
        if birthday_weekday >= 5:
            birthday_weekday = 0  # Monday
        if delta_days < 7 : #If we want to take first monday from today we need to add this line before ":"===>   +today.weekday() 
            birthday_weekday_name = (monday_of_next_week + timedelta(days=birthday_weekday)).strftime("%A")
            birthdays_per_week[birthday_weekday_name].append(name)
    # Display the result
    for day, birthdays in birthdays_per_week.items():
        print(f"{day}: {', '.join(birthdays)}")

# Example usage:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 12)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 3, 17)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
]
get_birthdays_per_week(users)
