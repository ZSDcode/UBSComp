# Assumption 1: Follows standard regex syntax
# Assumption 2: Will try for most general regex, rather than most specific
# Assumption 3: All repeat characters are on the same index for valid strings
# E.g. if all the valid strings are alphabets, the pattern will still be ^.+$ unless the invalid strings contain numbers

def generate_gree_expression(valid_strings, invalid_strings):
    regex = "^"
    specialChar = ['.', '+', '^', '$', '[', ']', '\\']
    if (checkingFirstRep(valid_strings) and not checkingFirstRep(invalid_strings)):
        regex += checkForSpecial(valid_strings[0][0])
    validRepeats = checkingAnyRep(valid_strings)
    invalidRepeats = checkingAnyRep(invalid_strings)
    crucialRepeats = {}
    if validRepeats:
        for validChar in validRepeats.keys():
            if invalidRepeats:
                if validChar not in invalidRepeats:
                    crucialRepeats[validChar] = validRepeats[validChar]
            else:
                crucialRepeats = validRepeats
    print(crucialRepeats)
    if not crucialRepeats:
        regex += regexAlpNumeric(valid_strings, invalid_strings)
    else:
        repeatChars = []
        for key in crucialRepeats.keys():
            repeatChars.append(key)
        validStringsToCheck = []
        invalidStringsToCheck = []
        for i in range(len(valid_strings)):
            validStringsToCheck.append(valid_strings[i][0:crucialRepeats[repeatChars[0]]])
        for i in range(len(invalid_strings)):
            invalidStringsToCheck.append(invalid_strings[i][0:crucialRepeats[repeatChars[0]]])
        regex += regexAlpNumeric(validStringsToCheck, invalidStringsToCheck)
        regex += checkForSpecial(repeatChars[0])

        if len(repeatChars) > 1:
            validStringsToCheck = []
            invalidStringsToCheck = []
            for i in range(len(valid_strings)):
                validStringsToCheck.append(valid_strings[i][crucialRepeats[repeatChars[0]]:crucialRepeats[repeatChars[1]]])
            for i in range(len(invalid_strings)):
                invalidStringsToCheck.append(invalid_strings[i][crucialRepeats[repeatChars[0]]:crucialRepeats[repeatChars[1]]])
            regex += regexAlpNumeric(validStringsToCheck, invalidStringsToCheck)
            for keyIdx in range(1, len(repeatChars)):
                validStringsToCheck = []
                invalidStringsToCheck = []
                for i in range(len(valid_strings)):
                    validStringsToCheck.append(valid_strings[i][0:crucialRepeats[repeatChars[keyIdx]]])
                for i in range(len(invalid_strings)):
                    invalidStringsToCheck.append(invalid_strings[i][0:crucialRepeats[repeatChars[keyIdx]]])
                if (keyIdx == len(repeatChars)-1):
                    for i in range(len(valid_strings)):
                        validStringsToCheck.append(valid_strings[i][crucialRepeats[repeatChars[keyIdx]]:len(valid_strings[i])])
                    for i in range(len(invalid_strings)):
                        invalidStringsToCheck.append(invalid_strings[i][crucialRepeats[repeatChars[keyIdx]]:len(invalid_strings[i])])
                    regex += checkForSpecial(repeatChars[keyIdx])
                    regex += regexAlpNumeric(validStringsToCheck, invalidStringsToCheck)
                else:
                    for i in range(len(valid_strings)):
                        validStringsToCheck.append(valid_strings[i][crucialRepeats[repeatChars[keyIdx]]:crucialRepeats[repeatChars[keyIdx+1]]])
                    for i in range(len(invalid_strings)):
                        invalidStringsToCheck.append(invalid_strings[i][crucialRepeats[repeatChars[keyIdx]]:crucialRepeats[repeatChars[keyIdx+1]]])
                    regex += regexAlpNumeric(validStringsToCheck, invalidStringsToCheck)
                    regex += checkForSpecial(repeatChars[keyIdx])
        else:
            validStringsToCheck = []
            invalidStringsToCheck = []
            for i in range(len(valid_strings)):
                validStringsToCheck.append(valid_strings[i][crucialRepeats[repeatChars[0]]:len(valid_strings[i])])
            for i in range(len(invalid_strings)):
                invalidStringsToCheck.append(invalid_strings[i][crucialRepeats[repeatChars[0]]:len(valid_strings[i])])
            regex += regexAlpNumeric(validStringsToCheck, invalidStringsToCheck)
    if (checkingLastRep(valid_strings) and not checkingLastRep(invalid_strings)):
        regex += checkForSpecial(valid_strings[0][len(valid_strings[0])-1])
    regex += "$"
    return regex

def checkingFirstRep(strings):
    alpha = strings[0][0]
    repeated = True
    for string in strings:
        if (string[0] != alpha):
            repeated = False
            break
    return repeated

def checkingLastRep(strings):
    lastLetter = strings[0][len(strings[0])-1]
    repeated = True
    for string in strings:
        if (string[len(string)-1] != lastLetter):
            repeated = False
            break
    return repeated

def checkingAnyRep(strings):
    repeatedChar = {}
    for i in range(1, len(strings[0])-1):
        letterToCheck = strings[0][i]
        repeated = True
        for string in strings:
            if (string[i] != letterToCheck):
                    repeated = False
                    break
        if repeated:
            repeatedChar[letterToCheck] = i
    return repeatedChar

def alphabetStringCheck(validStrings, invalidStrings):
    validAlpha = True
    invalidAlpha = False
    for string in validStrings:
        if not string.isalpha():
            validAlpha = False
            break
    for string in invalidStrings:
        if string.isalpha():
            invalidAlpha = True
            break
    if (validAlpha):
        if invalidAlpha:
            return False
        else:
            return True
    else:
        return False
    
def digitStringCheck(validStrings, invalidStrings):
    validDigitStr = True
    invalidDigitStr = False
    for string in validStrings:
        if not string.isdigit():
            validDigitStr = False
            break
    for string in invalidStrings:
        if string.isdigit():
            invalidDigitStr = True
            break
    if (validDigitStr):
        if invalidDigitStr:
            return False
        else:
            return True
    else:
        return False
    
def checkForMoreThanOne(listOfStrings):
    MoreThanOne = False
    for string in listOfStrings:
        if len(string) > 1:
            MoreThanOne = True
            break
    return MoreThanOne

def regexAlpNumeric(valid_strings, invalid_strings):
    addOn = ""
    if alphabetStringCheck(valid_strings, invalid_strings):
        addOn += "\\D"
        if checkForMoreThanOne(valid_strings):
            addOn += "+"
    elif digitStringCheck(valid_strings, invalid_strings):
        addOn += "\\d"
        if checkForMoreThanOne(valid_strings):
            addOn += "+"
    else:
        addOn += "."
        if checkForMoreThanOne(valid_strings):
            addOn += "+"
    return addOn

def checkForSpecial(char):
    specialChar = ['.', '+', '^', '$', '[', ']', '\\']
    if char in specialChar:
        return "\\" + char
    else:
        return "["+ char +"]"