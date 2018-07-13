import os, re

def countWord(filePath, word):
    filePath = os.path.abspath(filePath)
    pattern = re.compile('\\b{}\\b'.format(word))

    with open(filePath) as txtFile:
        file_contents = txtFile.read()
        matches = re.findall(pattern, file_contents)

    return len(matches)
