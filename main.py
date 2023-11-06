from datetime import date, datetime


def get_birthdays_per_week(users):
    if not users:
        return {}   
    
    current_date = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Initialize a dictionary to hold names of users for each weekday
    birthday_week = {day: [] for day in weekdays}

    for user in users:
        # Set the user's birthday year to the current year
        user_birthday = user['birthday'].replace(year=current_date.year)
        # Calculate the difference in days between today and the user's birthday
        day_difference = (user_birthday - current_date).days
        # Get the name of the weekday for the user's birthday
        target_day = (user_birthday).strftime('%A')  

        # Check if the birthday is within the next 7 days
        if 0 <= day_difference < 7:
            if target_day in ['Saturday', 'Sunday'] and current_date.weekday() == 0:
                target_day = None
            elif target_day in ['Saturday', 'Sunday'] and current_date.weekday() > 0:
                birthday_week['Monday'].append(user['name'])                
            else:
                birthday_week[target_day].append(user['name'])    
        # Process birthdays within specific date ranges         
        elif 364 <= day_difference <= 366 and current_date.weekday() == 0:
            birthday_week['Monday'].append(user['name'])
        elif -365 <= day_difference <= -357 and current_date.weekday() > 0:
            user_birthday = user['birthday'].replace(year=current_date.year+1)
            target_day = (user_birthday).strftime('%A')
            if target_day in ['Saturday', 'Sunday']:
                birthday_week['Monday'].append(user['name'])
            elif user_birthday.weekday() < current_date.weekday():
                birthday_week[target_day].append(user['name'])
            else:
                target_day =None            
        elif -2 <= day_difference <= -1 and current_date.weekday() == 0:
            birthday_week['Monday'].append(user['name'])
        elif -2 <= day_difference <= -1 and current_date.weekday() > 0:
            continue

     # Remove weekdays with no birthdays
    birthday_week = {key: value for key, value in birthday_week.items() if value}
    users = birthday_week

    #-----------------------------------
    # Реалізуйте тут домашнє завдання
    return users

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")