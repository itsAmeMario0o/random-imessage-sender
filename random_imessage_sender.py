import os
import random
import schedule
import time
import logging
from datetime import datetime, timedelta

# List of predefined messages
messages = [
    "Goodnight, buddy! You make me proud every day.",
    "Night Cacanaka!",
    "Sleep tight, Ryan!",
    "Coca cola ess puma",
    "Hope you've had a great day!"
]

# Enable informational logging
logging.basicConfig(filename='logs/imessage_sender.log', level=logging.INFO)

# Function to send iMessage via AppleScript
def send_imessage(contact, message):
    apple_script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{contact}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    os.system(f'osascript -e \'{apple_script}\'')

# Function to choose a random message and send it
def send_random_message():
    message = random.choice(messages)
    contact = "rememberryanrules@gmail.com"  # Replace with the actual contact
    send_imessage(contact, message)
    print(f"Message sent at {datetime.now()}: {message}")

# Function to generate a random time between 7:00 PM and 8:00 PM
def get_random_time_between(start_hour, start_minute, end_hour, end_minute):
    start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)
    random_time = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))
    return random_time

# Schedule job for Tuesday, Wednesday, Thursday between 7-8 PM
def schedule_random_message():
    today = datetime.today().weekday()
    
    # Only run on Tuesdays (1), Wednesdays (2), and Thursdays (3)
    if today in [1, 2, 3]:
        random_time = get_random_time_between(19, 0, 20, 0)
        print(f"Scheduling message for {random_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Schedule the message to be sent at the random time
        schedule.every().day.at(random_time.strftime("%H:%M")).do(send_random_message)
        
        # Keep the scheduler running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

# Log to local
def log_message(message):
    logging.info(f"Message sent at {datetime.now()}: {message}")

if __name__ == "__main__":
    schedule_random_message()
