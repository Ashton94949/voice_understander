import threading
import time

timers = []

def set_timer(duration, message):
    timer = threading.Timer(duration, lambda: timers.append(message))
    timer.start()
    return f"Timer set for {duration} seconds"

def get_timers():
    due_timers = timers.copy()
    timers.clear()
    return due_timers