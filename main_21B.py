import copy

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

calculate = copy.deepcopy(data)

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


left_side = ["humn"]

while "root" not in left_side:
    for e in calculate:
        if isinstance(calculate.get(e), list):
            for k in range(len(left_side)):
                if left_side[k] in calculate.get(e):
                    left_side.append(e)

    left_side = set(left_side)
    left_side = list(left_side)

left_side = set(left_side)
left_side = list(left_side)


data["humn"] = None

c_list = ["root"]


while data.get("humn") == None:

    work_item = c_list.pop()

    operator = calculate.get(work_item)[1]

    if calculate.get(work_item)[0] in left_side:
        to_modify = calculate.get(work_item)[0]
        fixed = calculate.get(work_item)[2]
        fixed_pos = 1
    else:
        to_modify = calculate.get(work_item)[2]
        fixed = calculate.get(work_item)[0]
        fixed_pos = 0

    c_list.append(to_modify)

    res = 0

    if work_item == "root":
        data[to_modify] = data.get(fixed)
    else:
        if operator == "+":

            res = data.get(work_item) - data.get(fixed)
            data[to_modify] = res

        if operator == "*":

            res = int(data.get(work_item) / data.get(fixed))
            data[to_modify] = res

        if operator == "-":

            if fixed_pos == 0:
                res = data.get(fixed) - data.get(work_item)
                data[to_modify] = res
            else:
                res = data.get(fixed) + data.get(work_item)
                data[to_modify] = res
        
        if operator == "/":

            if fixed_pos == 0:
                res = int(data.get(fixed) / data.get(work_item))
                data[to_modify] = res
            else:
                res = data.get(fixed) * data.get(work_item)
                data[to_modify] = res

print("Second part: " + str(data.get("humn")))
