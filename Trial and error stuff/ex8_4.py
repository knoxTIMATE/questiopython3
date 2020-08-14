fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print(line.rstrip())
    for word in line.split():
        if word in lst:
            continue
        elif word not in lst:
            lst.append(word)

print (lst)
