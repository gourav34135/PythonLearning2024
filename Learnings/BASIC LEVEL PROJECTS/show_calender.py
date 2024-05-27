import calendar

def show_calendar(year, month):
    # Display the calendar for the specified year and month
    cal = calendar.month(year, month)
    print("Calendar for {} {}\n".format(calendar.month_name[month], year))
    print("="*35)
    print(cal)
    print("="*35)

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    if month < 1 or month > 12:
        print("Invalid month! Please enter a month between 1 and 12.")
    else:
        show_calendar(year, month)
