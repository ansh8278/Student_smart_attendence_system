import pandas as pd
from datetime import datetime

def markAttendance(name):
    try:
        df = pd.read_csv("attendance.csv")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    now = datetime.now()
    timeString = now.strftime("%H:%M:%S")
    dateString = now.strftime("%Y-%m-%d")

    # Ensure 'Name' column exists before checking for duplicates
    if "Name" not in df.columns:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    if name not in df["Name"].values:
        new_entry = pd.DataFrame([[name, dateString, timeString]], columns=["Name", "Date", "Time"])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv("attendance.csv", index=False)
        print(f"📝 Attendance marked for {name} at {timeString}")

# Test the function (optional)
if __name__ == "__main__":
    markAttendance("TestUser")
