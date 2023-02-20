import glob 

with open("data/all/raw.txt", "r") as r:
    rawlines = r.read().splitlines()

with open("data/all/dialect.txt", "r") as r:
    dialectlines = r.read().splitlines()

for dialectline in dialectlines:
    dialect = dialectline.split("\t")[0]
    rawtodialect = {}
    with open("data/all/raw-dialect.txt", "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            elements = line.split("\t")
            if dialect == elements[2]:
                rawtodialect[elements[0]] = elements[1]
    
    with open(f"data/dialects/{dialect}.txt", "w") as w:
        for rawline in rawlines:
            if rawline in rawtodialect:
                w.write(f"{rawtodialect[rawline]}\n")
            else:
                w.write(f"\n")
