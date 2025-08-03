def generate_gree_expression(valid_strings, invalid_strings):
    regex = ""
    specialChar = ['.', '+', '*', '?', '^', '$', '(', ')', '[', ']', '{', '}', '|', '\\']
    validStringsParse = []
    for string in valid_strings:
        stringParse = []
        for char in string:
            if (char.isdigit()):
                stringParse.append("num")
            elif (char.isalpha()):
                stringParse.append("alp")
            else:
                stringParse.append(char)
        validStringsParse.append(stringParse)

def checkingRep(strings):
    lengthOfString = len(strings[0])
    charsInIndexOrder = []
    for j in range(lengthOfString):
        charInParticularIdx = []
        for i in range(len(strings)):
            charInParticularIdx.append(strings[i][j])
        charsInIndexOrder.append(charInParticularIdx)
    repeatedCharsAndIdx = []
    for i in range(len(charsInIndexOrder)):
        if (len(set(charsInIndexOrder[i])) == 1):
            repeatedCharsAndIdx.append((i, charsInIndexOrder[i][0]))
    print(repeatedCharsAndIdx)

checkingRep(["abc", "aef", "a23"])
checkingRep(["abc", "def", "123"])