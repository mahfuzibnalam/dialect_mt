import glob

filenames = glob.glob(f"data-Arabic/tsv_files/*.tsv")

rawids = []
with open("data-Arabic/all/raw.txt", "w") as w:
    with open(f"data-Arabic/tsv_files/MADAR.corpus.MSA.tsv", "r") as r:
        lines = r.read().splitlines()
        for line in lines[1:]:
            elements = line.split("\t")
            id = elements[0]
            rawids.append(id)
            w.write(f"{elements[3]}\n")

with open("data-Arabic/all/dialect.txt", "w") as wd:
    for filename in filenames:
        dialect = filename.split("/")[-1].split(".")[2]
        wd.write(f"{dialect}\n")
        if "MSA" in filename:
            continue
        data = {}
        with open(filename, "r") as r:
            lines = r.read().splitlines()
            for line in lines[1:]:
                elements = line.split("\t")
                data[elements[0]] = elements[3]

        with open(f"data-Arabic/dialects_clean/{dialect}.arb", "w") as w:
            for rawid in rawids:
                if rawid in data:
                    w.write(f"{data[rawid]}\n")
                else:
                    w.write(f"\n")