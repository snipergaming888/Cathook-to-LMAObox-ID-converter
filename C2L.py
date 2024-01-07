import sys
ask = int(input('Ignore or Target These IDs? (0,1):'))
sys.stdout = open('IgnoreList.lua', 'w')
with open('ids.txt', "r") as f:
    for line in f:
        numeric_filter = filter(str.isdigit, line)
        f = "".join(numeric_filter)
        f = ''.join(('"',f,'"'))
        if ask == 0:
            print("playerlist.SetPriority(" + (f) + ", -1);")
        else:
            print("playerlist.SetPriority(" + (f) + ", 0);")
