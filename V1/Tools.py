def textFormat(text):
    width = 60
    leftSpaces = (width - len(text)) // 2
    rightSpaces = width - len(text) - leftSpaces

    border = "|"
    line = border + (" " * leftSpaces) + text + (" " * rightSpaces) + border
    print(line)

    line = "|" + ("-" * 60) + "|"
    print(line)
