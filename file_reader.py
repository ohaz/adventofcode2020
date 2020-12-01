def reader(filename: str):
    with open(filename, 'r') as f:
        return f.read()

def getFileEntries(filename: str):
    content = reader(filename)
    return content.splitlines()

def getFileEntriesNumbers(filename: str):
    return [int(x) for x in getFileEntries(filename)]