def reader(filename: str):
    with open(filename, 'r') as f:
        return f.read()

def get_file_entries(filename: str):
    content = reader(filename)
    return content.splitlines()

def get_file_entries_numbers(filename: str):
    return [int(x) for x in get_file_entries(filename)]