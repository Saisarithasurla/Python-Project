import wikipedia

def search_wikipedia(query):
    try:

        search_results = wikipedia.search(query)
        if len(search_results) == 0:
            return "Sorry, I could not find any information."

        summary = wikipedia.summary(search_results[0], sentences=2)
    except Exception as e:
        summary = f"Sorry, I could not find any information. ({e})"
    return summary

