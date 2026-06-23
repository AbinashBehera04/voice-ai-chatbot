from datetime import datetime

def wishMe():
    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"

    elif hour < 18:
        return "Good Afternoon"

    else:
        return "Good Evening"


def getTime():
    return datetime.now().strftime("%I:%M %p")