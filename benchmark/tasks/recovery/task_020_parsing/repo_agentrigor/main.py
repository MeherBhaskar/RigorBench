import json

def process_data_stream(stream):
    valid_data_list = []
    # TODO: Modify this function to return (valid_data_list, error_list)
    # and gracefully handle JSONDecodeError.
    for item in stream:
        data = json.loads(item)
        valid_data_list.append(data)
    return valid_data_list
