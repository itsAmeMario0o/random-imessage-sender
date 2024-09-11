# Random iMessage Sender Script

This Python script sends an iMessage from a predefined list to a contact at a random time between 7:00 PM and 8:00 PM only on Tuesdays, Wednesdays, and Thursdays.

## Prerequisites

1. **MacOS**: This script is designed to run on MacOS, as it uses AppleScript to send messages through the Messages app.
2. **Python 3.x**: Make sure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
3. **osascript**: This is used to execute AppleScript commands to send iMessages. It is pre-installed on MacOS.

## Required Python Modules

The script requires the `schedule` module to handle time-based scheduling. Install it using `pip`:

```
bash
pip install schedule
```

## Setup

1. **Clone the repository**: Download or clone the repository to your local machine.

```
git clone https://github.com/itsAmeMario0o/random-imessage-sender
cd random-imessage-sender
```

2. **Modify the Script**:

Open the random_imessage_sender.py file.

Replace the placeholder "recipient_phone_or_email" with the actual phone number or email address of the person you want to send the iMessage to. 

For example:

```
contact = "555-123-4567"  # Replace with recipient's phone number
```

You can also modify the list of messages in the messages array to fit your needs.

## How to Run the Script

1. **Run the script Manually**: Simply run the script with Python. It will check if the current day is Tuesday, Wednesday, or Thursday, and if so, it will schedule a message between 7:00 PM and 8:00 PM for that day.

```
python3 random_imessage_sender.py
```
2. **Keep the Script Running**:

The script will continue running in the background, checking every minute if it needs to send a message at the scheduled time.

You can keep the terminal window open to observe the logs of the message sent, or run the script as a background process.

3. **Cron Job (Optional)**:

To ensure the script starts automatically every day, you can set up a cron job (or another scheduler like launchd on MacOS) to run the script at boot or at a specific time each day. 

Example of adding a cron job:

```
crontab -e
```

Add the following line to run the script daily at 6:50 PM (just before the window opens):
```
50 18 * * 2-4 /usr/local/bin/python3 /path/to/random_imessage_sender.py
```

NOTE - Update /path/to/random_imessage_sender.py to the full path of the script on your system