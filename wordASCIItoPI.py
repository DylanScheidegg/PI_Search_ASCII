from mpmath import mp


def create():
    # Number of digits
    mp.dps = 1000000

    # Writing the digits of pi
    f = open('pi.txt', 'w')
    f.write(str(mp.pi))


def load():
    # Read the file so it doesnt have to keep finding pi
    f = open('pi.txt', 'r')
    data = f.read()

    # Write to list
    loadpi = []
    for x in data:
        loadpi.append(x)
    return loadpi[2:]


# Check to make sure the pi file exists
pinums = load()
if len(pinums) == 0:
    # If the file is empty then write the file
    create()
else:
    # Converts the pi list to a singular word
    piWhole = ''.join(c for c in pinums)

    # Takes user input
    word = input('Word to find in pi: ')

    # Converts user input to ascii to be searched
    ascWord = ''.join(str(ord(c)) for c in word)
    print(word, ascWord)

    # Checks if the ascii text is in the pi list
    if ascWord in piWhole:
        # Gets the index of the first value
        ind = piWhole.index(ascWord)

        # Prints the index then prints some of the values after to make sure it works
        print("Index: " + str(ind), "Value 1: " + str(piWhole[ind]), "Value 2: " + str(piWhole[ind + 1]))
    else:
        # Tell the user the values do not exist
        print(str(word), str(ascWord) + ": Does not exist in the first million digits of pi")

