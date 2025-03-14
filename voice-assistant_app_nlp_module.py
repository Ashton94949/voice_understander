from claude_module import query_claude
from features.reminders import set_reminder, get_reminders
from features.weather import get_weather

def process_query(text):
    if "set reminder" in text.lower():
        response = set_reminder(text)
    elif "get reminders" in text.lower():
        reminders = get_reminders()
        if reminders:
            response = "You have the following reminders:\n" + "\n".join([reminder[1] for reminder in reminders])
        else:
            response = "You have no reminders."
    elif "weather" in text.lower():
        location = text.split("in")[-1].strip()
        response = get_weather(location)
    else:
        response = query_claude(text)
    return response
