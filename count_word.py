def countWord(file_path, keyword):
    f = open(file_path)
    contents = f.read()
    return contents.count(keyword)
