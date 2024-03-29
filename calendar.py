def get_first_day_year() -> int:
    """Prompt the user to input the first day of the year and return it as an integer."""
    given_day = -1
    while 6 < given_day or given_day < 0:
        given_day = int(input("Enter the first day of the year, (ex. Sunday = 0, Monday = 1, Tuesday = 2, etc.): "))
    return given_day


def month_name(month_int: int) -> str:
    """Return the name of the month corresponding to the given integer."""
    return {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
            9: "September", 10: "October", 11: "November", 12: "December"}.get(month_int)


def days_in_month(month_int: int, year_int: int) -> int:
    """Return the number of days in the given month and year, accounting for leap years."""
    if month_int in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month_int in (4, 6, 9, 11):
        return 30
    if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
        return 29
    return 28


def day_abbreviation(weekday: int) -> str:
    """Return the abbreviation for the given day of the week."""
    return {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}.get(weekday)


def print_month(year: int, month: int, weekday: int) -> None:
    """Print the calendar for the given month and year, starting on the specified weekday."""
    print(f'{month_name(month)} - {year}'.center(33))
    print("-" * 33)
    print('Sun  Mon  Tue  Wed  Thu  Fri  Sat')
    print("     " * weekday, end='')
    num_days = days_in_month(month, year)
    for i in range(1, num_days + 1):
        print(f'{str(i).rjust(3)}  ', end='')
        if (i + weekday) % 7 == 0:
            print()
    print()
    print()


if __name__ == "__main__":
    # Prompt the user for a year and print the calendar for that year.
    cal_year = int(input("Enter a year for calendar: "))
    first_day = get_first_day_year()
    print(f'===Calendar for {cal_year}===')
    for month_num in range(1, 13):
        print_month(cal_year, month_num, first_day)
        first_day = (first_day + days_in_month(month_num, cal_year)) % 7
