import sys
sys.stdout = open('IgnoreList.lua', 'w')
with open('ids.txt', "r") as f:
    for line in f:
        numeric_filter = filter(str.isdigit, line)
        f = "".join(numeric_filter)
        f = ''.join(('"',f,'"'))
        print("playerlist.SetPriority(" + (f) + ", -1);")
