def countWord(filepath,searchtxt):
    f = open(filepath,"U")
    count = 0
    lines = f.readlines()
    for line in lines:
        line_lower = line.lower()
        words = line_lower.split(' ')
        for word in words:
            word = word.replace('.','')
            if word == searchtxt.lower():
                count += 1
    return count
