with open(f"data-Swiss/all/raw.txt") as r:
    rawlines = r.read().splitlines()

id = 1
standards = {}
with open("data-Swiss/all/raw-dialect.txt", "r") as r:
    lines = r.read().splitlines()
    for line in lines:
        elements = line.split("\t")
        if id == (int)(elements[0]):
            standard = elements[1]
            id += 1
            continue
        else:
            standards[elements[1]] = standard

options = {}
with open(f"data-Swiss/all/blank-dialect.txt", "r") as r:
    lines = r.read().splitlines()
    for line in lines:
        elements = line.split("\t")
        if elements[1] not in options:
            options[elements[1]] = [elements[2]]
        else:
            options[elements[1]].append(elements[2])

dialects = {}
with open(f"data-Swiss/all/raw-dialect.tsv", "r") as r:
    lines = r.read().splitlines()
    for line in lines:
        elements = line.split("\t")
        if elements[2] != "standard":
            if elements[2] not in dialects:
                dialects[elements[2]] = [elements[1]]
            else:
                dialects[elements[2]].append(elements[1])

for dialect in dialects:
    with open(f"data-Swiss/dialects_clean/{dialect}_standard.deu", "w") as wr:
        with open(f"data-Swiss/dialects_clean/{dialect}.deu", "w") as ws:
            for variation in dialects[dialect]:
                if variation in options:
                    for option in options[variation]:
                        ws.write(f"{option}\n")
                        wr.write(f"{standards[variation]}\n")