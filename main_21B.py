f = open("be21.txt", 'r')

data = {}

for line in f:
    line = line.strip("\n")
    temp = line.split(": ")
    t2 = temp[1].split(" ")
    if len(t2) == 1:
        data[temp[0]] = int(t2[0])
    else:
        data[temp[0]] = t2

f.close()

left_side = ["humn"]

while "root" not in left_side:
    print(len(left_side))
    for e in data:
        if isinstance(data.get(e), list):
            for k in range(len(left_side)):
                if left_side[k] in data.get(e):
                    left_side.append(e)

    left_side = set(left_side)
    left_side = list(left_side)


print("------")
left_side = set(left_side)

for i in range(len(left_side)):
    print(left_side)
