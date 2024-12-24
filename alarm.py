# Import libraries
import time
import webbrowser
import random
import os

# Check if the user has the YT.txt file in the same area as alarm.py
if not os.path.isfile("YT.txt"):
    print("ERROR: YT.txt file not present. Creating file...")
    with open("YT.txt", 'w') as fileCreated:
        fileCreated.write("https://youtu.be/BZg8BhBWyo8\nhttps://youtu.be/dQw4w9WgXcQ")

# The User can set the time they want to wake up. The string the user puts in must match the example format to work.
print("What time do you want to wake up?")
print("Use this form.\nExample: 06:30")
Alarm = input("> ").strip()

# Validate user input for the correct time format
try:
    time.strptime(Alarm, "%H:%M")  # This will raise a ValueError if the format is incorrect
except ValueError:
    print("Invalid time format! Please use HH:MM (24-hour format).")
    exit()

# State the Time variable so it's usable in the while-loop
print("Waiting for the alarm...")

while True:
    # Get the current system time in the format HH:MM
    Time = time.strftime("%H:%M")
    
    # Check if the current time matches the alarm
    if Time == Alarm:
        print("Time to Wake up!")
        # Open a random link from YT.txt
        with open("YT.txt") as f:
            content = [line.strip() for line in f if line.strip()]  # Clean up the file content
        random_video = random.choice(content)
        print("Opening URL:", random_video)
        webbrowser.open(random_video)
        break  # Exit the loop after the alarm triggers
    
    # Pause for a second to avoid excessive CPU usage
    time.sleep(1)
