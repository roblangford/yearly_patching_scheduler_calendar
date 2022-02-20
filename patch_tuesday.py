#!/usr/bin/env python3
"""Simple script to calculate Microsofts Patch Tuesday (2nd Tuesday of the month)

Usage: 

    python3 patch_tuesday.py <MONTH> <YEAR>

Args:
    month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.
    year: The year in a numberic format: e.g. 2022, 2023


Depending on the day of the 1st of the month there is an offset:
Wed = +13days
Thu = +12days
Fri = +11days
Sat = +10days
Sun = +9days
Mon = +8days
Tue = +7days
"""
# Future enhancements: 
# python3 library module calendar - https://docs.python.org/3/library/calendar.html

# Libraries:
import calendar
from datetime import date


def patch_tuesday(month, year):
    """Calculate the Microsoft Patch tuesday for a given month or year

    Args:
        month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.
        year: The year in a numberic format: e.g. 2022, 2023
    """
    # Defined dictionary for the offset days for Patch Tuesdays
    tuesday_offset = {'Monday':9, 'Tuesday':8, 'Wednesday':14, 'Thursday':13, 'Friday':12, 'Saturday':11, 'Sunday':10}

    # Calculate First Day of the Month
    # calendar.weekday returns the numeric value based on the integer inputs of year, month, day
    # calendar.day_name returns the name of the day based on a numeric input: 0 = Monday, 1 = Tuesday, etc.
    first_day = calendar.day_name[calendar.weekday(int(year),int(month),1)]

    # Concatenate to details for date.
    patch_tuesday_date = str(tuesday_offset[first_day])+"/"+str(month)+"/"+str(year)

    # Store just the Patch Tuesday date
    patch_tuesday = tuesday_offset[first_day]

    dict_patch_tuesday = {'patch_tuesday':patch_tuesday,'patch_tuesday_date':patch_tuesday_date}

    return dict_patch_tuesday


# Main program:
def main():
    """Print the day and date of patch Tuesday

    Args:
        month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.
        year: The year in a numberic format: e.g. 2022, 2023
    """

    #Input year and month
    input_year = input("Please input year: ")
    input_month = input("Please input month: ")

    dates = patch_tuesday(input_month,input_year)

    # print out the details.
    print("Patch Tuesday for ", calendar.month_name[int(input_month)], "-",int(input_year), " = ", dates['patch_tuesday_date'])


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <month> <year>")
    main()
