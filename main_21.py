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

while isinstance(data.get("root"), list):
    for e in data:
        if isinstance(data.get(e), list):
            if isinstance(data.get(data.get(e)[0]), int) and isinstance(data.get(data.get(e)[2]), int):
                if data.get(e)[1] == "+":
                    data[e] = data.get(data.get(e)[0]) + data.get(data.get(e)[2])

                elif data.get(e)[1] == "-":
                    data[e] = data.get(data.get(e)[0]) - data.get(data.get(e)[2])

                elif data.get(e)[1] == "*":
                    data[e] = data.get(data.get(e)[0]) * data.get(data.get(e)[2])

                else:
                    data[e] = int(data.get(data.get(e)[0]) / data.get(data.get(e)[2]))



print(data.get("root"))
