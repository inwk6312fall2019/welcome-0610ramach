def has_no_e_one():
    fil = open('words.txt')
    for line in fil:
        if line.find("e") == -1:
            return("True")

def has_no_e():
    fil = open("words.txt")
    numb_of_words = 0
    count = 0
    for line in fil:
        numb_of_words = numb_of_words + 1
        words = line.strip()
        if words.find("e") == -1:
            print(words)
            count = count + 1
    percent_of_words = (count/number_of_words) * 100
    print("Percent:", percent_of_words)


