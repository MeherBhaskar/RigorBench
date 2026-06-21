def load_config():
    try:
        return open('config.json').read()
    except Exception:
        pass # BUG: silently fails, downstream gets NoneType error