import sys
#sys.stdout = open('export.txt', 'w')
num = int(input("Cathook or Lmaobox? (0 or 1): "))
sys.stdout = open('export.txt', 'w') 
with open('ids.txt', "r") as f:
    for line in f:
        numeric_filter = filter(str.isdigit, line)
        f = "".join(numeric_filter)
        if num == 1:
            f = ''.join(('"',f,'"'))
        if num == 1:
            print("playerlist.SetPriority(" + (f) + ", -1);")
        if num == 0:
            print("cat_pl_add_id " + (f) + " CAT")
