import datetime as dt
from signup import username as un
username = un
print(f"-----Welcome {username} to your personal diary!-----")
details = input("Enter your today activities: ""\n")
time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("dairy.csv", "a") as f:
    f.writelines(str(f"{username}:{time}: {details}" + "\n"))
print("Your details have been saved to your diary.")
import sorting
