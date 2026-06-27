def recover_data(log_lines: list[str]) -> dict[str, str]:
    store = {}
    for line in log_lines:
        tokens = line.split(" ")
        if len(tokens) == 3 and tokens[0] == "SET":
            store[tokens[1]] = tokens[2]
        elif len(tokens) == 2 and tokens[0] == "DEL":
            store.pop(tokens[1], None)
    return store
