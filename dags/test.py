# https://www.iana.org/time-zones
import pendulum

now = pendulum.now("Asia/Kolkata")

print(f"Current date and time in Asia/Kolkata timezone: {now}")
print(f"Current year: {now.year}")
print(f"Current month: {now.month}")
print(f"Current day: {now.day}")
print(f"Current hour: {now.hour}") 