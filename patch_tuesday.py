#!/usr/bin/env python3
"""Simple script to calculate Microsofts Patch Tuesday (2nd Tuesday of the month)

Usage: 

    python3 patch_tuesday.py <YEAR> <MONTH>

Args:
    year: The year in a numberic format: e.g. 2022, 2023
    month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.

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
import sys
import calendar

def patch_tuesday(year, month):
    """Calculate the Microsoft Patch tuesday for a given month or year

    Args:
        month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.
        year: The year in a numberic format: e.g. 2022, 2023
    """
    # Defined dictionary for the offset days for Patch Tuesdays
    tuesday_offset = { 'Monday':9,
                      'Tuesday':8,
                      'Wednesday':14,
                      'Thursday':13,
                      'Friday':12,
                      'Saturday':11,
                      'Sunday':10 }

    # Calculate First Day of the Month
    # calendar.weekday returns the numeric value based on the integer inputs of year, month, day
    # calendar.day_name returns the day name based on a number input: 0 = Monday, 1 = Tuesday, etc.
    first_day = calendar.day_name[calendar.weekday(int(year),int(month),1)]

    # Concatenate to details for date.
    patch_tuesday_date = str(tuesday_offset[first_day])+"/"+str(month)+"/"+str(year)

    # Store just the Patch Tuesday offset value
    patch_tuesday_offset = tuesday_offset[first_day]

    dict_patch_tuesday = { 'patch_tuesday':patch_tuesday_offset,
                           'patch_tuesday_date':patch_tuesday_date }

    return dict_patch_tuesday

def print_output(input_year, input_month, dates):
    """Format and print output to screen.

    Args:
        input_year: The user input month
        input_month: The user input month
        dates: The Dates values returned from patch_tuesday function

    """
    print("Patch Tuesday for", calendar.month_name[int(input_month)],
          "-",int(input_year), " = ", dates['patch_tuesday_date'])


# Main program:
def main():
    """Print the day and date of patch Tuesday

    Args:
        year: The year in a numberic format: e.g. 2022, 2023
        month: The Month in a numeric format: e.g. 1 = Jan, 2 Feb etc.
    """

    #Input year and month
    input_year = input("Please input year: ")
    #Ensure a valid month is input ()
    while True:
        input_month = input("Please input month: ")
        if int(input_month) in range(1,13): # Ranged 1-13 to include 12 as a valid month
            break
        print("Invalid Month, please try again")
        continue

    # Execute the patch_tuesday function and pass all details to the print_output function
    print_output(input_year, input_month, patch_tuesday(input_year, input_month))


if __name__ == '__main__':
    if len(sys.argv) == 3: # Executes when user provides two arguments at execution
        arg_year = int(sys.argv[1])
        arg_month = int(sys.argv[2])
        if arg_month in range(1, 13): # Validate month is correct
            print_output(arg_year, arg_month, patch_tuesday(arg_year, arg_month))
        else:
            raise SystemExit(
                f"Invalid month:{sys.argv[2]}\nThis should be between 1 and 12.\nPlease Try again."
                )
    elif len(sys.argv) == 2: # Executes when only one argument is provided
        arg_year = int(sys.argv[1])
        print(f"User input only a year, outputting all Patch tuesdays for year: {arg_year}")
        for range_month in range(1,13): # Validate month is correct
            print_output(arg_year, range_month, patch_tuesday(arg_year, range_month))
    elif len(sys.argv) == 1: # Executes main function when no arguments provided
        main()
    else: # If more than two arguments are provided raise as an error.
        raise SystemExit(f"Usage: {sys.argv[0]} <year> <month>")
