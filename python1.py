def char():
    fil = open("words.txt")
    for line in fil:
        words = line.strip()
        if len(words) > 20:
            print(words)
char()
