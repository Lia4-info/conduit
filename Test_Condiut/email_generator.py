import time
from datetime import datetime

now = datetime.now()
print(now)
email_num = now.strftime("%d%H")
username = f"TKori{email_num}"
print(username)
email = f"tk{email_num}@mail.com"
print(email)
password = f"TKpass{email_num}"
print(password)


