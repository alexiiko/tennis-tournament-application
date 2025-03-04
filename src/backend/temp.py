from datetime import datetime

date_format = "%d.%m.%Y"
    
# Get the current date
current_date = datetime.now().strftime(date_format)
current_date_obj = datetime.strptime(current_date, date_format)

next_date = "25.02.2025"

next_date_obj = datetime.strptime(next_date, date_format)

delta_days = (next_date_obj - current_date_obj).days

print(delta_days)
