from datetime import datetime, timezone
import locale


today = datetime.now(tz=timezone.utc)
print(today)

today_sin_utc = datetime.now(tz=None)
print(today_sin_utc)

date_time = datetime(year=2019, month=12, day=31, hour=23, minute=59, second=59, tzinfo=None)

print("============")
print(f"date_time {date_time}")
print(f"date_time {date_time.year}")
print(f"date_time {date_time.month}")
print(f"date_time {date_time.day}")
print(f"date_time {date_time.hour}")
print(f"date_time {date_time.minute}")
print(f"date_time {date_time.second}")
print(f"date_time {date_time.microsecond}") 

#setear español
# locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8') #Spanish_Spain.1252
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
date_format = datetime.strftime(date_time, '%d de %b de %Y')
print(f"date_format {date_format}")

