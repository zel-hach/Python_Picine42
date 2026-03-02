
import time
from datetime import datetime

timestamp = time.time()
print(timestamp)
formatted_number = f"{timestamp:,.4f}"
scientific = f"{timestamp:.2e}"

print(f"Seconds since January 1, 1970: {formatted_number} or {scientific} in scientific notation")

now = datetime.now()
print(now)
formatted_date = now.strftime("%b %d %Y")

print(formatted_date)
