

import random

def getRangeOfCharsFromStart(hexStart: int, hexEnd: int):
    return [ hex(x) for x in list(range(hexStart, hexEnd +1)) ]

def getRandFromList(inList: list):
    return inList[random.randrange(0, len(inList))]

def toStrFromHex(hexIn: str):
    return chr(int(hexIn, 16))

def replaceLetter(letter: str):
    retVal = letter
    replace = random.randrange(0, 2) > 0
    if replace:
        if letter == 'A':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xC0, 0xC5)))
        elif letter == 'B':
            retVal = toStrFromHex(getRandFromList([ '0xDF' ]))
        elif letter == 'C':
            retVal = toStrFromHex(getRandFromList( [ '0xC7']))
        elif letter == 'D':
            retVal = toStrFromHex(getRandFromList( [ '0xD0' ]))
        elif letter == 'E':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xC8, 0xCB)))
        elif letter == 'I':
            retVal = toStrFromHex(getRandFromList( getRangeOfCharsFromStart(0xCC, 0xCF)))
        elif letter == 'N':
            retVal = toStrFromHex(getRandFromList([ '0xD1' ]))
        elif letter == 'O':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xD2, 0xD8)))
        elif letter == 'U':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xD9, 0xDC)))
        elif letter == 'Y':
            retVal = toStrFromHex(getRandFromList([ '0xDD' ]))
        elif letter == 'a':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xE0, 0xE5)))
        elif letter == 'c':
            retVal = toStrFromHex(getRandFromList( [ '0xE7' ]))
        elif letter == 'e':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xE8, 0xEB)))
        elif letter == 'i':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xEC, 0xEF)))
        elif letter == 'n':
            retVal = toStrFromHex(getRandFromList([ '0xF1' ]))
        elif letter == 'o':
            retVal = toStrFromHex(getRandFromList([ '0xF0' ] + getRangeOfCharsFromStart(0xF2, 0xF8)))
        elif letter == 'u':
            retVal = toStrFromHex(getRandFromList(getRangeOfCharsFromStart(0xF9, 0xFC)))
        elif letter == 'y':
            retVal = toStrFromHex(getRandFromList([ '0xFD', '0xFF' ]))
    return retVal

def isCharNotBanned(inChar: chr):
    banList = ['\'', ' ', '\"', '.', '?', '!']
    if inChar not in banList:
        return True
    return False

def curseText(inStr: str):
    outStr = ''.join([ replaceLetter(x) for x in list(inStr) ])
    for _ in range(0, random.randrange(0, int(len(outStr)/3))):
        position = random.randint(0, len(outStr))
        try:
            if isCharNotBanned(outStr[position]) and isCharNotBanned(outStr[position-1]):
                outStr = outStr[:position] + '\'' + outStr[position:]
        except:
            pass
    return outStr

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
