import re

def ArrayChallenge(strArr):
    pattern = r'\d+'
    max_x = -1
    max_y = -1
    min_x = 10**300
    min_y = 10**300

    for i, x in enumerate(strArr):
        digits = re.findall(pattern, x)
        strArr[i] = [int(d) for d in digits]
        if strArr[i][0] > max_x:
            max_x = strArr[i][0]
        if strArr[i][0] < min_x:
            min_x = strArr[i][0]
        if strArr[i][1] > max_y:
            max_y = strArr[i][1]
        if strArr[i][1] < min_y:
            min_y = strArr[i][1]

    return ((max_x - min_x) * (max_y - min_y))

print(ArrayChallenge(["(1 1)","(1 3)","(3 1)","(3 3)"]))
