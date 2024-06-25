from datetime import datetime
from functions import get_day_of_week, is_leap_year, calculate_age
from electronic_display import display_date

def main():
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))
    
    birth_date = datetime(year, month, day)

    day_of_week = get_day_of_week(birth_date)
    print(f"Вы родились в {day_of_week}.")


    leap_year = is_leap_year(year)
    if leap_year:
        print(f"{year} год был високосным.")
    else:
        print(f"{year} год не был високосным.")


    age = calculate_age(birth_date)
    print(f"Вам сейчас {age} лет.")


    display_date(day, month, year)

if __name__ == "__main__":
    main()