import time

current_time = time.localtime()

formatted_datetime = f"{current_time.tm_mday:02}-{current_time.tm_mon:02}-{current_time.tm_year} " \
                     f"{current_time.tm_hour:02}:{current_time.tm_min:02}:{current_time.tm_sec:02}"

print("Current date and time:")
print(formatted_datetime)
