import sys
import re

DICT = {
    '': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def p89(roman):
    if len(roman) <= 1:
        return DICT[roman]
    one_count = {'V':0, 'L': 0, 'D': 0}
    result = 0
    preresult = 0
    for i in range(0, len(roman)):
        curr = roman[i]
        # Rule3
        if curr in one_count:
            if one_count[curr]: return -1
            one_count[curr] = 1
        if i == 0: 
            preresult = DICT[curr]
            continue
        
        prev = roman[i-1]
        # Rule1
        if DICT[prev] > DICT[curr]:
            result = result + preresult
            preresult = DICT[curr]
        elif DICT[prev] == DICT[curr]:
            preresult = preresult + DICT[curr]
            # Rule2
            if preresult == DICT[curr] * 10:
                return -1
        else:
            # subtractive combination
            # SubRule1
            if preresult == DICT[prev] and prev not in "IXC": return -1
            # SubRule2
            if prev == 'I' and curr not in "VX": return -1
            # SubRule3
            if prev == 'X' and curr not in "LC": return -1
            # SubRule4
            if prev == 'C' and curr not in "DM": return -1
            preresult = DICT[curr] - preresult
    result = result + preresult
    
    return result
    
def readlines(file):
    lines = None
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        
    return lines

def fuck(file):
    count = 0
    with open(file, 'r') as f:
        content = f.read()
        return len(content) - len(re.sub(r"DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", "kk", content))

if __name__ == '__main__':
    for l in readlines(sys.argv[1]):
        print "%s = %s" % (l, p89(l))
    print fuck(sys.argv[1])
    