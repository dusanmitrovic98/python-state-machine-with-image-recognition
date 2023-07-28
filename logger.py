LOG_MESSAGES = True

def log(message):
    if (not LOG_MESSAGES):
        return

    print(message)