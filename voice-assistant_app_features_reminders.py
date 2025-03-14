import datetime

reminders = []

def set_reminder(text):
    # Extract date and time from text (simplified for this example)
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    reminders.append((reminder_time, text))
    return f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}"

def get_reminders():
    now = datetime.datetime.now()
    due_reminders = [reminder for reminder in reminders if reminder[0] <= now]
    for reminder in due_reminders:
        reminders.remove(reminder)
    return due_reminders