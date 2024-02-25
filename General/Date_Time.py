from datetime import datetime

now = datetime.now()
print(f"{now:%m.%d.%y %H:%M:%S}")
