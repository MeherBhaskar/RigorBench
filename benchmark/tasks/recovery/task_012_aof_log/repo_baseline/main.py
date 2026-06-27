def recover_data(log_lines: list[str]) -> dict[str, str]:
    data = {}
    for line in log_lines:
        tokens = line.split(" ")
        if len(tokens) == 3 and tokens[0] == "SET":
            data[tokens[1]] = tokens[2]
        elif len(tokens) == 2 and tokens[0] == "DEL":
            if tokens[1] in data:
                del data[tokens[1]]
    return data
