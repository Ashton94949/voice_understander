from openai_module import query_openai
from features.reminders import set_reminder, get_reminders
from features.weather import get_weather
from features.smart_home import control_device
from features.timers import set_timer, get_timers
from features.music import play_music

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
    elif "control" in text.lower() and "device" in text.lower():
        parts = text.split()
        device_name = parts[parts.index("device") + 1]
        action = parts[parts.index("control") + 1]
        response = control_device(device_name, action)
    elif "set timer" in text.lower():
        parts = text.split()
        duration = int(parts[parts.index("for") + 1])
        message = " ".join(parts[parts.index("for") + 2:])
        response = set_timer(duration, message)
    elif "get timers" in text.lower():
        timers = get_timers()
        if timers:
            response = "The following timers have finished:\n" + "\n".join(timers)
        else:
            response = "You have no finished timers."
    elif "play music" in text.lower():
        song_name = text.split("play music")[-1].strip()
        response = play_music(song_name)
    else:
        response = query_openai(text)
    return response
