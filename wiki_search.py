import wikipedia


def search_wikipedia(topic):

    try:
        result = wikipedia.summary(topic, sentences=2)
        return result

    except Exception:
        return "No information found."