def countWord(filepath,word):
    import re
    f = open(filepath)
    text = f.read()
    all_occurences = re.findall('(?<!\w)'+word+'(?!\w)',text,flags=re.IGNORECASE)
    all_occurences = len(all_occurences)
    return all_occurences
