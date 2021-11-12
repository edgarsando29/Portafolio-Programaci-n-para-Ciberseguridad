# Detect English module
# https://www.nostarch.com/crackingcodes (BSD Licensed)

# To use, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# https://invpy.com/dictionary.txt)
MAYUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Agregar Ñ, acentos y diéresis
LETRAS_Y_ESPACIOS = MAYUSCULAS + MAYUSCULAS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictEsp.txt', encoding='utf-8')
    #dictionaryFile = open('dictEsp.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

SPANISH_WORDS = loadDictionary()

def getSpanishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    matches = 0
    for word in possibleWords:
        if word in SPANISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETRAS_Y_ESPACIOS:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isSpanish(message, wordPercentage=40, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getSpanishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch
