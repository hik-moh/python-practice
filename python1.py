import datetime

# 1. Get current date and time
now = datetime.datetime.now()
print("current Date & Time: ", now)

# 2. Extract specific parts
print("Year: ", now.year)
print("Month: ", now.month)
print("Day: ", now.day)
print("Time:", now.strftime("%H:%M:%S"))

# 3. Format date nicely (e.g., "Friday, Nov 06, 2026")
formatted_date = now.strftime("%A, %b %d, %Y")
print("Formatted Date: ", formatted_date)

# 4. Create a specific past/future date
custom_date = datetime.datetime(2026, 12, 25)
print("christmas 2026: ", custom_date)