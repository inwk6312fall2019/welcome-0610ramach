def avoids(word, stringHere):
    for letters in word:
        if stringHere in word:
            return False
    return True

def avoids_forbidden():
    user_input = input("Enter a string of forbidden letters!")
    fil = open("words.txt")
    count = 0
    for line in fil:
        words = line.strip()
        if user_input not in words:
            count = count + 1
    print(count)
