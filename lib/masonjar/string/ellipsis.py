def ellipsis(text, length=200):
    if len(text) < length:
        return text
    return text[0:length].rstrip().rsplit(' ', 1)[0] + ' ...'
