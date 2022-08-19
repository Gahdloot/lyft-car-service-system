from datetime import datetime

first_time = datetime(2012, 3, 5, 23, 8, 15)
second_time = datetime.now()
duration_in_seconds = (second_time - first_time).total_seconds()

years = divmod(duration_in_seconds, 31536000)[0]
print(round(years))