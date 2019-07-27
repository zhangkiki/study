import sys

for arg in sys.argv[1:]:
    i = arg.__len__()
    if i >= 3:
        print(arg)
