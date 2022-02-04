# Simple script to calculate Patch Tuesday

# Inputs: Year [Format: YY or YYYY], Month [Format: MM or Month abbrieviation Jan, Feb, etc. or Full Month March, July, etc.)
# Outputs: date of Microsoft Patch Tuesday [Format: DD/MM/YYYY]

''' 
Depending on the day of the 1st of the month there is an offset:
Wed = +13days
Thu = +12days
Fri = +11days
Sat = +10days
Sun = +9days
Mon = +8days
Tue = +7days

'''

# python3 library module calendar - https://docs.python.org/3/library/calendar.html

def patch_tuesday(input_month, input_year):

    import calendar
    from datetime import date

    # Defined dictionary for the offset days for Patch Tuesdays
    tuesday_offset = {'Monday':9, 'Tuesday':8, 'Wednesday':14, 'Thursday':13, 'Friday':12, 'Saturday':11, 'Sunday':10}

    # Input year and month
    #input_year = input("Please input year: ")
    #input_month = input("Please input month: ")

    # Calculate First Day of the Month
    # calendar.weekday returns the numeric value based on the integer inputs of year, month, day
    # calendar.day_name returns the name of the day based on a numeric input: 0 = Monday, 1 = Tuesday, etc.
    first_day = calendar.day_name[calendar.weekday(int(input_year),int(input_month),1)]

    # Concatenate to details for date.
    patch_tuesday = str(tuesday_offset[first_day])+"/"+input_month+"/"+input_year
    
    # print out the details.
    print("Patch Tuesday for ", calendar.month_name[int(input_month)], "-",input_year, " = ", patch_tuesday)

    return patch_tuesday