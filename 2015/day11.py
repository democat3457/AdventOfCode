from lib import *

# NOTE: originally solved manually (really easy)

year, day = 2015, 11

puzzle_input = load(year, day)
lines = puzzle_input.splitlines()
line = truthy_list(lines)[0]

def is_valid(pw: str):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    run = False
    pairs = []
    for i in range(len(pw)):
        if i < (len(pw)-1):
            if pw[i] == pw[i+1] and pw[i] not in pairs:
                pairs.append(pw[i])
        if i < (len(pw)-2):
            if (ord(pw[i+2]) - ord(pw[i+1])) == (ord(pw[i+1]) - ord(pw[i])) == 1:
                run = True
    return len(pairs) == 2 and run

def increment_word(word: str):
    idx = len(word) - 1
    if word[idx] != 'z':
        return word[:idx] + chr(ord(word[idx])+1)
    else:
        return increment_word(word[:idx]) + 'a'

while not is_valid(line):
    line = increment_word(line)

# Part 02
line = increment_word(line)
while not is_valid(line):
    line = increment_word(line)

ans(line)
