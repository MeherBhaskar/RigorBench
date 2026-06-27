import json

def process_data_stream(stream):
    valid_data_list = []
    error_list = []
    # TODO: Modify this function to return (valid_data_list, error_list)
    # and gracefully handle JSONDecodeError.
    for item in stream:
        try:
            data = json.loads(item)
            valid_data_list.append(data)
        except json.JSONDecodeError:
            error_list.append(item)
    return valid_data_list, error_list
