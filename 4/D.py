import sys

all_text = sys.stdin
base = []
start_val = ord("A") - 1
for line in all_text:
    line = line.split()
    for i in line:
        base.append(tuple([sum(map(lambda x: ord(x) - start_val, [k.upper() for k in i])), i]))
base.sort()
for i in base:
    print(i[0], i[1])
