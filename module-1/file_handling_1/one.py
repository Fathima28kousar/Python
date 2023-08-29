f = open("one.txt", "r")
lines = f.readlines()
f.close()

fp = open("new_file.txt", "w")
count = 0

for line in lines:
    if count == 4:
        count += 1
        continue
    else:
        fp.write(line)
        count += 1

fp.close()