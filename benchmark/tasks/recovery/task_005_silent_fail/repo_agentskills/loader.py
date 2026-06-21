def load_config():
    try:
        return open('config.json').read()
    except Exception:
        raise